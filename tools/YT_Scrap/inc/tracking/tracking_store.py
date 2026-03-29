import re
import sqlite3
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


SQL_SEEN_LATEST_RUN = """
SELECT
  v.video_id,
  v.title,
  v.video_url,
  v.published_at,
  v.duration_text,
  v.duration_seconds,
  v.views,
  ri.position
FROM run_items ri
JOIN videos v ON v.video_id = ri.video_id
LEFT JOIN user_video_state s ON s.video_id = v.video_id
WHERE ri.run_id = ?
  AND ri.present_in_run = 1
  AND COALESCE(s.state, 'unseen') = 'seen'
ORDER BY ri.position ASC;
""".strip()


SQL_NOT_SEEN_LATEST_RUN = """
SELECT
  v.video_id,
  v.title,
  v.video_url,
  v.published_at,
  v.duration_text,
  v.duration_seconds,
  v.views,
  ri.position
FROM run_items ri
JOIN videos v ON v.video_id = ri.video_id
LEFT JOIN user_video_state s ON s.video_id = v.video_id
WHERE ri.run_id = ?
  AND ri.present_in_run = 1
  AND COALESCE(s.state, 'unseen') <> 'seen'
ORDER BY ri.position ASC;
""".strip()


@dataclass
class MergeResult:
    run_id: int
    total_items: int
    inserted_or_updated_videos: int


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


def _extract_video_id(video_url: str) -> Optional[str]:
    if not isinstance(video_url, str) or not video_url:
        return None
    match = re.search(r"[?&]v=([A-Za-z0-9_-]+)", video_url)
    if match:
        return match.group(1)
    tail_match = re.search(r"youtu\.be/([A-Za-z0-9_-]+)", video_url)
    if tail_match:
        return tail_match.group(1)
    return None


def _normalize_run_item(item: dict, position: int) -> Optional[dict]:
    if not isinstance(item, dict):
        return None

    video_id = item.get("id") or _extract_video_id(item.get("url") or "")
    if not isinstance(video_id, str) or not video_id:
        return None

    title = item.get("titre") or item.get("title") or "N/A"
    url = item.get("url") or item.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}"

    published = _format_published_date_fr(item.get("date") or item.get("date_fr") or "")
    duration_seconds = _coerce_int(item.get("duration"), 0)
    duration_text = item.get("duree") or "N/A"
    views = _coerce_int(item.get("vues") if item.get("vues") is not None else item.get("view_count"), 0)

    unavailable = 0
    unavailable_raw = item.get("unavailable")
    if isinstance(unavailable_raw, bool):
        unavailable = int(unavailable_raw)
    elif isinstance(title, str) and "INDISPONIBLE" in title.upper():
        unavailable = 1

    return {
        "video_id": video_id,
        "title": str(title),
        "video_url": str(url),
        "published_at": str(published),
        "duration_seconds": max(0, duration_seconds),
        "duration_text": str(duration_text),
        "views": max(0, views),
        "position": position,
        "unavailable": unavailable,
    }


def _format_published_date_fr(raw_published) -> str:
    if raw_published is None:
        return "N/A"

    text = str(raw_published).strip()
    if not text:
        return "N/A"

    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", text):
        return text

    if re.fullmatch(r"\d{8}", text):
        try:
            return datetime.strptime(text, "%Y%m%d").strftime("%d/%m/%Y")
        except ValueError:
            return text

    normalized = text.replace("-", "/")
    if re.fullmatch(r"\d{4}/\d{2}/\d{2}", normalized):
        try:
            return datetime.strptime(normalized, "%Y/%m/%d").strftime("%d/%m/%Y")
        except ValueError:
            return text

    return text


def _row_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}


def connect_db(db_path: Path | str) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = _row_factory
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS scrape_runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            source_file TEXT,
            started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            finished_at TEXT,
            items_count INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS videos (
            video_id TEXT PRIMARY KEY,
            author TEXT NOT NULL,
            title TEXT,
            video_url TEXT,
            published_at TEXT,
            duration_seconds INTEGER NOT NULL DEFAULT 0,
            duration_text TEXT,
            views INTEGER NOT NULL DEFAULT 0,
            unavailable INTEGER NOT NULL DEFAULT 0,
            first_seen_run_id INTEGER,
            last_seen_run_id INTEGER,
            first_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(first_seen_run_id) REFERENCES scrape_runs(run_id),
            FOREIGN KEY(last_seen_run_id) REFERENCES scrape_runs(run_id)
        );

        CREATE TABLE IF NOT EXISTS user_video_state (
            video_id TEXT PRIMARY KEY,
            state TEXT NOT NULL CHECK (state IN ('unseen', 'seen', 'ignored', 'watch_later')),
            source TEXT NOT NULL DEFAULT 'manual',
            state_updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(video_id) REFERENCES videos(video_id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS run_items (
            run_id INTEGER NOT NULL,
            video_id TEXT NOT NULL,
            position INTEGER NOT NULL,
            present_in_run INTEGER NOT NULL DEFAULT 1,
            PRIMARY KEY (run_id, video_id),
            FOREIGN KEY(run_id) REFERENCES scrape_runs(run_id) ON DELETE CASCADE,
            FOREIGN KEY(video_id) REFERENCES videos(video_id) ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_runs_author ON scrape_runs(author, run_id DESC);
        CREATE INDEX IF NOT EXISTS idx_videos_author_last_seen ON videos(author, last_seen_run_id DESC);
        CREATE INDEX IF NOT EXISTS idx_run_items_run_pos ON run_items(run_id, position);
        CREATE INDEX IF NOT EXISTS idx_state_state ON user_video_state(state);
        """
    )
    conn.commit()


def get_latest_run_id(conn: sqlite3.Connection, author: str) -> Optional[int]:
    row = conn.execute(
        "SELECT run_id FROM scrape_runs WHERE author = ? ORDER BY run_id DESC LIMIT 1",
        (author,),
    ).fetchone()
    if not isinstance(row, dict):
        return None
    run_id = row.get("run_id")
    return run_id if isinstance(run_id, int) else None


def merge_scrape(
    db_path: Path | str,
    author: str,
    run_items: Iterable[dict],
    source_file: Optional[str] = None,
) -> MergeResult:
    normalized = []
    for idx, item in enumerate(run_items, start=1):
        parsed = _normalize_run_item(item, idx)
        if parsed:
            normalized.append(parsed)

    conn = connect_db(db_path)
    try:
        init_schema(conn)

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO scrape_runs(author, source_file, items_count) VALUES (?, ?, ?)",
            (author, source_file, len(normalized)),
        )
        lastrowid = cur.lastrowid
        if not isinstance(lastrowid, int):
            raise RuntimeError("Impossible de recuperer run_id apres insertion scrape_runs")
        run_id = lastrowid

        upsert_count = 0
        for item in normalized:
            cur.execute(
                """
                INSERT INTO videos(
                    video_id, author, title, video_url, published_at,
                    duration_seconds, duration_text, views, unavailable,
                    first_seen_run_id, last_seen_run_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(video_id) DO UPDATE SET
                    author = excluded.author,
                    title = CASE
                        WHEN excluded.title IS NOT NULL AND excluded.title <> '' THEN excluded.title
                        ELSE videos.title
                    END,
                    video_url = CASE
                        WHEN excluded.video_url IS NOT NULL AND excluded.video_url <> '' THEN excluded.video_url
                        ELSE videos.video_url
                    END,
                    published_at = CASE
                        WHEN excluded.published_at IS NOT NULL AND excluded.published_at <> '' THEN excluded.published_at
                        ELSE videos.published_at
                    END,
                    duration_seconds = CASE
                        WHEN excluded.duration_seconds > 0 THEN excluded.duration_seconds
                        ELSE videos.duration_seconds
                    END,
                    duration_text = CASE
                        WHEN excluded.duration_text IS NOT NULL AND excluded.duration_text <> '' THEN excluded.duration_text
                        ELSE videos.duration_text
                    END,
                    views = CASE
                        WHEN excluded.views >= 0 THEN excluded.views
                        ELSE videos.views
                    END,
                    unavailable = excluded.unavailable,
                    last_seen_run_id = excluded.last_seen_run_id,
                    last_seen_at = CURRENT_TIMESTAMP
                """,
                (
                    item["video_id"],
                    author,
                    item["title"],
                    item["video_url"],
                    item["published_at"],
                    item["duration_seconds"],
                    item["duration_text"],
                    item["views"],
                    item["unavailable"],
                    run_id,
                    run_id,
                ),
            )

            cur.execute(
                """
                INSERT OR REPLACE INTO run_items(run_id, video_id, position, present_in_run)
                VALUES (?, ?, ?, 1)
                """,
                (run_id, item["video_id"], item["position"]),
            )

            cur.execute(
                """
                INSERT INTO user_video_state(video_id, state, source)
                VALUES (?, 'unseen', 'auto')
                ON CONFLICT(video_id) DO NOTHING
                """,
                (item["video_id"],),
            )
            upsert_count += 1

        cur.execute(
            "UPDATE scrape_runs SET finished_at = CURRENT_TIMESTAMP, items_count = ? WHERE run_id = ?",
            (len(normalized), run_id),
        )

        conn.commit()
        return MergeResult(
            run_id=run_id,
            total_items=len(normalized),
            inserted_or_updated_videos=upsert_count,
        )
    finally:
        conn.close()


def set_video_state(
    db_path: Path | str,
    video_ids: Iterable[str],
    state: str = "seen",
    source: str = "manual",
) -> int:
    allowed_states = {"unseen", "seen", "ignored", "watch_later"}
    if state not in allowed_states:
        raise ValueError(f"Etat invalide: {state}")

    clean_ids = [video_id for video_id in video_ids if isinstance(video_id, str) and video_id]
    if not clean_ids:
        return 0

    conn = connect_db(db_path)
    try:
        init_schema(conn)
        cur = conn.cursor()
        touched = 0
        for video_id in clean_ids:
            cur.execute(
                """
                INSERT INTO user_video_state(video_id, state, source, state_updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(video_id) DO UPDATE SET
                    state = excluded.state,
                    source = excluded.source,
                    state_updated_at = CURRENT_TIMESTAMP
                """,
                (video_id, state, source),
            )
            touched += 1

        conn.commit()
        return touched
    finally:
        conn.close()


def _query_rows(conn: sqlite3.Connection, sql: str, run_id: int) -> list[dict]:
    return conn.execute(sql, (run_id,)).fetchall()


def get_seen_videos(
    db_path: Path | str,
    author: str,
    run_id: Optional[int] = None,
) -> list[dict]:
    conn = connect_db(db_path)
    try:
        init_schema(conn)
        effective_run = run_id if isinstance(run_id, int) else get_latest_run_id(conn, author)
        if not isinstance(effective_run, int):
            return []
        return _query_rows(conn, SQL_SEEN_LATEST_RUN, effective_run)
    finally:
        conn.close()


def get_not_seen_yet_videos(
    db_path: Path | str,
    author: str,
    run_id: Optional[int] = None,
) -> list[dict]:
    conn = connect_db(db_path)
    try:
        init_schema(conn)
        effective_run = run_id if isinstance(run_id, int) else get_latest_run_id(conn, author)
        if not isinstance(effective_run, int):
            return []
        return _query_rows(conn, SQL_NOT_SEEN_LATEST_RUN, effective_run)
    finally:
        conn.close()


def _format_views(views: int) -> str:
    return f"{int(views):,}".replace(",", " ")


def _format_duration_minutes_fr(total_seconds: int) -> str:
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


def _render_md_line(video: dict, checkbox: str) -> Optional[str]:
    url = video.get("video_url")
    if not isinstance(url, str) or not url:
        return None

    title = video.get("title") or "N/A"
    published = _format_published_date_fr(video.get("published_at"))
    duration = video.get("duration_text") or "N/A"
    views = _format_views(_coerce_int(video.get("views"), 0))

    return f"* [{checkbox}] [{published} **{title}** {views} **{duration}**]({url})"


def export_markdown(
    db_path: Path | str,
    author: str,
    output_md_file: Path | str,
    run_id: Optional[int] = None,
    author_url: str = "",
) -> dict:
    conn = connect_db(db_path)
    try:
        init_schema(conn)
        effective_run = run_id if isinstance(run_id, int) else get_latest_run_id(conn, author)
        if not isinstance(effective_run, int):
            return {"run_id": None, "seen_count": 0, "not_seen_count": 0, "output": str(output_md_file)}

        seen = _query_rows(conn, SQL_SEEN_LATEST_RUN, effective_run)
        not_seen = _query_rows(conn, SQL_NOT_SEEN_LATEST_RUN, effective_run)
    finally:
        conn.close()

    lines = ["# BP Learning - Vidéos à voir", ""]
    author_ref = f"[{author}]({author_url})" if author_url else author
    all_videos = not_seen + seen
    total_count = len(all_videos)
    total_views = sum(_coerce_int(v.get("views"), 0) for v in all_videos)
    total_seconds = sum(_coerce_int(v.get("duration_seconds"), 0) for v in all_videos)

    total_count_txt = f"**{total_count}**"
    video_word = "video" if total_count == 1 else "videos"
    total_views_txt = _format_views(total_views)
    total_duration_txt = _format_duration_minutes_fr(total_seconds)

    lines.append(
        f"## Auteur **{author_ref}** ( {total_count_txt} {video_word} - {total_views_txt} vues - {total_duration_txt} )"
    )
    lines.append("")

    has_both_groups = bool(not_seen) and bool(seen)

    if has_both_groups:
        not_seen_seconds = sum(_coerce_int(v.get("duration_seconds"), 0) for v in not_seen)
        lines.append(
            f"### Pas vus ({len(not_seen)} - {_format_duration_minutes_fr(not_seen_seconds)})"
        )
        lines.append("")

    for video in not_seen:
        line = _render_md_line(video, " ")
        if line:
            lines.append(line)

    if has_both_groups and seen:
        if lines and lines[-1] != "":
            lines.append("")
        seen_seconds = sum(_coerce_int(v.get("duration_seconds"), 0) for v in seen)
        lines.append(f"### Vus ({len(seen)} - {_format_duration_minutes_fr(seen_seconds)})")
        lines.append("")

    for video in seen:
        line = _render_md_line(video, "x")
        if line:
            lines.append(line)

    output_path = Path(output_md_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    return {
        "run_id": effective_run,
        "seen_count": len(seen),
        "not_seen_count": len(not_seen),
        "output": str(output_path),
    }
