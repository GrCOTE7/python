import argparse
import re
from datetime import datetime
from pathlib import Path

import inc.authors as auth
from inc.runner import run_scrap
from suivi.tracking_store import (
    connect_db,
    get_latest_run_id,
    get_not_seen_yet_videos,
    get_seen_videos,
    init_schema,
    set_video_state,
)


DEFAULT_BPL_TITLE = "# BPL Quotidien (Une lecon - ISC - 2mnPy - BdC - Graven - Jordy + Indently - Fooxpy)"

# 7 chaines cibles. Les IDs "scrap_id" correspondent a inc/authors.py.
TARGET_AUTHORS = [
    {"author": "InformatiqueSansComplexe", "label": "FR Auteur", "scrap_id": 14},
    {"author": "2minutesPy", "label": "FR/GB Auteur", "scrap_id": 17},
    {"author": "bandedecodeurs", "label": "FR Auteur", "scrap_id": 11},
    {"author": "Gravenilvectuto", "label": "FR Auteur", "scrap_id": 7},
    {"author": "JordyBayo", "label": "FR Auteur", "scrap_id": 18},
    {"author": "Indently", "label": "GB Auteur", "scrap_id": 20},
    {"author": "foxxpy", "label": "FR Maths Auteur", "scrap_id": 21},
]

TARGET_BY_AUTHOR = {item["author"]: item for item in TARGET_AUTHORS}


def parse_selection(raw_selection):
    if raw_selection is None or raw_selection.lower() == "default":
        return None

    if raw_selection.lower() == "all":
        return "all"

    if raw_selection.startswith("range:"):
        upper = int(raw_selection.split(":", 1)[1])
        return list(range(upper))

    if "," in raw_selection:
        return [int(item.strip()) for item in raw_selection.split(",") if item.strip()]

    return int(raw_selection)


def _default_scrape_ids(targets):
    return [
        author["scrap_id"]
        for author in targets
        if isinstance(author.get("scrap_id"), int)
    ]


def get_default_target_scrape_ids():
    return _default_scrape_ids(TARGET_AUTHORS)


def _build_targets(raw_authors):
    if not raw_authors:
        return TARGET_AUTHORS

    names = [name.strip() for name in raw_authors.split(",") if name.strip()]
    built = []
    for name in names:
        if name in TARGET_BY_AUTHOR:
            built.append(TARGET_BY_AUTHOR[name])
            continue

        built.append({
            "author": name,
            "label": "Auteur",
            "scrap_id": None,
        })

    return built


def _format_views(views):
    return f"{int(views):,}".replace(",", " ")


def _coerce_int(value, default=0):
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(round(value))
    try:
        return int(str(value).strip())
    except Exception:
        return default


def _format_duration_minutes_fr(total_seconds):
    minutes = max(0, int(total_seconds) // 60)
    hours = minutes // 60
    rem_minutes = minutes % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours} heure{'s' if hours > 1 else ''}")
    if rem_minutes > 0:
        parts.append(f"{rem_minutes} minute{'s' if rem_minutes > 1 else ''}")

    if not parts:
        return "0 minute"
    return " et ".join(parts)


def _minutes_to_hhmm(total_minutes):
    safe_minutes = max(0, _coerce_int(total_minutes, 0))
    hours = safe_minutes // 60
    minutes = safe_minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def _author_alias(author):
    aliases = {
        "InformatiqueSansComplexe": "ISC",
        "2minutesPy": "2mn",
        "bandedecodeurs": "BdC",
        "Gravenilvectuto": "Gravn",
        "JordyBayo": "Jordy",
        "Indently": "Indent",
        "foxxpy": "Foxxy",
    }
    return aliases.get(author, author)


def _build_compact_summary_table_md(rows):
    headers = ["Id", "Auteur", "Vues", "2c", "N & Tps", "Vus", "Reste (%)"]

    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]

    total_videos = sum(row["videos"] for row in rows)
    total_views = sum(row["views"] for row in rows)
    total_minutes = sum(row["total_minutes"] for row in rows)
    total_not_seen = sum(row["not_seen"] for row in rows)
    total_not_seen_minutes = sum(row["not_seen_minutes"] for row in rows)
    total_seen = sum(row["seen"] for row in rows)
    total_seen_minutes = sum(row["seen_minutes"] for row in rows)

    for row in rows:
        pct_n = f"{(100.0 * row['not_seen'] / row['videos']):.1f}%" if row["videos"] > 0 else "0.0%"
        pct_t = (
            f"{(100.0 * row['not_seen_minutes'] / row['total_minutes']):.1f}%"
            if row["total_minutes"] > 0
            else "0.0%"
        )

        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["id"]),
                    _author_alias(row["author"]),
                    _format_views(row["views"]),
                    f"{row['not_seen']}<br>{_minutes_to_hhmm(row['not_seen_minutes'])}",
                    f"{row['videos']}<br>{_minutes_to_hhmm(row['total_minutes'])}",
                    f"{row['seen']}<br>{_minutes_to_hhmm(row['seen_minutes'])}",
                    f"{pct_n}<br>{pct_t}",
                ]
            )
            + " |"
        )

    total_pct_n = f"{(100.0 * total_not_seen / total_videos):.1f}%" if total_videos > 0 else "0.0%"
    total_pct_t = (
        f"{(100.0 * total_not_seen_minutes / total_minutes):.1f}%"
        if total_minutes > 0
        else "0.0%"
    )

    lines.append(
        "| "
        + " | ".join(
            [
                str(len(rows)),
                "TOTAL",
                _format_views(total_views),
                f"{total_not_seen}<br>{_minutes_to_hhmm(total_not_seen_minutes)}",
                f"{total_videos}<br>{_minutes_to_hhmm(total_minutes)}",
                f"{total_seen}<br>{_minutes_to_hhmm(total_seen_minutes)}",
                f"{total_pct_n}<br>{total_pct_t}",
            ]
        )
        + " |"
    )

    return lines


def _extract_video_id_from_line(line):
    match = re.search(r"(?:[?&]v=|youtu\.be/)([A-Za-z0-9_-]+)", line)
    return match.group(1) if match else None


def extract_markdown_states(markdown_path):
    states = {}
    if not markdown_path.is_file():
        return states

    for raw_line in markdown_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not (line.startswith("* [x]") or line.startswith("* [ ]")):
            continue

        video_id = _extract_video_id_from_line(line)
        if not video_id:
            continue

        states[video_id] = "seen" if line.startswith("* [x]") else "unseen"

    return states


def _read_existing_title(markdown_path):
    if not markdown_path.is_file():
        return DEFAULT_BPL_TITLE

    for raw_line in markdown_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("# "):
            return line

    return DEFAULT_BPL_TITLE


def _format_published_date_fr(raw_published):
    if raw_published is None:
        return "N/A"

    text = str(raw_published).strip()
    if not text:
        return "N/A"

    # Deja au format JJ/MM/AAAA.
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", text):
        return text

    # Cas principal du pipeline actuel: YYYYMMDD.
    if re.fullmatch(r"\d{8}", text):
        try:
            return datetime.strptime(text, "%Y%m%d").strftime("%d/%m/%Y")
        except ValueError:
            return text

    # Accepte aussi YYYY-MM-DD et YYYY/MM/DD.
    normalized = text.replace("-", "/")
    if re.fullmatch(r"\d{4}/\d{2}/\d{2}", normalized):
        try:
            return datetime.strptime(normalized, "%Y/%m/%d").strftime("%d/%m/%Y")
        except ValueError:
            return text

    return text


def _video_line(video, checked=False):
    url = video.get("video_url")
    if not isinstance(url, str) or not url:
        return None

    title = video.get("title") or "N/A"
    published = _format_published_date_fr(video.get("published_at"))
    duration = video.get("duration_text") or "N/A"
    views = _format_views(_coerce_int(video.get("views"), 0))
    checkbox = "x" if checked else " "
    return f"* [{checkbox}] [{published} **{title}** {views} **{duration}**]({url})"


def _filter_existing_video_ids(conn, video_ids):
    clean_ids = [video_id for video_id in video_ids if isinstance(video_id, str) and video_id]
    if not clean_ids:
        return set()

    placeholders = ",".join(["?"] * len(clean_ids))
    rows = conn.execute(
        f"SELECT video_id FROM videos WHERE video_id IN ({placeholders})",
        tuple(clean_ids),
    ).fetchall()
    return {row["video_id"] for row in rows if isinstance(row, dict) and isinstance(row.get("video_id"), str)}


def import_states_into_tracking(db_path, bpl_path):
    states = extract_markdown_states(bpl_path)
    if not states:
        return 0, 0, 0

    conn = connect_db(db_path)
    try:
        init_schema(conn)
        existing_ids = _filter_existing_video_ids(conn, states.keys())
    finally:
        conn.close()

    seen_ids = [video_id for video_id, state in states.items() if state == "seen" and video_id in existing_ids]
    unseen_ids = [video_id for video_id, state in states.items() if state == "unseen" and video_id in existing_ids]

    updated_seen = set_video_state(db_path=db_path, video_ids=seen_ids, state="seen", source="bpl_import") if seen_ids else 0
    updated_unseen = set_video_state(db_path=db_path, video_ids=unseen_ids, state="unseen", source="bpl_import") if unseen_ids else 0
    ignored_not_found = len(states) - len(existing_ids)

    return updated_seen, updated_unseen, ignored_not_found


def build_bpl(db_path, bpl_path, targets):
    conn = connect_db(db_path)
    try:
        init_schema(conn)
        title = _read_existing_title(bpl_path)

        available_runs = 0
        for target in targets:
            run_id = get_latest_run_id(conn, target["author"])
            if isinstance(run_id, int):
                available_runs += 1

        if available_runs == 0 and bpl_path.is_file():
            existing_text = bpl_path.read_text(encoding="utf-8")
            if "* [" in existing_text:
                return {
                    "written": False,
                    "reason": "no_target_data",
                    "available_runs": 0,
                    "target_count": len(targets),
                }

        lines = [title, ""]
        summary_rows = []

        for index, target in enumerate(targets, start=1):
            author = target["author"]
            label = target["label"]
            author_url = f"https://www.youtube.com/@{author}/videos"
            run_id = get_latest_run_id(conn, author)

            if not isinstance(run_id, int):
                summary_rows.append(
                    {
                        "id": target.get("scrap_id") if isinstance(target.get("scrap_id"), int) else index,
                        "author": author,
                        "views": 0,
                        "videos": 0,
                        "total_minutes": 0,
                        "not_seen": 0,
                        "not_seen_minutes": 0,
                        "seen": 0,
                        "seen_minutes": 0,
                    }
                )
                lines.append(f"## {index} {label} **[{author}]({author_url})**")
                lines.append("")
                lines.append("* [ ] Aucune donnee disponible dans tracking.sqlite3 pour cette chaine.")
                lines.append("")
                continue

            not_seen = get_not_seen_yet_videos(db_path, author, run_id=run_id)
            seen = get_seen_videos(db_path, author, run_id=run_id)
            all_videos = not_seen + seen

            total_count = len(all_videos)
            total_views = sum(_coerce_int(video.get("views"), 0) for video in all_videos)
            total_seconds = sum(_coerce_int(video.get("duration_seconds"), 0) for video in all_videos)
            not_seen_seconds = sum(
                _coerce_int(video.get("duration_seconds"), 0) for video in not_seen
            )
            seen_seconds = sum(
                _coerce_int(video.get("duration_seconds"), 0) for video in seen
            )

            summary_rows.append(
                {
                    "id": target.get("scrap_id") if isinstance(target.get("scrap_id"), int) else index,
                    "author": author,
                    "views": total_views,
                    "videos": total_count,
                    "total_minutes": max(0, total_seconds // 60),
                    "not_seen": len(not_seen),
                    "not_seen_minutes": max(0, not_seen_seconds // 60),
                    "seen": len(seen),
                    "seen_minutes": max(0, seen_seconds // 60),
                }
            )
            video_word = "video" if total_count == 1 else "videos"

            lines.append(
                f"## {index} {label} **[{author}]({author_url})** ( **{total_count}** {video_word} - {_format_views(total_views)} vues - {_format_duration_minutes_fr(total_seconds)} )"
            )
            lines.append("")

            has_both_groups = bool(not_seen) and bool(seen)
            if has_both_groups:
                lines.append(
                    f"### Pas vus ({len(not_seen)} - {_format_duration_minutes_fr(not_seen_seconds)})"
                )
                lines.append("")

            for video in not_seen:
                rendered = _video_line(video, checked=False)
                if rendered:
                    lines.append(rendered)

            if has_both_groups and seen:
                if lines and lines[-1] != "":
                    lines.append("")
                lines.append(
                    f"### Vus ({len(seen)} - {_format_duration_minutes_fr(seen_seconds)})"
                )
                lines.append("")

            for video in seen:
                rendered = _video_line(video, checked=True)
                if rendered:
                    lines.append(rendered)

            lines.append("")

        if summary_rows:
            summary_block = _build_compact_summary_table_md(summary_rows)
            lines = lines[:2] + summary_block + [""] + lines[2:]

        bpl_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        return {
            "written": True,
            "reason": "ok",
            "available_runs": available_runs,
            "target_count": len(targets),
        }
    finally:
        conn.close()


def run_optional_scrap(selection, targets):
    if selection is None:
        run_scrap(_default_scrape_ids(targets))
        return

    if selection == "all":
        run_scrap(range(auth.nb_authors()))
        return

    run_scrap(selection)


def main():
    parser = argparse.ArgumentParser(
        description="Alimente BPL.md a partir de tools/YT_Scrap/cache/tracking.sqlite3"
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Lance d'abord le scrap YT avant la generation BPL",
    )
    parser.add_argument(
        "--selection",
        type=str,
        default="default",
        help="Selection pour --refresh: default | 1 | 1,2,3 | range:5 | all",
    )
    parser.add_argument(
        "--bpl",
        type=str,
        default=None,
        help="Chemin du fichier BPL cible (defaut: ../../BPL.md)",
    )
    parser.add_argument(
        "--authors",
        type=str,
        default=None,
        help="Liste d'auteurs cible, separes par des virgules (ex: InformatiqueSansComplexe,2minutesPy)",
    )

    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    db_path = script_dir / "cache" / "tracking.sqlite3"
    bpl_path = Path(args.bpl).resolve() if args.bpl else script_dir.parent.parent / "BPL.md"
    targets = _build_targets(args.authors)

    if args.refresh:
        selection = parse_selection(args.selection)
        run_optional_scrap(selection, targets)

    updated_seen, updated_unseen, ignored_not_found = import_states_into_tracking(db_path, bpl_path)
    write_info = build_bpl(db_path, bpl_path, targets)

    print(
        "BPL genere "
        f"(seen_sync={updated_seen}, unseen_sync={updated_unseen}, ids_hors_db={ignored_not_found}) "
        f"-> {bpl_path} | write={write_info.get('written')} | reason={write_info.get('reason')}"
    )


if __name__ == "__main__":
    main()
