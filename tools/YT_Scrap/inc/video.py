from datetime import datetime
import xml.etree.ElementTree as ET
from urllib.request import urlopen

import yt_dlp
from typing import TYPE_CHECKING, cast

from inc.constants import YDL_OPTS_DETAIL_ANDROID

if TYPE_CHECKING:
    from yt_dlp.YoutubeDL import _Params


_RSS_PUBLISHED_DATES_CACHE = {}


def _parse_yyyymmdd(value):
    if not isinstance(value, str):
        return None
    text = value.strip()
    if len(text) != 8 or not text.isdigit():
        return None
    try:
        return datetime.strptime(text, "%Y%m%d")
    except Exception:
        return None


def _datetime_to_yyyymmdd(dt):
    if not isinstance(dt, datetime):
        return None
    return dt.strftime("%Y%m%d")


def _extract_date_from_rss(video_id, channel_id):
    if not isinstance(video_id, str) or not video_id:
        return None
    if not isinstance(channel_id, str) or not channel_id:
        return None

    rss_dates = fetch_channel_rss_published_dates(channel_id)
    rss_date = rss_dates.get(video_id)
    return _parse_yyyymmdd(rss_date)


def _parse_timestamp_safely(raw_ts):
    if not isinstance(raw_ts, (int, float)):
        return None
    if raw_ts <= 0:
        return None
    try:
        dt = datetime.fromtimestamp(raw_ts)
    except Exception:
        return None

    # Garde-fou: ignorer les dates manifestement invalides/futures.
    if dt.year < 2005:
        return None
    if dt > datetime.now() and (dt - datetime.now()).total_seconds() > 86400:
        return None
    return dt


def _is_probably_extraction_time(dt):
    if not isinstance(dt, datetime):
        return False
    # Certains retours yt-dlp exposent la date d'extraction (maintenant)
    # a la place de la date de publication.
    return abs((datetime.now() - dt).total_seconds()) <= 36 * 3600


def timestamp2fr(ts: float) -> str:
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%d/%m/%Y %H:%M:%S")


def timestamp_fr_to_epoch(timestamp_fr):
    if not isinstance(timestamp_fr, str):
        return None
    try:
        dt = datetime.strptime(timestamp_fr, "%d/%m/%Y %H:%M:%S")
        return dt.timestamp()
    except Exception:
        return None


def format_duration(seconds):
    if seconds is None:
        return "N/A"

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = int(seconds % 60)

    if hours == 0:
        return f"{minutes:02d}:{remaining_seconds:02d}"
    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"


def format_date(date):
    if date is None:
        return "N/A"
    try:
        return date.strftime("%d/%m/%Y")
    except Exception:
        return "N/A"


def _coerce_known_date(value):
    if isinstance(value, datetime):
        return value

    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None

        if len(text) == 8 and text.isdigit():
            try:
                return datetime.strptime(text, "%Y%m%d")
            except Exception:
                return None

        for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d"):
            try:
                return datetime.strptime(text, fmt)
            except Exception:
                continue

    return None


def normalize_video_dates(raw_date=None, raw_date_fr=None, raw_datetime=None):
    """Retourne un tuple (date_yyyymmdd|None, date_fr)."""
    dt = _coerce_known_date(raw_datetime)
    if dt is None:
        dt = _coerce_known_date(raw_date)
    if dt is None:
        dt = _coerce_known_date(raw_date_fr)

    if dt is None:
        return None, "N/A"

    return dt.strftime("%Y%m%d"), dt.strftime("%d/%m/%Y")


def extract_video_datetime(video):
    if not isinstance(video, dict):
        return None

    upload_dt = _parse_yyyymmdd(video.get("upload_date"))
    if upload_dt is not None:
        return upload_dt

    release_dt = _parse_yyyymmdd(video.get("release_date"))
    if release_dt is not None:
        return release_dt

    rss_dt = _extract_date_from_rss(video.get("id"), video.get("channel_id"))
    if rss_dt is not None:
        return rss_dt

    for key in ("release_timestamp", "available_at"):
        dt = _parse_timestamp_safely(video.get(key))
        if dt is not None:
            return dt

    ts_dt = _parse_timestamp_safely(video.get("timestamp"))
    if ts_dt is not None and not _is_probably_extraction_time(ts_dt):
        return ts_dt

    return None


def build_video_payload(v):
    date = extract_video_datetime(v)
    date_yyyymmdd, date_fr = normalize_video_dates(
        raw_date=v.get("upload_date") or v.get("release_date"),
        raw_date_fr=v.get("date_fr"),
        raw_datetime=date,
    )
    return {
        "id": v.get("id"),
        "titre": v.get("title"),
        "date": date_yyyymmdd,
        "date_fr": date_fr,
        "duration": v.get("duration"),
        "duree": format_duration(v.get("duration")),
        "url": v.get("webpage_url"),
        "vues": v.get("view_count"),
        "likes": v.get("like_count"),
    }


def fetch_channel_rss_published_dates(channel_id):
    if not isinstance(channel_id, str) or not channel_id:
        return {}

    cached = _RSS_PUBLISHED_DATES_CACHE.get(channel_id)
    if isinstance(cached, dict):
        return cached

    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    published_by_video_id = {}
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
    }

    try:
        with urlopen(feed_url, timeout=8) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)
        for entry in root.findall("atom:entry", ns):
            video_id = entry.findtext("yt:videoId", default="", namespaces=ns)
            published = entry.findtext("atom:published", default="", namespaces=ns)
            if not video_id or not published:
                continue
            try:
                published_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
                published_by_video_id[video_id] = published_dt.strftime("%Y%m%d")
            except Exception:
                continue
    except Exception:
        published_by_video_id = {}

    _RSS_PUBLISHED_DATES_CACHE[channel_id] = published_by_video_id
    return published_by_video_id


def resolve_unavailable_upload_date(entry, video_id):
    if isinstance(entry, dict):
        upload_date = entry.get("upload_date")
        if isinstance(upload_date, str) and upload_date:
            return upload_date

        rss_dt = _extract_date_from_rss(video_id, entry.get("channel_id"))
        rss_yyyymmdd = _datetime_to_yyyymmdd(rss_dt)
        if isinstance(rss_yyyymmdd, str):
            return rss_yyyymmdd

        for ts_key in ("timestamp", "release_timestamp"):
            dt = _parse_timestamp_safely(entry.get(ts_key))
            yyyymmdd = _datetime_to_yyyymmdd(dt)
            if isinstance(yyyymmdd, str):
                return yyyymmdd

    return None


def build_unavailable_video_payload(entry, video_id, video_url=None):
    title = None
    upload_date = None
    duration = None
    view_count = None
    if isinstance(entry, dict):
        title = entry.get("title")
        upload_date = resolve_unavailable_upload_date(entry, video_id)
        duration = entry.get("duration")
        view_count = entry.get("view_count")

    safe_title = title if isinstance(title, str) and title.strip() else "[INDISPONIBLE]"
    safe_date = upload_date if isinstance(upload_date, str) and upload_date else None
    safe_duration = None
    if isinstance(duration, (int, float)):
        safe_duration = max(0, int(round(float(duration))))

    safe_views = int(view_count) if isinstance(view_count, (int, float)) else 0
    url = video_url or f"https://www.youtube.com/watch?v={video_id}"

    date_yyyymmdd, date_fr = normalize_video_dates(
        raw_date=safe_date,
        raw_date_fr=entry.get("date_fr") if isinstance(entry, dict) else None,
    )

    return {
        "id": video_id,
        "titre": safe_title,
        "date": date_yyyymmdd,
        "date_fr": date_fr,
        "duration": safe_duration,
        "duree": format_duration(safe_duration),
        "url": url,
        "vues": safe_views,
        "likes": None,
    }


def try_extract_video_detail_android(video_url, fallback_video_id=None):
    if not isinstance(video_url, str) or not video_url:
        return None

    android_opts = dict(YDL_OPTS_DETAIL_ANDROID)
    android_opts["extractor_args"] = {"youtube": {"player_client": ["android"]}}

    try:
        with yt_dlp.YoutubeDL(cast("_Params", android_opts)) as ydl_android:
            detail = ydl_android.extract_info(video_url, download=False)
        if not isinstance(detail, dict):
            return None

        payload = dict(detail)
        if not isinstance(payload.get("id"), str) and isinstance(fallback_video_id, str):
            payload["id"] = fallback_video_id
        if not isinstance(payload.get("webpage_url"), str):
            payload["webpage_url"] = video_url
        return payload
    except Exception:
        return None


def video_sort_key(video):
    if not isinstance(video, dict):
        return datetime.min

    date_str = video.get("date")
    if isinstance(date_str, str):
        try:
            return datetime.strptime(date_str, "%Y%m%d")
        except ValueError:
            pass

    date_fr = video.get("date_fr")
    if isinstance(date_fr, str):
        try:
            return datetime.strptime(date_fr, "%d/%m/%Y")
        except ValueError:
            pass

    return datetime.min


def pluralize_fr(value, singular, plural=None):
    if plural is None:
        plural = singular + "s"
    return singular if value == 1 else plural


def format_remaining_time_fr(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    parts = []

    if hours > 0:
        parts.append(f"{hours} {pluralize_fr(hours, 'heure')}")
    if minutes > 0:
        parts.append(f"{minutes} {pluralize_fr(minutes, 'minute')}")

    if not parts:
        return "0 minute"

    return " et ".join(parts)


def compute_effective_total(total_playlist, excluded_count):
    if not isinstance(total_playlist, int):
        return None
    safe_excluded = excluded_count if isinstance(excluded_count, int) else 0
    if safe_excluded < 0:
        safe_excluded = 0
    return max(0, total_playlist - safe_excluded)


def is_scrap_complete(scraped, effective_total):
    if not isinstance(scraped, int) or not isinstance(effective_total, int):
        return False
    if effective_total == 0:
        return scraped == 0
    return scraped >= effective_total
