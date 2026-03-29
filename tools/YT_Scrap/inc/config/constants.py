from typing import TypedDict


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
    "progress": True,
    "ignoreerrors": True,
    "retries": 3,
    "extractor_retries": 3,
    "check_formats": False,
    "socket_timeout": 20,
}

YDL_OPTS_DETAIL_ANDROID: YdlOpts = {
    "extract_flat": False,
    "quiet": True,
    "ignoreerrors": False,
    "retries": 1,
    "extractor_retries": 1,
    "check_formats": False,
    "socket_timeout": 20,
}

KNOWN_IDS_STOP_THRESHOLD = 7
RECENT_PLAYLIST_SCAN_STEP = 40
RECENT_PLAYLIST_SCAN_MAX = 400
