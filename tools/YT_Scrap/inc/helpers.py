import re
from urllib.parse import parse_qs, urlparse

from pymox_kit import YELLOW, R


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


def remember_excluded_id(excluded_ids, current_id, video_url=None):
    if isinstance(current_id, str) and current_id:
        excluded_ids.add(current_id)
        return current_id

    extracted_id = extract_youtube_id(video_url)
    if isinstance(extracted_id, str) and extracted_id:
        excluded_ids.add(extracted_id)
        return extracted_id

    return None


class CountedErrorTracker:
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
        self.count = 0
        self.stop_requested = False
        self._last_signature = None

    def progress_suffix(self):
        return f"| {YELLOW}403/rate-limit : {self.count}/{self.threshold}{R}"


class YtDlpCountedErrorLogger:
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
