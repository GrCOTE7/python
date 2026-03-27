import json, os, shutil, time
from typing import Any, Optional, TypedDict


class ValidCacheEntry(TypedDict):
    videos: list[Any]
    timestamp: float
    timestamp_fr: Optional[str]
    remaining_minutes: int


def read_cache_payload(cache_file: str) -> Optional[dict[str, Any]]:
    """Lit le JSON du cache et retourne son contenu brut."""
    if not os.path.isfile(cache_file):
        return None

    try:
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def extract_cache_videos(data: dict[str, Any]) -> Any:
    """Normalise la structure des videos selon les formats de cache rencontres."""
    videos = data.get("videos") or data.get("version")

    # Compat: ancien bug de serialisation -> [[...], true]
    if (
        isinstance(videos, list)
        and len(videos) == 2
        and isinstance(videos[1], bool)
        and isinstance(videos[0], list)
    ):
        videos = videos[0]

    return videos


def get_valid_cache_entry(cache_file: str, cache_ttl: int) -> Optional[ValidCacheEntry]:
    """Retourne une entree cache valide (non expiree) avec metadonnees utiles."""
    data = read_cache_payload(cache_file)
    if not data:
        return None

    # Les anciens caches (sans marqueur) sont considers non fiables,
    # et un cache explicitement invalide force aussi un refetch.
    if "cache_valid" not in data or data.get("cache_valid") is False:
        return None

    timestamp = data.get("timestamp")
    if not isinstance(timestamp, (int, float)):
        return None

    if time.time() - timestamp >= cache_ttl:
        return None

    remaining_seconds = max(0, int(cache_ttl - (time.time() - timestamp)))
    remaining_minutes = max(1, (remaining_seconds + 59) // 60)

    videos = extract_cache_videos(data)
    if not isinstance(videos, list):
        return None

    timestamp_fr = data.get("timestamp_fr")
    if timestamp_fr is not None and not isinstance(timestamp_fr, str):
        timestamp_fr = str(timestamp_fr)

    return {
        "videos": videos,
        "timestamp": float(timestamp),
        "timestamp_fr": timestamp_fr,
        "remaining_minutes": remaining_minutes,
    }


def write_result(
    *,
    output_file,
    storage_dir,
    url,
    timestamp2fr,
    videos,
    total_playlist,
    excluded_ids=None,
    excluded_count=None,
    cache_valid=True,
):
    os.makedirs(storage_dir, exist_ok=True)
    now_ts = time.time()
    scraped = len(videos)
    normalized_excluded_ids = []
    if isinstance(excluded_ids, (list, set, tuple)):
        normalized_excluded_ids = sorted(
            {
                video_id
                for video_id in excluded_ids
                if isinstance(video_id, str) and video_id
            }
        )

    normalized_excluded_count = (
        excluded_count
        if isinstance(excluded_count, int)
        else len(normalized_excluded_ids)
    )
    if normalized_excluded_count < len(normalized_excluded_ids):
        normalized_excluded_count = len(normalized_excluded_ids)
    if normalized_excluded_count < 0:
        normalized_excluded_count = 0

    if isinstance(total_playlist, int):
        max_excluded_for_consistency = max(0, total_playlist - scraped)
        if normalized_excluded_count > max_excluded_for_consistency:
            normalized_excluded_count = max_excluded_for_consistency

    payload = {
        "url": url,
        "timestamp": now_ts,
        "timestamp_fr": timestamp2fr(now_ts),
        "cache_valid": bool(cache_valid),
        "scraped": scraped,
        "total_playlist": total_playlist,
        "excluded_count": normalized_excluded_count,
        "videos": videos,
        "excluded_ids": normalized_excluded_ids,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return normalized_excluded_count


def read_previous_state(output_file):
    if not os.path.isfile(output_file):
        return []

    try:
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        videos = data.get("videos") if isinstance(data.get("videos"), list) else []
        return videos
    except Exception:
        return []


def read_previous_counts(output_file):
    if not os.path.isfile(output_file):
        return None, None, 0

    try:
        with open(output_file, "r", encoding="utf-8") as f:
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

        excluded_ids = data.get("excluded_ids")
        excluded_ids_count = (
            len(
                [
                    video_id
                    for video_id in excluded_ids
                    if isinstance(video_id, str) and video_id
                ]
            )
            if isinstance(excluded_ids, list)
            else None
        )

        excluded_count = data.get("excluded_count")
        if not isinstance(excluded_count, int):
            legacy_adult_count = data.get("adult_count")
            if isinstance(legacy_adult_count, int):
                excluded_count = legacy_adult_count
            elif excluded_ids_count is not None:
                excluded_count = excluded_ids_count
            else:
                adult_videos = data.get("adult_videos")
                excluded_count = (
                    len(adult_videos) if isinstance(adult_videos, list) else 0
                )

        if excluded_ids_count is not None and excluded_count < excluded_ids_count:
            excluded_count = excluded_ids_count

        if excluded_ids_count is None:
            legacy_adults = data.get("adults")
            if isinstance(legacy_adults, list):
                legacy_count = len(
                    [
                        video_id
                        for video_id in legacy_adults
                        if isinstance(video_id, str) and video_id
                    ]
                )
                if excluded_count < legacy_count:
                    excluded_count = legacy_count

        if not isinstance(total_playlist, int) or total_playlist < (
            scraped + excluded_count
        ):
            total_playlist = max(0, scraped + excluded_count)

        return scraped, total_playlist, excluded_count
    except Exception:
        return None, None, 0


def read_previous_excluded_ids(output_file):
    if not os.path.isfile(output_file):
        return set()

    try:
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        excluded_ids = data.get("excluded_ids")
        if isinstance(excluded_ids, list):
            return {
                video_id
                for video_id in excluded_ids
                if isinstance(video_id, str) and video_id
            }

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


def auto_heal_cache_invariants(cache_file, *, url, timestamp2fr, timestamp_fr_to_epoch):
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

    excluded_ids_raw = data.get("excluded_ids")
    normalized_excluded_ids = []
    if isinstance(excluded_ids_raw, list):
        normalized_excluded_ids = sorted(
            {
                video_id
                for video_id in excluded_ids_raw
                if isinstance(video_id, str) and video_id
            }
        )
    else:
        legacy_adults = data.get("adults")
        if isinstance(legacy_adults, list):
            normalized_excluded_ids = sorted(
                {
                    video_id
                    for video_id in legacy_adults
                    if isinstance(video_id, str) and video_id
                }
            )
        else:
            adult_videos = data.get("adult_videos")
            if isinstance(adult_videos, list):
                normalized_excluded_ids = sorted(
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

    if data.get("excluded_ids") != normalized_excluded_ids:
        data["excluded_ids"] = normalized_excluded_ids
        changed_fields.append("excluded_ids")

    if "adults" in data:
        data.pop("adults", None)
        changed_fields.append("adults")

    videos = data.get("videos")
    if isinstance(videos, list):
        expected_scraped = len(videos)
        if data.get("scraped") != expected_scraped:
            data["scraped"] = expected_scraped
            changed_fields.append("scraped")

    excluded_count = data.get("excluded_count")
    if not isinstance(excluded_count, int):
        legacy_adult_count = data.get("adult_count")
        if isinstance(legacy_adult_count, int):
            excluded_count = legacy_adult_count

    if not isinstance(excluded_count, int) or excluded_count < 0:
        data["excluded_count"] = len(normalized_excluded_ids)
        excluded_count = len(normalized_excluded_ids)
        changed_fields.append("excluded_count")
    elif excluded_count < len(normalized_excluded_ids):
        data["excluded_count"] = len(normalized_excluded_ids)
        excluded_count = len(normalized_excluded_ids)
        changed_fields.append("excluded_count")

    if "adult_count" in data:
        data.pop("adult_count", None)
        changed_fields.append("adult_count")

    total_playlist = data.get("total_playlist")
    if isinstance(total_playlist, int):
        scraped_value = data.get("scraped")
        if isinstance(scraped_value, int):
            max_excluded_for_consistency = max(0, total_playlist - scraped_value)
            if excluded_count > max_excluded_for_consistency:
                data["excluded_count"] = max_excluded_for_consistency
                excluded_count = max_excluded_for_consistency
                changed_fields.append("excluded_count")

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

    if data.get("url") != url:
        data["url"] = url
        changed_fields.append("url")

    current_timestamp = data.get("timestamp")
    current_timestamp_fr = data.get("timestamp_fr")
    if not isinstance(current_timestamp, (int, float)):
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
        raw_excluded = data.get("excluded_count")
        scraped_value = raw_scraped if isinstance(raw_scraped, int) else 0
        excluded_value = raw_excluded if isinstance(raw_excluded, int) else 0
        data["total_playlist"] = max(0, scraped_value + excluded_value)
        changed_fields.append("total_playlist")
    else:
        raw_scraped = data.get("scraped")
        raw_excluded = data.get("excluded_count")
        scraped_value = raw_scraped if isinstance(raw_scraped, int) else 0
        excluded_value = raw_excluded if isinstance(raw_excluded, int) else 0
        min_total = max(0, scraped_value + excluded_value)
        if total_playlist < min_total:
            data["total_playlist"] = min_total
            changed_fields.append("total_playlist")

    if not changed_fields:
        return []

    changed_fields = list(dict.fromkeys(changed_fields))

    if "excluded_ids" in data:
        excluded_ids_value = data.pop("excluded_ids")
        data["excluded_ids"] = excluded_ids_value

    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        return []

    return changed_fields


def bootstrap_missing_cache_from_legacy(output_file, storage_dir, author):
    if os.path.isfile(output_file) or not os.path.isdir(storage_dir):
        return None

    candidates = []
    for name in os.listdir(storage_dir):
        if not name.lower().endswith(".json"):
            continue
        if name == os.path.basename(output_file):
            continue
        if author.lower() not in name.lower():
            continue
        path = os.path.join(storage_dir, name)
        if os.path.isfile(path):
            candidates.append(path)

    if not candidates:
        return None

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

            os.makedirs(storage_dir, exist_ok=True)
            shutil.copyfile(candidate, output_file)
            return candidate
        except Exception:
            continue

    return None
