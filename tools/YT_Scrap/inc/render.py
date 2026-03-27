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
