import json
import re
from pathlib import Path
from datetime import timedelta

from tracking_store import export_markdown, merge_scrape, set_video_state


def parse_duration(text):
    """Convertit une durée 'MM:SS' ou 'HH:MM:SS' en timedelta."""
    parts = text.split(":")
    parts = list(map(int, parts))
    if len(parts) == 2:  # MM:SS
        minutes, seconds = parts
        return timedelta(minutes=minutes, seconds=seconds)
    elif len(parts) == 3:  # HH:MM:SS
        hours, minutes, seconds = parts
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return timedelta(0)


def _extract_markdown_states(filename):
    seen = []
    unchecked = []
    total_duration = timedelta(0)

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not (line.startswith("* [ ]") or line.startswith("* [x]")):
                continue

            is_seen = line.startswith("* [x]")

            # Extraction de l'ID YouTube
            match_id = re.search(r"v=([A-Za-z0-9_-]+)", line)
            video_id = match_id.group(1) if match_id else None
            if not video_id:
                continue

            # Extraction de la durée (dernier **XX:XX**)
            match_duration = re.findall(r"\*\*(\d{1,2}:\d{2}(?::\d{2})?)\*\*", line)
            duration = (
                parse_duration(match_duration[-1]) if match_duration else timedelta(0)
            )

            if is_seen:
                seen.append(video_id)
            else:
                unchecked.append(video_id)
                total_duration += duration

    return seen, unchecked, total_duration


def _build_run_items_from_cache_json(cache_json_file):
    payload = json.loads(Path(cache_json_file).read_text(encoding="utf-8"))
    videos = payload.get("videos") if isinstance(payload, dict) else []
    if not isinstance(videos, list):
        return []
    return [item for item in videos if isinstance(item, dict)]


if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent.parent
    cache_dir = BASE_DIR / "cache"
    db_path = cache_dir / "tracking.sqlite3"

    author = "LionelCOTE"
    author_url = "https://www.youtube.com/@LionelCOTE"
    candidate_cache_json_files = [
        cache_dir / f"{author}.json",
        cache_dir / f"{author}_videos.json",
        cache_dir / f"{author}_YT.json",
    ]
    previous_md = cache_dir / f"{author}_YT.md"
    output_md = cache_dir / f"{author}_YT.md"

    cache_json_file = None
    for candidate in candidate_cache_json_files:
        if candidate.is_file():
            cache_json_file = candidate
            break

    if cache_json_file is None:
        names = ", ".join(str(p.name) for p in candidate_cache_json_files)
        raise FileNotFoundError(
            f"Aucun cache JSON trouve pour {author}. Fichiers attendus: {names}"
        )

    run_items = _build_run_items_from_cache_json(cache_json_file)
    merge_result = merge_scrape(
        db_path=db_path,
        author=author,
        run_items=run_items,
        source_file=str(cache_json_file),
    )

    if previous_md.is_file():
        seen_ids, unchecked_ids, total_remaining = _extract_markdown_states(previous_md)
        if seen_ids:
            set_video_state(db_path, seen_ids, state="seen", source="md_import")
        if unchecked_ids:
            set_video_state(db_path, unchecked_ids, state="unseen", source="md_import")

        print(
            f"Import markdown: seen={len(seen_ids)} | not_seen={len(unchecked_ids)} | total_remaining={total_remaining}"
        )

    summary = export_markdown(
        db_path=db_path,
        author=author,
        output_md_file=output_md,
        author_url=author_url,
    )

    print(
        "Merge OK "
        f"run_id={merge_result.run_id} "
        f"items={merge_result.total_items} "
        f"updated={merge_result.inserted_or_updated_videos}"
    )
    print(
        "Export markdown OK "
        f"run_id={summary['run_id']} "
        f"not_seen={summary['not_seen_count']} "
        f"seen={summary['seen_count']} "
        f"file={summary['output']}"
    )
