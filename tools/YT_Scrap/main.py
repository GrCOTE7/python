from datetime import datetime
from importlib import import_module
import re
import select
import json, locale, os, shutil, time, threading, yt_dlp
from tabulate import tabulate
from yt_dlp.utils import DownloadError
from typing import TYPE_CHECKING, Optional, TypedDict, cast
from urllib.parse import parse_qs, urlparse
import inc.authors as auth

# ❌ Compatibilité de PyMoX-Kit & locazle avec Linux (Cf. GH spaces)
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

# try:
#     from pymox_kit import cls, end
# except Exception:
#     # Fallback minimal si pymox_kit échoue (ex: locale fr_FR absente).
#     def cls():
#         import subprocess

#         try:
#             subprocess.run(["clear"], check=False)
#         except Exception:
#             print("\033[2J\033[H", end="")

from pymox_kit import cls, end, SB, R, YELLOW, GREEN, RED, CYAN, nf

# ❌ Looker ce qui n'a pas été refait ici par rapport à to_see.py et del to_see

if TYPE_CHECKING:
    from yt_dlp.YoutubeDL import _Params


def ini(ida):
    global AUTHOR, URL, SCRIPT_DIR, STORAGE_DIR, OUTPUT_FILE, OUTPUT_MD_FILE, CACHE_TTL, MAX_CUMULATED_403_ERRORS, PAUSE_ON_RATE_LIMIT, MAX_STALL_RETRIES, TOTAL_PLAYLIST_DROP_GUARD_RATIO, PLAYLIST_FETCH_TIMEOUT_SECONDS, PLAYLIST_FETCH_MAX_TOTAL_SECONDS, get_valid_cache_entry, _cache_utils_module

    AUTHOR = auth.get_author_name(ida)  # 1 → 16
    URL = f"https://www.youtube.com/@{AUTHOR}/videos"

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    STORAGE_DIR = os.path.join(SCRIPT_DIR, "cache")

    OUTPUT_FILE = os.path.join(STORAGE_DIR, f"{AUTHOR}_videos.json")  # 2ar
    OUTPUT_MD_FILE = os.path.join(STORAGE_DIR, f"{AUTHOR}_YT.md")
    # CACHE_TTL = 86400  # 3600 = 1 heure - 86400 = 1 jour
    CACHE_TTL = 86400

    MAX_CUMULATED_403_ERRORS = 7
    PAUSE_ON_RATE_LIMIT = 5  # secondes d'attente avant reprise automatique
    MAX_STALL_RETRIES = 3  # passes sans progression avant arrêt définitif
    TOTAL_PLAYLIST_DROP_GUARD_RATIO = 0.03  # 3%
    PLAYLIST_FETCH_TIMEOUT_SECONDS = 45  # timeout d'inactivité (pas un timeout global)
    PLAYLIST_FETCH_MAX_TOTAL_SECONDS = 900  # garde-fou global (15 min)

    _cache_utils_module = import_module(
        f"{__package__}.cache_utils" if __package__ else "cache_utils"
    )

    get_valid_cache_entry = _cache_utils_module.get_valid_cache_entry


class YdlOpts(TypedDict, total=False):
    extract_flat: bool
    quiet: bool
    ignoreerrors: bool
    retries: int
    extractor_retries: int
    progress: bool
    check_formats: bool
    socket_timeout: int
    logger: object
    playlist_items: str


YDL_OPTS_LIST: YdlOpts = {
    "extract_flat": True,
    "quiet": False,
    "ignoreerrors": True,
    "retries": 2,
    "extractor_retries": 2,
    "socket_timeout": 20,
}

YDL_OPTS_DETAIL: YdlOpts = {
    "extract_flat": False,
    "quiet": False,
    "progress": True,  # Afficher une barre de progression
    "ignoreerrors": True,
    "retries": 3,
    "extractor_retries": 3,
    "check_formats": False,
    "socket_timeout": 20,
}

KNOWN_IDS_STOP_THRESHOLD = 7
RECENT_PLAYLIST_SCAN_STEP = 40
RECENT_PLAYLIST_SCAN_MAX = 400


def probe_latest_playlist_video_id(url: str) -> Optional[str]:
    """Récupère l'ID de la vidéo la plus récente avec une requête ultra-légère."""
    probe_opts = dict(YDL_OPTS_LIST)
    probe_opts["playlist_items"] = "1"

    try:
        infos = extract_playlist_with_hard_timeout(
            url,
            probe_opts,
            timeout_seconds=min(20, PLAYLIST_FETCH_TIMEOUT_SECONDS),
            max_total_seconds=min(60, PLAYLIST_FETCH_MAX_TOTAL_SECONDS),
        )
    except Exception:
        return None

    if not isinstance(infos, dict):
        return None

    entries = infos.get("entries")
    if isinstance(entries, list) and entries:
        latest_entry_id = extract_entry_video_id(entries[0])
        if isinstance(latest_entry_id, str) and latest_entry_id:
            return latest_entry_id

    return None


def extract_playlist_ids(entries):
    return [
        entry_id
        for e in entries
        for entry_id in [extract_entry_video_id(e)]
        if isinstance(entry_id, str) and entry_id
    ]


def scan_recent_entries_until_known_ids(
    url: str,
    existing_ids,
    adult_ids,
    known_ids_target=KNOWN_IDS_STOP_THRESHOLD,
):
    """Charge progressivement le haut de playlist jusqu'à retrouver N IDs connus consécutifs."""
    upper_bound = 0
    best_entries = []
    detected_total = None
    known_streak = 0

    while upper_bound < RECENT_PLAYLIST_SCAN_MAX:
        upper_bound = min(
            upper_bound + RECENT_PLAYLIST_SCAN_STEP, RECENT_PLAYLIST_SCAN_MAX
        )
        scan_opts = dict(YDL_OPTS_LIST)
        scan_opts["playlist_items"] = f"1:{upper_bound}"

        infos = extract_playlist_with_hard_timeout(
            url,
            scan_opts,
            timeout_seconds=min(20, PLAYLIST_FETCH_TIMEOUT_SECONDS),
            max_total_seconds=min(120, PLAYLIST_FETCH_MAX_TOTAL_SECONDS),
        )

        if not isinstance(infos, dict):
            return None, None, 0, upper_bound

        entries = (
            infos.get("entries", []) if isinstance(infos.get("entries"), list) else []
        )
        best_entries = entries

        playlist_count = infos.get("playlist_count")
        if isinstance(playlist_count, int):
            detected_total = playlist_count

        playlist_ids = list(dict.fromkeys(extract_playlist_ids(entries)))
        known_streak = 0
        for video_id in playlist_ids:
            if video_id in existing_ids or video_id in adult_ids:
                known_streak += 1
            else:
                known_streak = 0

            if known_streak >= known_ids_target:
                return best_entries, detected_total, known_streak, upper_bound

        if len(entries) < upper_bound:
            return best_entries, detected_total, known_streak, upper_bound

    return best_entries, detected_total, known_streak, upper_bound


def is_counted_ytdlp_error(exc):
    msg = str(exc).lower()
    is_403 = "403" in msg and ("http error" in msg or "forbidden" in msg)
    is_rate_limited = (
        "rate-limited" in msg
        or "rate limited" in msg
        or "current session has been rate-limited" in msg
        or "this content isn't available, try again later" in msg
    )
    return is_403 or is_rate_limited


def is_adult_restricted_error(exc):
    msg = str(exc).lower()
    return (
        "sign in to confirm your age" in msg
        or "sign in to confirm that you may be age-restricted" in msg
        or "this video may be inappropriate for some users" in msg
        or "the uploader has not made this video available in your country" in msg
        or "confirm your age" in msg
        or "age-restricted" in msg
        or "inappropriate for some users" in msg
        or "connectez-vous pour confirmer votre âge" in msg
        or "confirmer votre âge" in msg
        or "réservée à un public averti" in msg
    )


def is_skippable_unavailable_error(exc):
    msg = str(exc).lower()
    return (
        "private video" in msg
        or "this video is private" in msg
        or "video unavailable" in msg
        or "this video is unavailable" in msg
        or "has been removed" in msg
        or "members-only" in msg
        or "members only" in msg
    )


def extract_youtube_id(video_url):
    if not isinstance(video_url, str) or not video_url:
        return None

    # Cas fréquent: yt-dlp fournit directement l'ID vidéo.
    if (
        "://" not in video_url
        and "youtube.com" not in video_url
        and "youtu.be" not in video_url
    ):
        candidate = video_url.strip()
        if candidate:
            return candidate

    try:
        parsed = urlparse(video_url)
        if parsed.netloc.endswith("youtu.be"):
            return parsed.path.lstrip("/") or None
        if "youtube.com" in parsed.netloc:
            query_id = parse_qs(parsed.query).get("v")
            if query_id and query_id[0]:
                return query_id[0]
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) >= 2 and parts[0] in {"shorts", "watch", "live"}:
                return parts[1]
    except Exception:
        return None

    return None


def extract_entry_video_id(entry):
    """Retourne un ID vidéo robuste depuis une entrée playlist yt-dlp."""
    if not isinstance(entry, dict):
        return None

    current_id = entry.get("id")
    if isinstance(current_id, str) and current_id:
        return current_id

    for key in ("url", "webpage_url", "original_url"):
        extracted = extract_youtube_id(entry.get(key))
        if isinstance(extracted, str) and extracted:
            return extracted

    return None


def remember_adult_id(adult_ids, current_id, video_url=None):
    if isinstance(current_id, str) and current_id:
        adult_ids.add(current_id)
        return current_id

    extracted_id = extract_youtube_id(video_url)
    if isinstance(extracted_id, str) and extracted_id:
        adult_ids.add(extracted_id)
        return extracted_id

    return None


class CountedErrorTracker:
    """Compteur d'erreurs 403/rate-limit avec anti double-comptage immédiat."""

    def __init__(self, threshold):
        self.threshold = threshold
        self.count = 0
        self.total_count = 0
        self.stop_requested = False
        self._last_signature = None

    def increment(self, message, url=None, source="logger"):
        signature = (str(message).strip().lower(), str(url or ""), source)
        if signature == self._last_signature:
            return
        self._last_signature = signature

        self.count += 1
        self.total_count += 1
        print(
            f"{YELLOW}Erreur cumulée (403/rate-limit) {self.count}/{self.threshold} [{source}] {url or ''}{R}"
        )
        if self.count >= self.threshold:
            self.stop_requested = True

    def reset(self):
        """Remet le compteur de passe à zéro (total_count conservé)."""
        self.count = 0
        self.stop_requested = False
        self._last_signature = None

    def progress_suffix(self):
        return f"| {YELLOW}403/rate-limit : {self.count}/{self.threshold}{R}"


class YtDlpCountedErrorLogger:
    """Logger yt-dlp: relaie les logs et compte les erreurs ciblées."""

    def __init__(self, tracker):
        self.tracker = tracker
        self._adult_detected_ids = set()

    @staticmethod
    def _extract_video_id_from_log(text):
        match = re.search(r"\[youtube\]\s+([A-Za-z0-9_-]{6,})\s*:", text)
        if not match:
            return None
        return match.group(1)

    def is_adult_candidate(self, video_id):
        return isinstance(video_id, str) and video_id in self._adult_detected_ids

    def _handle(self, msg, level):
        text = str(msg)
        print(text)
        if is_adult_restricted_error(text):
            detected_id = self._extract_video_id_from_log(text)
            if detected_id:
                self._adult_detected_ids.add(detected_id)
        if is_counted_ytdlp_error(text):
            self.tracker.increment(text, source=f"log:{level}")

    def debug(self, msg):
        self._handle(msg, "debug")

    def info(self, msg):
        self._handle(msg, "info")

    def warning(self, msg):
        self._handle(msg, "warning")

    def error(self, msg):
        self._handle(msg, "error")


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


def extract_video_datetime(video):
    upload_date = video.get("upload_date")
    if upload_date:
        try:
            return datetime.strptime(upload_date, "%Y%m%d")
        except (ValueError, TypeError):
            pass

    for key in ("timestamp", "release_timestamp", "available_at"):
        ts = video.get(key)
        if ts:
            try:
                return datetime.fromtimestamp(ts)
            except (ValueError, OSError, TypeError):
                continue

    return None


def build_video_payload(v):
    date = extract_video_datetime(v)
    return {
        "id": v.get("id"),
        "titre": v.get("title"),
        "date": v.get("upload_date"),
        "date_fr": format_date(date),
        "duration": v.get("duration"),
        "duree": format_duration(v.get("duration")),
        "url": v.get("webpage_url"),
        "vues": v.get("view_count"),
        "likes": v.get("like_count"),
    }


def video_sort_key(video):
    """Clé de tri des vidéos par date de parution (plus récente d'abord)."""
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


def write_markdown(videos, total_playlist=None):
    if not isinstance(videos, list):
        return

    total_duration_seconds = sum(
        int(v.get("duration") or 0) for v in videos if isinstance(v, dict)
    )
    total_views = sum(int(v.get("vues") or 0) for v in videos if isinstance(v, dict))
    total_duration_txt = format_remaining_time_fr(total_duration_seconds // 60)
    total_views_txt = f"{total_views:,}".replace(",", " ")
    nb_videos_txt = f"**{len(videos)}** video{'s' if len(videos) > 1 else ''}"

    md = "# BP Learning - Vidéos à voir\n\n"
    partiel_txt1 = ""
    partiel_txt2 = ""
    if isinstance(total_playlist, int) and len(videos) < total_playlist:
        partiel_txt1 = f" ⚠️ PARTIEL → "
        partiel_txt2 = f"/ **{total_playlist}** "

    bilan = f"({partiel_txt1} {nb_videos_txt} {partiel_txt2}- {total_views_txt} vues - {total_duration_txt} )"
    md += f"## Auteur **[{AUTHOR}]({URL})** {bilan}\n\n"

    bilan = bilan.replace("*", "").strip()

    for video in videos:
        if not isinstance(video, dict):
            continue

        titre = video.get("titre") or "N/A"
        vues = video.get("vues") if isinstance(video.get("vues"), int) else 0
        duree = video.get("duree") or "N/A"
        date_fr = video.get("date_fr") or "N/A"
        url = video.get("url") or ""

        if not url:
            continue

        md += (
            "* [ ] [" + f"{date_fr} **{titre}** {vues} **{duree}**" + "](" + url + ")\n"
        )

    os.makedirs(STORAGE_DIR, exist_ok=True)
    with open(OUTPUT_MD_FILE, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"{GREEN}Fichier markdown généré : {OUTPUT_MD_FILE}{R}")

    return bilan


def build_scrap_summary_row(ida, author, videos):
    videos_count = len(videos) if isinstance(videos, list) else 0
    total_views = (
        sum(int(v.get("vues") or 0) for v in videos if isinstance(v, dict))
        if isinstance(videos, list)
        else 0
    )
    total_duration_seconds = (
        sum(int(v.get("duration") or 0) for v in videos if isinstance(v, dict))
        if isinstance(videos, list)
        else 0
    )
    total_duration_txt = format_remaining_time_fr(total_duration_seconds // 60)
    total_views_txt = f"{total_views:,}".replace(",", " ")

    return [ida, author, videos_count, total_views_txt, total_duration_txt]


def print_scrap_summary_table(rows):
    if not rows:
        return

    def bold(value):
        return f"{SB}{value}{R}"

    def parse_views(value):
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            try:
                return int(value.replace(" ", ""))
            except ValueError:
                return 0
        return 0

    def parse_duration_minutes(value):
        if not isinstance(value, str):
            return 0

        hours = 0
        minutes = 0

        hours_match = re.search(r"(\d+)\s+heure", value)
        if hours_match:
            hours = int(hours_match.group(1))

        minutes_match = re.search(r"(\d+)\s+minute", value)
        if minutes_match:
            minutes = int(minutes_match.group(1))

        return hours * 60 + minutes

    total_scraps = len(rows)
    videos_values = [int(row[2]) if isinstance(row[2], int) else 0 for row in rows]
    views_values = [parse_views(row[3]) for row in rows]
    duration_minutes_values = [parse_duration_minutes(row[4]) for row in rows]

    total_videos = sum(videos_values)
    total_views = sum(views_values)
    total_duration_minutes = sum(duration_minutes_values)

    display_rows = [
        [
            row[0],
            row[1],
            nf(row[2], 0) if isinstance(row[2], int) else row[2],
            row[3],
            row[4],
        ]
        for row in rows
    ]

    total_row = [
        bold(total_scraps),
        bold("TOTAL"),
        bold(nf(total_videos, 0)),
        bold(f"{total_views:,}".replace(",", " ")),
        bold(format_remaining_time_fr(total_duration_minutes)),
    ]

    table_rows = display_rows + [total_row]

    headers = [
        bold("id"),
        bold("AUTHOR"),
        bold("videos"),
        bold("vues"),
        bold("duree cumulee"),
    ]
    print(
        tabulate(
            table_rows,
            headers=headers,
            tablefmt="fancy_grid",
            colalign=("right", "left", "right", "right", "right"),
        )
    )


def write_result(
    videos, total_playlist, adult_ids=None, adult_count=None, cache_valid=True
):
    os.makedirs(STORAGE_DIR, exist_ok=True)
    now_ts = time.time()
    scraped = len(videos)
    normalized_adults = []
    if isinstance(adult_ids, (list, set, tuple)):
        normalized_adults = sorted(
            {
                video_id
                for video_id in adult_ids
                if isinstance(video_id, str) and video_id
            }
        )

    normalized_adult_count = (
        adult_count if isinstance(adult_count, int) else len(normalized_adults)
    )
    if normalized_adult_count < len(normalized_adults):
        normalized_adult_count = len(normalized_adults)
    if normalized_adult_count < 0:
        normalized_adult_count = 0

    if isinstance(total_playlist, int):
        # Garde une cohérence stricte: effective_total ne doit jamais être < scraped.
        max_adults_for_consistency = max(0, total_playlist - scraped)
        if normalized_adult_count > max_adults_for_consistency:
            normalized_adult_count = max_adults_for_consistency

    effective_total = (
        max(0, total_playlist - normalized_adult_count)
        if isinstance(total_playlist, int)
        else None
    )
    payload = {
        "url": URL,
        "timestamp": now_ts,
        "timestamp_fr": timestamp2fr(now_ts),
        "cache_valid": bool(cache_valid),
        "scraped": scraped,
        "total_playlist": total_playlist,
        "adult_count": normalized_adult_count,
        "videos": videos,
        "adults": normalized_adults,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return normalized_adult_count


def read_previous_state():
    if not os.path.isfile(OUTPUT_FILE):
        return []

    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        videos = data.get("videos") if isinstance(data.get("videos"), list) else []
        return videos
    except Exception:
        return []


def read_previous_counts():
    """Retourne les compteurs du dernier JSON pour savoir si le cache est complet."""
    if not os.path.isfile(OUTPUT_FILE):
        return None, None, 0

    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        videos = data.get("videos") if isinstance(data.get("videos"), list) else []
        scraped = data.get("scraped") if isinstance(data.get("scraped"), int) else None
        if not isinstance(scraped, int):
            scraped = len(videos)
        total_playlist = (
            data.get("total_playlist")
            if isinstance(data.get("total_playlist"), int)
            else None
        )

        adults = data.get("adults")
        adults_count = (
            len(
                [
                    video_id
                    for video_id in adults
                    if isinstance(video_id, str) and video_id
                ]
            )
            if isinstance(adults, list)
            else None
        )

        adult_count = data.get("adult_count")
        if not isinstance(adult_count, int):
            if adults_count is not None:
                adult_count = adults_count
            else:
                adult_videos = data.get("adult_videos")
                adult_count = len(adult_videos) if isinstance(adult_videos, list) else 0

        if adults_count is not None and adult_count < adults_count:
            adult_count = adults_count

        # Compat: anciens JSON sans total_playlist ou total incohérent (ex: 0 avec vidéos).
        if not isinstance(total_playlist, int) or total_playlist < (
            scraped + adult_count
        ):
            total_playlist = max(0, scraped + adult_count)

        return scraped, total_playlist, adult_count
    except Exception:
        return None, None, 0


def read_previous_adult_ids():
    if not os.path.isfile(OUTPUT_FILE):
        return set()

    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        adults = data.get("adults")
        if isinstance(adults, list):
            return {
                video_id
                for video_id in adults
                if isinstance(video_id, str) and video_id
            }

        adult_videos = data.get("adult_videos")
        if isinstance(adult_videos, list):
            return {
                video.get("id")
                for video in adult_videos
                if isinstance(video, dict)
                and isinstance(video.get("id"), str)
                and video.get("id")
            }
    except Exception:
        return set()

    return set()


def auto_heal_cache_invariants(cache_file):
    """Corrige uniquement les invariants certains du JSON cache."""
    if not os.path.isfile(cache_file):
        return []

    try:
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    if not isinstance(data, dict):
        return []

    changed_fields = []

    adults_raw = data.get("adults")
    normalized_adults = []
    if isinstance(adults_raw, list):
        normalized_adults = sorted(
            {
                video_id
                for video_id in adults_raw
                if isinstance(video_id, str) and video_id
            }
        )
    else:
        adult_videos = data.get("adult_videos")
        if isinstance(adult_videos, list):
            normalized_adults = sorted(
                {
                    video_id
                    for video in adult_videos
                    for video_id in [
                        video.get("id") if isinstance(video, dict) else None
                    ]
                    if isinstance(video, dict)
                    and isinstance(video_id, str)
                    and video_id
                }
            )

    if data.get("adults") != normalized_adults:
        data["adults"] = normalized_adults
        changed_fields.append("adults")

    videos = data.get("videos")
    if isinstance(videos, list):
        expected_scraped = len(videos)
        if data.get("scraped") != expected_scraped:
            data["scraped"] = expected_scraped
            changed_fields.append("scraped")

    adult_count = data.get("adult_count")
    if not isinstance(adult_count, int) or adult_count < 0:
        data["adult_count"] = len(normalized_adults)
        adult_count = len(normalized_adults)
        changed_fields.append("adult_count")
    elif adult_count < len(normalized_adults):
        data["adult_count"] = len(normalized_adults)
        adult_count = len(normalized_adults)
        changed_fields.append("adult_count")

    total_playlist = data.get("total_playlist")
    if isinstance(total_playlist, int):
        scraped_value = data.get("scraped")
        if isinstance(scraped_value, int):
            max_adults_for_consistency = max(0, total_playlist - scraped_value)
            if adult_count > max_adults_for_consistency:
                data["adult_count"] = max_adults_for_consistency
                adult_count = max_adults_for_consistency
                changed_fields.append("adult_count")

    expected_timestamp = timestamp_fr_to_epoch(data.get("timestamp_fr"))
    current_timestamp = data.get("timestamp")
    if expected_timestamp is not None:
        if not isinstance(current_timestamp, (int, float)) or (
            abs(float(current_timestamp) - expected_timestamp) > 2
        ):
            data["timestamp"] = float(expected_timestamp)
            changed_fields.append("timestamp")

    if "complete" in data:
        data.pop("complete", None)
        changed_fields.append("complete")

    if "adult_videos" in data:
        data.pop("adult_videos", None)
        changed_fields.append("adult_videos")

    if "effective_total" in data:
        data.pop("effective_total", None)
        changed_fields.append("effective_total")

    # Garantit les métadonnées minimales pour la reprise et l'affichage.
    if data.get("url") != URL:
        data["url"] = URL
        changed_fields.append("url")

    current_timestamp = data.get("timestamp")
    current_timestamp_fr = data.get("timestamp_fr")
    if not isinstance(current_timestamp, (int, float)):
        # Si timestamp_fr est fiable, on l'utilise; sinon, on prend maintenant.
        inferred_ts = timestamp_fr_to_epoch(current_timestamp_fr)
        data["timestamp"] = float(
            inferred_ts if inferred_ts is not None else time.time()
        )
        changed_fields.append("timestamp")

    if not isinstance(data.get("timestamp_fr"), str):
        ts_for_format = data.get("timestamp")
        if isinstance(ts_for_format, (int, float)):
            data["timestamp_fr"] = timestamp2fr(float(ts_for_format))
            changed_fields.append("timestamp_fr")

    total_playlist = data.get("total_playlist")
    if not isinstance(total_playlist, int):
        raw_scraped = data.get("scraped")
        raw_adult = data.get("adult_count")
        scraped_value = raw_scraped if isinstance(raw_scraped, int) else 0
        adult_value = raw_adult if isinstance(raw_adult, int) else 0
        data["total_playlist"] = max(0, scraped_value + adult_value)
        changed_fields.append("total_playlist")
    else:
        raw_scraped = data.get("scraped")
        raw_adult = data.get("adult_count")
        scraped_value = raw_scraped if isinstance(raw_scraped, int) else 0
        adult_value = raw_adult if isinstance(raw_adult, int) else 0
        min_total = max(0, scraped_value + adult_value)
        if total_playlist < min_total:
            data["total_playlist"] = min_total
            changed_fields.append("total_playlist")

    if not changed_fields:
        return []

    # Evite les doublons si un même champ est corrigé plusieurs fois.
    changed_fields = list(dict.fromkeys(changed_fields))

    # Conserve adults en fin de fichier JSON pour la lisibilité souhaitée.
    if "adults" in data:
        adults_value = data.pop("adults")
        data["adults"] = adults_value

    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        return []

    return changed_fields


def bootstrap_missing_cache_from_legacy():
    """Restaure OUTPUT_FILE depuis un cache JSON legacy compatible si disponible."""
    if os.path.isfile(OUTPUT_FILE) or not os.path.isdir(STORAGE_DIR):
        return None

    candidates = []
    for name in os.listdir(STORAGE_DIR):
        if not name.lower().endswith(".json"):
            continue
        if name == os.path.basename(OUTPUT_FILE):
            continue
        if AUTHOR.lower() not in name.lower():
            continue
        path = os.path.join(STORAGE_DIR, name)
        if os.path.isfile(path):
            candidates.append(path)

    if not candidates:
        return None

    # Prend le plus récent parmi les JSON de la chaîne ciblée.
    candidates.sort(key=os.path.getmtime, reverse=True)

    for candidate in candidates:
        try:
            with open(candidate, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                continue

            videos = data.get("videos")
            if not isinstance(videos, list):
                continue

            os.makedirs(STORAGE_DIR, exist_ok=True)
            shutil.copyfile(candidate, OUTPUT_FILE)
            return candidate
        except Exception:
            continue

    return None


def extract_playlist_with_hard_timeout(
    url, ydl_opts, timeout_seconds, max_total_seconds=None
):
    """Exécute yt-dlp avec timeout d'inactivité + garde-fou global."""
    result_holder = {}
    error_holder = {}

    # Le timeout court doit déclencher seulement si plus aucun log n'arrive.
    last_activity = time.time()

    class PlaylistActivityLogger:
        def __init__(self, base_logger=None):
            self.base_logger = base_logger

        def _touch(self):
            nonlocal last_activity
            last_activity = time.time()

        def debug(self, msg):
            self._touch()
            if self.base_logger and hasattr(self.base_logger, "debug"):
                self.base_logger.debug(msg)
            else:
                print(msg)

        def info(self, msg):
            self._touch()
            if self.base_logger and hasattr(self.base_logger, "info"):
                self.base_logger.info(msg)
            else:
                print(msg)

        def warning(self, msg):
            self._touch()
            if self.base_logger and hasattr(self.base_logger, "warning"):
                self.base_logger.warning(msg)
            else:
                print(msg)

        def error(self, msg):
            self._touch()
            if self.base_logger and hasattr(self.base_logger, "error"):
                self.base_logger.error(msg)
            else:
                print(msg)

    ydl_opts_list = dict(ydl_opts)
    ydl_opts_list["logger"] = PlaylistActivityLogger(ydl_opts_list.get("logger"))

    effective_max_total = (
        max_total_seconds
        if isinstance(max_total_seconds, int) and max_total_seconds > 0
        else max(timeout_seconds * 20, timeout_seconds + 60)
    )

    def _worker():
        try:
            with yt_dlp.YoutubeDL(cast("_Params", ydl_opts_list)) as ydl_list:
                result_holder["data"] = ydl_list.extract_info(url, download=False)
        except Exception as exc:
            error_holder["exc"] = exc

    thread = threading.Thread(target=_worker, daemon=True)
    thread.start()

    start_time = time.time()
    elapsed_width = max(2, len(str(effective_max_total)))
    next_heartbeat = 5
    while thread.is_alive():
        elapsed = int(time.time() - start_time)
        idle_for = int(time.time() - last_activity)

        if idle_for >= timeout_seconds:
            raise TimeoutError(
                f"Timeout playlist après {timeout_seconds}s sans activité réseau détectée (logs yt-dlp inactifs)."
            )

        if elapsed >= effective_max_total:
            raise TimeoutError(
                f"Timeout playlist global après {effective_max_total}s (garde-fou)."
            )

        # N'affiche l'attente que s'il y a une vraie inactivité.
        if elapsed >= next_heartbeat and idle_for >= 5:
            print(
                f"{CYAN}... Attente de la réponse YouTube ( {elapsed:>{elapsed_width}}s écoulées / {effective_max_total}s max, activité il y a {idle_for}s ) ...{R}",
                flush=True,
            )
            next_heartbeat += 5
        elif elapsed >= next_heartbeat:
            next_heartbeat += 5

        thread.join(1)

    if "exc" in error_holder:
        raise error_holder["exc"]

    return result_holder.get("data")


def try_return_valid_ttl_cache(ida):
    """Retourne un résumé immédiat si le cache TTL est valide et complet."""
    cache_entry = get_valid_cache_entry(OUTPUT_FILE, CACHE_TTL)
    if cache_entry is None:
        return None

    cached_videos = cache_entry.get("videos")
    cache_date = cache_entry.get("timestamp_fr")
    remaining_minutes = cache_entry.get("remaining_minutes")
    scraped, total_playlist, adult_count = read_previous_counts()
    effective_total = (
        max(0, total_playlist - adult_count)
        if isinstance(total_playlist, int)
        else None
    )
    cache_is_complete = (
        isinstance(scraped, int)
        and isinstance(effective_total, int)
        and (
            (effective_total == 0 and scraped == 0)
            or (effective_total > 0 and scraped >= effective_total)
        )
    )

    if (
        isinstance(scraped, int)
        and isinstance(total_playlist, int)
        and not cache_is_complete
    ):
        print(
            f"Cache valide mais incomplet ({scraped}/{effective_total}) : reprise du scraping pour combler les trous."
        )

    if not isinstance(cached_videos, list):
        return None

    cached_videos = sorted(cached_videos, key=video_sort_key, reverse=True)
    if not cache_is_complete:
        return None

    ttl_minutes = max(1, (CACHE_TTL + 59) // 60)
    ttl_txt = format_remaining_time_fr(ttl_minutes)
    print(f"Données chargées depuis le cache JSON (valide {ttl_txt}).")
    if cache_date and isinstance(remaining_minutes, int):
        remaining_txt = format_remaining_time_fr(remaining_minutes)
        print(
            f"Dernière mise à jour: {cache_date} (prochaine actualisation dans environ {CYAN}{remaining_txt}{R})."
        )
    if os.path.isfile(OUTPUT_MD_FILE):
        print("Markdown non regénéré (cache TTL valide).")
    else:
        write_markdown(cached_videos, total_playlist=effective_total)
        print(f"{YELLOW}Markdown régénéré car fichier absent (cache TTL valide).{R}")

    return build_scrap_summary_row(ida, AUTHOR, cached_videos)


def decide_post_ttl_strategy(
    ida,
    videos,
    adult_ids,
    total_playlist,
    persisted_adult_count,
):
    """Décide la stratégie post-TTL: retour immédiat, incrémental, ou complet."""
    initial_video_count = len(videos)
    previous_total_playlist = total_playlist
    latest_cached_video_id = (
        videos[0].get("id")
        if videos
        and isinstance(videos[0], dict)
        and isinstance(videos[0].get("id"), str)
        and videos[0].get("id")
        else None
    )
    previous_effective_total = (
        max(0, total_playlist - persisted_adult_count)
        if isinstance(total_playlist, int)
        else None
    )
    previous_cache_is_complete = isinstance(previous_effective_total, int) and (
        (previous_effective_total == 0 and initial_video_count == 0)
        or (
            previous_effective_total > 0
            and initial_video_count >= previous_effective_total
        )
    )

    use_recent_incremental_scan = False
    if previous_cache_is_complete:
        print(
            f"{CYAN}Cache TTL expiré: vérification ultra-légère du dernier ID publié...{R}"
        )
        probed_latest_video_id = probe_latest_playlist_video_id(URL)
        if (
            isinstance(probed_latest_video_id, str)
            and isinstance(latest_cached_video_id, str)
            and probed_latest_video_id == latest_cached_video_id
        ):
            print(
                f"{GREEN}Dernier ID inchangé ({probed_latest_video_id}) : cache conservé, scraping détaillé ignoré.{R}"
            )
            sorted_videos = sorted(videos, key=video_sort_key, reverse=True)
            current_adult_count = write_result(
                videos=sorted_videos,
                total_playlist=total_playlist,
                adult_ids=adult_ids,
                adult_count=max(persisted_adult_count, len(adult_ids)),
                cache_valid=True,
            )
            if not isinstance(current_adult_count, int):
                current_adult_count = max(persisted_adult_count, len(adult_ids))

            if os.path.isfile(OUTPUT_MD_FILE):
                print(
                    "Markdown non regénéré (cache prolongé après vérification du total)."
                )
            else:
                write_markdown(sorted_videos, total_playlist=previous_effective_total)
                print(
                    f"{YELLOW}Markdown régénéré car fichier absent (cache prolongé).{R}"
                )
            return {
                "early_summary": build_scrap_summary_row(ida, AUTHOR, sorted_videos),
                "use_recent_incremental_scan": False,
                "previous_total_playlist": previous_total_playlist,
            }

        if isinstance(probed_latest_video_id, str) and isinstance(
            latest_cached_video_id, str
        ):
            print(
                f"{YELLOW}Dernier ID changé ({latest_cached_video_id} -> {probed_latest_video_id}) : scraping détaillé nécessaire.{R}"
            )
            use_recent_incremental_scan = True
        else:
            print(f"{YELLOW}Probe ID non concluant: poursuite du scraping détaillé.{R}")

    return {
        "early_summary": None,
        "use_recent_incremental_scan": use_recent_incremental_scan,
        "previous_total_playlist": previous_total_playlist,
    }


def fetch_playlist_batch(
    use_recent_incremental_scan,
    has_fetched_playlist_this_run,
    existing_ids,
    adult_ids,
):
    """Récupère les entrées playlist selon la stratégie active (incrémental/complet)."""
    started_at = time.time()
    if use_recent_incremental_scan and not has_fetched_playlist_this_run:
        print(
            f"{CYAN}Connexion à YouTube (mode incrémental): scan des entrées récentes jusqu'à {KNOWN_IDS_STOP_THRESHOLD} IDs déjà connus...{R}",
            flush=False,
        )
        (
            recent_entries,
            recent_total_videos,
            known_streak,
            scanned_limit,
        ) = scan_recent_entries_until_known_ids(
            URL,
            existing_ids,
            adult_ids,
            known_ids_target=KNOWN_IDS_STOP_THRESHOLD,
        )
        has_fetched_playlist_this_run = True

        if (
            isinstance(recent_entries, list)
            and known_streak >= KNOWN_IDS_STOP_THRESHOLD
        ):
            entries = recent_entries
            total_videos = recent_total_videos
            print(
                f"{CYAN}Mode incrémental validé: {known_streak} IDs connus consécutifs retrouvés dans les {len(entries)} premières entrées (borne {scanned_limit}).{R}"
            )
        else:
            print(
                f"{YELLOW}Mode incrémental insuffisant ({known_streak}/{KNOWN_IDS_STOP_THRESHOLD} IDs connus consécutifs, borne {scanned_limit}) : bascule en scan complet.{R}"
            )
            use_recent_incremental_scan = False
            print(
                f"{CYAN}Connexion à YouTube pour récupérer la playlist complète ({AUTHOR})...{R}",
                flush=False,
            )
            playlist_infos = extract_playlist_with_hard_timeout(
                URL,
                YDL_OPTS_LIST,
                PLAYLIST_FETCH_TIMEOUT_SECONDS,
                PLAYLIST_FETCH_MAX_TOTAL_SECONDS,
            )
            if isinstance(playlist_infos, dict):
                entries = playlist_infos.get("entries", [])
                total_videos = playlist_infos.get("playlist_count")
            else:
                entries = []
                total_videos = None
    else:
        print(
            f"{CYAN}Connexion à YouTube pour récupérer la playlist ({AUTHOR})...{R}",
            flush=False,
        )
        playlist_infos = extract_playlist_with_hard_timeout(
            URL,
            YDL_OPTS_LIST,
            PLAYLIST_FETCH_TIMEOUT_SECONDS,
            PLAYLIST_FETCH_MAX_TOTAL_SECONDS,
        )
        has_fetched_playlist_this_run = True
        if isinstance(playlist_infos, dict):
            entries = playlist_infos.get("entries", [])
            total_videos = playlist_infos.get("playlist_count")
        else:
            entries = []
            total_videos = None

    elapsed = round(time.time() - started_at, 1)
    print(
        f"{CYAN}Playlist récupérée en {elapsed}s.{R}",
        flush=True,
    )
    return (
        entries,
        total_videos,
        has_fetched_playlist_this_run,
        use_recent_incremental_scan,
    )


def resolve_total_playlist_from_batch(total_videos, entries, previous_total_playlist):
    """Calcule total_playlist à partir du batch courant avec garde-fou de baisse."""
    detected_total_playlist = total_videos if isinstance(total_videos, int) else None
    if (
        isinstance(detected_total_playlist, int)
        and detected_total_playlist <= 0
        and isinstance(entries, list)
        and len(entries) > 0
    ):
        detected_total_playlist = len(entries)

    if isinstance(detected_total_playlist, int):
        total_playlist = detected_total_playlist
        if (
            isinstance(previous_total_playlist, int)
            and previous_total_playlist > 0
            and detected_total_playlist < previous_total_playlist
        ):
            entries_count = len(entries) if isinstance(entries, list) else 0
            detected_matches_entries = (
                entries_count > 0 and detected_total_playlist == entries_count
            )
            drop_ratio = (
                previous_total_playlist - detected_total_playlist
            ) / previous_total_playlist
            if (
                drop_ratio > TOTAL_PLAYLIST_DROP_GUARD_RATIO
                and not detected_matches_entries
            ):
                print(
                    f"{YELLOW}Protection total_playlist: nouveau total détecté {detected_total_playlist} inférieur de {drop_ratio * 100:.2f}% à l'ancien {previous_total_playlist}. Ancienne valeur conservée dans le JSON.{R}"
                )
                total_playlist = previous_total_playlist
        return total_playlist

    return previous_total_playlist if isinstance(previous_total_playlist, int) else None


def remove_stale_adult_ids(adult_ids, playlist_ids):
    """Retire les IDs adults absents de la playlist courante."""
    if not adult_ids:
        return

    playlist_id_set = set(playlist_ids)
    stale_adults = {
        video_id for video_id in adult_ids if video_id not in playlist_id_set
    }
    if stale_adults:
        adult_ids.difference_update(stale_adults)
        print(
            f"{YELLOW}{len(stale_adults)} ID(s) adults obsolètes retirés (absents de la playlist courante).{R}"
        )


def handle_no_missing_ids_case(
    effective_total,
    videos,
    total_playlist,
    playlist_ids,
    current_adult_count,
    persisted_adult_count,
):
    """Gère le cas sans IDs manquants et retourne (break_loop, persisted_adult_count)."""
    if isinstance(effective_total, int) and len(videos) < effective_total:
        hidden_count_from_playlist = 0
        if isinstance(total_playlist, int) and total_playlist > 0:
            hidden_count_from_playlist = max(0, total_playlist - len(playlist_ids))

        if (
            hidden_count_from_playlist > 0
            and hidden_count_from_playlist > current_adult_count
        ):
            persisted_adult_count = hidden_count_from_playlist
            print(
                f"{YELLOW}Aucun ID manquant détecté mais {hidden_count_from_playlist} vidéo(s) sont comptées par YouTube sans ID exploitable: adult_count ajusté à {persisted_adult_count}.{R}"
            )
        print(
            f"{YELLOW}Aucun trou détecté sur les IDs remontés par yt-dlp, mais cache encore incomplet ({len(videos)}/{effective_total}). État conservé en partiel.{R}"
        )
    else:
        print("Aucun trou détecté dans le cache pour les IDs connus de la playlist.")

    return True, persisted_adult_count


def process_missing_entries_detailed(
    entries,
    missing_in_cache,
    existing_ids,
    adult_ids,
    videos,
    error_tracker,
    on_threshold_pause,
    handle_exception,
):
    """Traite le détail des vidéos manquantes et met à jour les structures en place."""
    ydl_opts_detail = dict(YDL_OPTS_DETAIL)
    detail_logger = YtDlpCountedErrorLogger(error_tracker)
    ydl_opts_detail["logger"] = detail_logger

    total_entries = len(entries)
    run_processed = 0

    with yt_dlp.YoutubeDL(cast("_Params", ydl_opts_detail)) as ydl_detail:
        missing_count = max(1, len(missing_in_cache))
        for idx, entry in enumerate(entries, start=1):
            if error_tracker.stop_requested:
                on_threshold_pause()
                break

            if not isinstance(entry, dict):
                continue

            current_id = extract_entry_video_id(entry)

            # On saute immédiatement les vidéos déjà présentes dans le cache.
            if isinstance(current_id, str) and current_id in existing_ids:
                continue
            if isinstance(current_id, str) and current_id in adult_ids:
                continue

            video_url = entry.get("url") or entry.get("webpage_url")
            if not video_url and isinstance(current_id, str) and current_id:
                video_url = f"https://www.youtube.com/watch?v={current_id}"
            if not video_url:
                continue

            print(
                f"{CYAN}[progress] Vidéo globale {SB}{idx} / {total_entries} - {round(100*idx/total_entries,1)} %{R} {CYAN}| Exécutées : {SB}{run_processed} ( {(run_processed) / missing_count * 100:.1f} % ) {R}{error_tracker.progress_suffix()} | {SB}{AUTHOR}{R}"
            )

            try:
                video_detail = ydl_detail.extract_info(video_url, download=False)
            except DownloadError as e:
                if is_adult_restricted_error(e) or is_skippable_unavailable_error(e):
                    if is_adult_restricted_error(e):
                        skipped_video_id = remember_adult_id(
                            adult_ids, current_id, video_url
                        )
                        if skipped_video_id:
                            print(
                                f"{YELLOW}Vidéo exclue du total (adult): {skipped_video_id}{R}"
                            )
                    else:
                        skipped_video_id = (
                            current_id
                            if isinstance(current_id, str) and current_id
                            else extract_youtube_id(video_url)
                        )
                        if skipped_video_id:
                            remember_adult_id(adult_ids, skipped_video_id, video_url)
                            print(
                                f"{YELLOW}Vidéo exclue du total (indisponible): {skipped_video_id}{R}"
                            )
                    continue
                if handle_exception(e, video_url, "Erreur yt-dlp ignorée sur"):
                    break
                continue
            except Exception as e:
                if handle_exception(e, video_url, "Erreur lors du détail pour"):
                    break
                continue

            if error_tracker.stop_requested:
                on_threshold_pause()
                break

            if not isinstance(video_detail, dict):
                candidate_id = (
                    current_id
                    if isinstance(current_id, str) and current_id
                    else extract_youtube_id(video_url)
                )
                if candidate_id:
                    remember_adult_id(adult_ids, candidate_id, video_url)
                    if detail_logger.is_adult_candidate(candidate_id):
                        print(
                            f"{YELLOW}Vidéo exclue du total (adult via logs): {candidate_id}{R}"
                        )
                    else:
                        print(
                            f"{YELLOW}Vidéo exclue du total (non exploitable): {candidate_id}{R}"
                        )
                else:
                    print(
                        f"{YELLOW}Vidéo non exploitable sans ID détectable: {video_url}{R}"
                    )
                continue

            video = build_video_payload(video_detail)
            video_id = video.get("id")
            if video_id in existing_ids:
                continue
            videos.append(video)
            if video_id:
                existing_ids.add(video_id)
                if video_id in adult_ids:
                    adult_ids.discard(video_id)
                    print(
                        f"{GREEN}ID retiré de adults après revalidation réussie: {video_id}{R}"
                    )
            run_processed += 1

    return run_processed


def scrap_some(ida):
    ini(ida)
    print(f"SCRAP des vidéos de {SB}{AUTHOR}{R}\n→ {URL}")

    restored_from = bootstrap_missing_cache_from_legacy()
    if isinstance(restored_from, str):
        print(
            f"{CYAN}Cache principal absent: restauration depuis {os.path.basename(restored_from)}.{R}"
        )

    healed_fields = auto_heal_cache_invariants(OUTPUT_FILE)
    if healed_fields:
        print(
            f"{YELLOW}Auto-heal cache appliqué (invariants): {', '.join(healed_fields)}{R}"
        )

    ttl_summary = try_return_valid_ttl_cache(ida)
    if ttl_summary is not None:
        return ttl_summary

    videos = read_previous_state()
    initial_video_count = len(videos)
    existing_ids = {
        v.get("id")
        for v in videos
        if isinstance(v, dict) and isinstance(v.get("id"), str) and v.get("id")
    }
    adult_ids = read_previous_adult_ids()
    _, total_playlist, persisted_adult_count = (
        read_previous_counts()
    )  # récupère total connu pour la vérification de complétude
    persisted_adult_count = (
        persisted_adult_count if isinstance(persisted_adult_count, int) else 0
    )
    post_ttl_strategy = decide_post_ttl_strategy(
        ida=ida,
        videos=videos,
        adult_ids=adult_ids,
        total_playlist=total_playlist,
        persisted_adult_count=persisted_adult_count,
    )
    if post_ttl_strategy["early_summary"] is not None:
        return post_ttl_strategy["early_summary"]
    use_recent_incremental_scan = post_ttl_strategy["use_recent_incremental_scan"]
    previous_total_playlist = post_ttl_strategy["previous_total_playlist"]

    error_tracker = CountedErrorTracker(MAX_CUMULATED_403_ERRORS)

    if videos:
        print(
            f"État précédent détecté. {CYAN}Vérification complète des IDs pour combler les trous{R}."
        )
    else:
        print("Aucun état précédent trouvé, démarrage depuis la première vidéo.")

    stall_retries = 0
    scraped_before_pass = len(videos)
    has_fetched_playlist_this_run = False

    def log_threshold_pause_message():
        print(
            f"{RED}Seuil d'erreurs 403/rate-limit atteint ({MAX_CUMULATED_403_ERRORS}). Pause {PAUSE_ON_RATE_LIMIT}s puis reprise...{R}"
        )

    def handle_detail_exception(exc, video_url, fallback_prefix):
        if is_adult_restricted_error(exc):
            return False

        if is_counted_ytdlp_error(exc):
            error_tracker.increment(str(exc), url=video_url, source="exception")
            if error_tracker.stop_requested:
                log_threshold_pause_message()
                return True
            return False

        print(f"{fallback_prefix} {video_url}: {exc}")
        return False

    while True:
        # ── Vérification complétude avant chaque passe ──────────────────────
        current_adult_count = max(persisted_adult_count, len(adult_ids))
        effective_total = (
            max(0, total_playlist - current_adult_count)
            if isinstance(total_playlist, int)
            else None
        )
        if (
            has_fetched_playlist_this_run
            and isinstance(effective_total, int)
            and effective_total > 0
            and len(videos) >= effective_total
        ):
            break

        if (
            isinstance(effective_total, int)
            and effective_total > 0
            and len(videos) >= effective_total
        ):
            print(
                f"{CYAN}Cache local marqué complet ({len(videos)}/{effective_total}) : vérification YouTube en cours pour détecter d'éventuelles nouveautés...{R}"
            )

        try:
            (
                entries,
                total_videos,
                has_fetched_playlist_this_run,
                use_recent_incremental_scan,
            ) = fetch_playlist_batch(
                use_recent_incremental_scan=use_recent_incremental_scan,
                has_fetched_playlist_this_run=has_fetched_playlist_this_run,
                existing_ids=existing_ids,
                adult_ids=adult_ids,
            )

            total_playlist = resolve_total_playlist_from_batch(
                total_videos=total_videos,
                entries=entries,
                previous_total_playlist=previous_total_playlist,
            )

            total_videos_txt = (
                str(total_videos)
                if isinstance(total_videos, int)
                else f"Nombre inconnu (au moins {len(entries)}) de"
            )
            print(f"{RED}{total_videos_txt} vidéo(s){R} trouvée(s) dans la playlist.")
            total_entries = len(entries)
            run_processed = 0
            playlist_ids = extract_playlist_ids(entries)
            # Déduplication stable: évite de retraiter deux fois le même ID.
            playlist_ids = list(dict.fromkeys(playlist_ids))
            remove_stale_adult_ids(adult_ids=adult_ids, playlist_ids=playlist_ids)
            missing_in_cache = [
                video_id
                for video_id in playlist_ids
                if video_id not in existing_ids and video_id not in adult_ids
            ]

            if missing_in_cache:
                print(
                    f"{YELLOW}{len(missing_in_cache)} vidéo(s) absente(s) du cache seront (re)téléchargées.{R}"
                )
            else:
                _, persisted_adult_count = handle_no_missing_ids_case(
                    effective_total=effective_total,
                    videos=videos,
                    total_playlist=total_playlist,
                    playlist_ids=playlist_ids,
                    current_adult_count=current_adult_count,
                    persisted_adult_count=persisted_adult_count,
                )
                break

            process_missing_entries_detailed(
                entries=entries,
                missing_in_cache=missing_in_cache,
                existing_ids=existing_ids,
                adult_ids=adult_ids,
                videos=videos,
                error_tracker=error_tracker,
                on_threshold_pause=log_threshold_pause_message,
                handle_exception=handle_detail_exception,
            )

        except Exception as e:
            print(f"{RED}Scrap interrompu: {e}{R}", flush=True)
            print(
                f"{YELLOW}Conseil: vérifier la connexion/rate-limit YouTube, puis relancer. Timeout réseau: {YDL_OPTS_LIST.get('socket_timeout')}s/requête, timeout global playlist: {PLAYLIST_FETCH_TIMEOUT_SECONDS}s.{R}",
                flush=True,
            )

        # ── Fin de passe: décider si on continue, on pause, ou on abandonne ──
        scraped_now = len(videos)

        if not error_tracker.stop_requested:
            # Passe terminée normalement sans atteindre le seuil: on sort.
            break

        # Détection de stall: pas de progression sur cette passe
        if scraped_now <= scraped_before_pass:
            stall_retries += 1
            print(
                f"{RED}Aucune progression détectée (passe #{stall_retries}/{MAX_STALL_RETRIES}).{R}"
            )
            if stall_retries >= MAX_STALL_RETRIES:
                print(
                    f"{RED}Abandon définitif après {MAX_STALL_RETRIES} passes sans progression.{R}"
                )
                break
        else:
            stall_retries = 0

        scraped_before_pass = scraped_now
        error_tracker.reset()
        # Sauvegarde de la progression avant la pause (persistance entre passes)
        persisted_adult_count = write_result(
            videos=sorted(videos, key=video_sort_key, reverse=True),
            total_playlist=total_playlist,
            adult_ids=adult_ids,
            adult_count=max(persisted_adult_count, len(adult_ids)),
            cache_valid=has_fetched_playlist_this_run,
        )
        bilan = write_markdown(
            sorted(videos, key=video_sort_key, reverse=True),
            total_playlist=(
                max(0, total_playlist - max(persisted_adult_count, len(adult_ids)))
                if isinstance(total_playlist, int)
                else None
            ),
        )
        print(f"{GREEN}JSON intermédiaire écrit ({scraped_now} vidéos).{R}")
        print(
            f"{YELLOW}Pause {PAUSE_ON_RATE_LIMIT}s avant reprise (scraped={scraped_now}, total={total_playlist})...{R}"
        )
        # exit() # Pour tests sans attendre et redémarrer auto
        time.sleep(PAUSE_ON_RATE_LIMIT)

    videos = sorted(videos, key=video_sort_key, reverse=True)
    scraped = len(videos)
    current_adult_count = max(persisted_adult_count, len(adult_ids))
    bilan = "unused"

    current_adult_count = write_result(
        videos=videos,
        total_playlist=total_playlist,
        adult_ids=adult_ids,
        adult_count=current_adult_count,
        cache_valid=has_fetched_playlist_this_run,
    )
    if not isinstance(current_adult_count, int):
        current_adult_count = max(persisted_adult_count, len(adult_ids))
    markdown_missing = not os.path.isfile(OUTPUT_MD_FILE)
    if len(videos) != initial_video_count or markdown_missing:
        bilan = write_markdown(
            videos,
            total_playlist=(
                max(0, total_playlist - current_adult_count)
                if isinstance(total_playlist, int)
                else None
            ),
        )
        if markdown_missing and len(videos) == initial_video_count:
            print(f"{YELLOW}Markdown régénéré car fichier absent.{R}")
    else:
        bilan = "Markdown non regénéré (aucun changement détecté)"
        print("Markdown non regénéré (aucun changement détecté).")
    effective_total = (
        max(0, total_playlist - current_adult_count)
        if isinstance(total_playlist, int)
        else None
    )
    status = (
        "complete"
        if isinstance(effective_total, int)
        and effective_total > 0
        and scraped >= effective_total
        else "partial"
    )
    print(f"{GREEN}Fichier JSON écrit: {OUTPUT_FILE}{R}")
    print(
        f"scraped={scraped}, total_playlist={total_playlist}, adult={current_adult_count}, effective_total={effective_total}, status={status}"
    )
    print(
        f"Erreurs cumulées (403/rate-limit) total toutes passes: {error_tracker.total_count}"
    )
    # bilan='oki'
    print(f"Fin du scrap des vidéos de {SB}{AUTHOR}{R}\n{bilan}.")
    return build_scrap_summary_row(ida, AUTHOR, videos)


if __name__ == "__main__":

    cls()

    # Scrap partiel - Indices des comptes à scraper
    nb = auth.nb_authors()
    res = []
    selected_yt_users_ids = [0, 1, 2, 6, 10, 11, 12, 16]
    selected_yt_users_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    selected_yt_users_ids = [17]
    selected_yt_users_ids = list(range(nb)) # All
    selected_yt_users_ids.remove(3)
    selected_yt_users_ids.remove(4)
    selected_yt_users_ids.remove(9)

    if (1) :
        for i in selected_yt_users_ids:
            end()
            print(
                f"{SB}{i:> 3}{R} {SB}{selected_yt_users_ids.index(i)+1:> 3}{R} / {nb:> 3} → {SB}{auth.AUTHORS[i]}{R}"
            )
            res.append(scrap_some(i))
        end()
        print_scrap_summary_table(res)

    # print (list(selected_yt_users_ids))

    # Scrap total
    # nb = len(auth.AUTHORS)
    # for i in range(nb):
    #     end()
    #     print(
    #         f"{SB}{i:> 3}{R} / {nb:> 3} → {SB}{auth.AUTHORS[i]}{R}"
    #     )
    #     res.append(scrap_some(i))
    # end()
    # print_scrap_summary_table(res)

    # Scrap unique
    # scrap_some(8)
    end()
