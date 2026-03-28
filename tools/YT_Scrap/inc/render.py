import os, re

from tabulate import tabulate
from pymox_kit import SB, R, GREEN, nf

from inc.video import format_remaining_time_fr


def write_markdown_file(videos, total_playlist, author, url, storage_dir, output_md_file):
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
        partiel_txt1 = " ⚠️ PARTIEL → "
        partiel_txt2 = f"/ **{total_playlist}** "

    bilan = f"({partiel_txt1} {nb_videos_txt} {partiel_txt2}- {total_views_txt} vues - {total_duration_txt} )"
    md += f"## Auteur **[{author}]({url})** {bilan}\n\n"

    bilan = bilan.replace("*", "").strip()

    for video in videos:
        if not isinstance(video, dict):
            continue

        titre = video.get("titre") or "N/A"
        vues = video.get("vues") if isinstance(video.get("vues"), int) else 0
        duree = video.get("duree") or "N/A"
        date_fr = video.get("date_fr") or "N/A"
        video_url = video.get("url") or ""

        if not video_url:
            continue

        md += (
            "* [ ] ["
            + f"{date_fr} **{titre}** {vues} **{duree}**"
            + "]("
            + video_url
            + ")\n"
        )

    os.makedirs(storage_dir, exist_ok=True)
    with open(output_md_file, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"{GREEN}Fichier markdown généré : {output_md_file}{R}")
    return bilan


def _parse_duration_seconds(duration_text):
    if not isinstance(duration_text, str):
        return 0

    text = duration_text.strip()
    if not text:
        return 0

    parts = text.split(":")
    if len(parts) == 2:
        try:
            minutes = int(parts[0])
            seconds = int(parts[1])
            return max(0, minutes * 60 + seconds)
        except ValueError:
            return 0

    if len(parts) == 3:
        try:
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])
            return max(0, hours * 3600 + minutes * 60 + seconds)
        except ValueError:
            return 0

    return 0


def _extract_md_seen_unseen_stats(md_file_path):
    stats = {
        "not_seen_count": 0,
        "not_seen_seconds": 0,
        "seen_count": 0,
        "seen_seconds": 0,
    }

    if not isinstance(md_file_path, str) or not os.path.isfile(md_file_path):
        return stats

    line_re = re.compile(r"^\* \[(?P<state>[ x])\].*\*\*(?P<dur>\d{1,2}:\d{2}(?::\d{2})?)\*\*\]\(")

    with open(md_file_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            match = line_re.match(line)
            if not match:
                continue

            duration_seconds = _parse_duration_seconds(match.group("dur"))
            if match.group("state") == "x":
                stats["seen_count"] += 1
                stats["seen_seconds"] += duration_seconds
            else:
                stats["not_seen_count"] += 1
                stats["not_seen_seconds"] += duration_seconds

    return stats


def _format_ratio_percent(part, total):
    if not isinstance(total, int) or total <= 0:
        return "0.0%"
    return f"{(100.0 * part / total):.1f}%"


def build_scrap_summary_row(ida, author, videos, md_file_path=None):
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

    stats = _extract_md_seen_unseen_stats(md_file_path)
    seen_count = stats["seen_count"]
    seen_seconds = stats["seen_seconds"]
    not_seen_count = stats["not_seen_count"]
    not_seen_seconds = stats["not_seen_seconds"]

    # Fallback: si le markdown n'est pas dispo, on considere tout en "pas vus".
    if seen_count + not_seen_count == 0 and videos_count > 0:
        not_seen_count = videos_count
        not_seen_seconds = total_duration_seconds

    seen_duration_txt = format_remaining_time_fr(seen_seconds // 60)
    not_seen_duration_txt = format_remaining_time_fr(not_seen_seconds // 60)
    seen_pct_count_txt = _format_ratio_percent(seen_count, videos_count)
    seen_pct_duration_txt = _format_ratio_percent(seen_seconds, total_duration_seconds)

    return [
        ida,
        author,
        videos_count,
        total_views_txt,
        total_duration_txt,
        not_seen_count,
        not_seen_duration_txt,
        seen_count,
        seen_duration_txt,
        seen_pct_count_txt,
        seen_pct_duration_txt,
    ]


def print_scrap_summary_table(rows):
    if not rows:
        return

    author_alias_map = {
        "InformatiqueSansComplexe": "ISC",
        "2minutesPy": "2mn",
        "bandedecodeurs": "BdC",
        "Gravenilvectuto": "Gravn",
        "JordyBayo": "Jordy",
        "Indently": "Indent",
        "foxxpy": "Foxxy",
    }
    author_order = [
        "InformatiqueSansComplexe",
        "2minutesPy",
        "bandedecodeurs",
        "Gravenilvectuto",
        "JordyBayo",
        "Indently",
        "foxxpy",
    ]
    author_rank = {name: idx for idx, name in enumerate(author_order)}

    def bold(value):
        return f"{SB}{value}{R}"

    def author_alias(author_name):
        if not isinstance(author_name, str):
            return "N/A"
        return author_alias_map.get(author_name, author_name)

    def author_sort_key(row):
        name = row[1] if len(row) > 1 else ""
        return (author_rank.get(name, 999), str(name).lower())

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

    def minutes_to_hhmm(total_minutes):
        if not isinstance(total_minutes, int) or total_minutes < 0:
            return "00:00"
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"

    rows = sorted(rows, key=author_sort_key)

    total_scraps = len(rows)
    videos_values = [int(row[2]) if isinstance(row[2], int) else 0 for row in rows]
    views_values = [parse_views(row[3]) for row in rows]
    duration_minutes_values = [parse_duration_minutes(row[4]) for row in rows]
    not_seen_values = [int(row[5]) if isinstance(row[5], int) else 0 for row in rows]
    not_seen_minutes_values = [parse_duration_minutes(row[6]) for row in rows]
    seen_values = [int(row[7]) if isinstance(row[7], int) else 0 for row in rows]
    seen_minutes_values = [parse_duration_minutes(row[8]) for row in rows]

    total_videos = sum(videos_values)
    total_views = sum(views_values)
    total_duration_minutes = sum(duration_minutes_values)
    total_not_seen = sum(not_seen_values)
    total_not_seen_minutes = sum(not_seen_minutes_values)
    total_seen = sum(seen_values)
    total_seen_minutes = sum(seen_minutes_values)

    total_seen_pct_count = (
        f"{(100.0 * total_seen / total_videos):.1f}%"
        if total_videos > 0
        else "0.0%"
    )
    total_seen_pct_duration = (
        f"{(100.0 * total_seen_minutes / total_duration_minutes):.1f}%"
        if total_duration_minutes > 0
        else "0.0%"
    )

    display_rows = [
        [
            row[0],
            author_alias(row[1]),
            row[3],
            (
                f"{nf(row[5], 0) if isinstance(row[5], int) else row[5]}\n"
                f"{minutes_to_hhmm(parse_duration_minutes(row[6]))}"
            ),
            (
                f"{nf(row[2], 0) if isinstance(row[2], int) else row[2]}\n"
                f"{minutes_to_hhmm(parse_duration_minutes(row[4]))}"
            ),
            (
                f"{nf(row[7], 0) if isinstance(row[7], int) else row[7]}\n"
                f"{minutes_to_hhmm(parse_duration_minutes(row[8]))}"
            ),
            f"{row[9]}\n{row[10]}",
        ]
        for row in rows
    ]

    total_row = [
        bold(total_scraps),
        bold("TOTAL"),
        bold(f"{total_views:,}".replace(",", " ")),
        bold(f"{nf(total_not_seen, 0)}\n{minutes_to_hhmm(total_not_seen_minutes)}"),
        bold(f"{nf(total_videos, 0)}\n{minutes_to_hhmm(total_duration_minutes)}"),
        bold(f"{nf(total_seen, 0)}\n{minutes_to_hhmm(total_seen_minutes)}"),
        bold(f"{total_seen_pct_count}\n{total_seen_pct_duration}"),
    ]

    table_rows = display_rows + [total_row]

    headers = [
        bold("id"),
        bold("Auteur"),
        bold("Vues"),
        bold("2c"),
        bold("N & Tps"),
        bold("Vus"),
        bold("Suivis (%)"),
    ]
    print(
        tabulate(
            table_rows,
            headers=headers,
            tablefmt="fancy_grid",
            colalign=(
                "right",
                "left",
                "right",
                "right",
                "right",
                "right",
                "right",
            ),
        )
    )
