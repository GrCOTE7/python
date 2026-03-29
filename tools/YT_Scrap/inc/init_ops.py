import os
from inc import cache as cache_ops


def build_init_context(
    *,
    ida,
    manager_file,
    get_author_name_fn,
):
    """Construit le contexte d'initialisation runtime pour une chaine cible."""
    author = get_author_name_fn(ida)
    url = f"https://www.youtube.com/@{author}/videos"

    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(manager_file)))
    storage_dir = os.path.join(script_dir, "cache")

    output_file = os.path.join(storage_dir, f"{author}_videos.json")
    output_md_file = os.path.join(storage_dir, f"{author}_YT.md")

    # cache_ttl = 60 # 86400
    cache_ttl = 86400
    max_cumulated_403_errors = 7
    pause_on_rate_limit = 5
    max_stall_retries = 3
    total_playlist_drop_guard_ratio = 0.03
    playlist_fetch_timeout_seconds = 45
    playlist_fetch_max_total_seconds = 900

    return {
        "AUTHOR": author,
        "URL": url,
        "SCRIPT_DIR": script_dir,
        "STORAGE_DIR": storage_dir,
        "OUTPUT_FILE": output_file,
        "OUTPUT_MD_FILE": output_md_file,
        "CACHE_TTL": cache_ttl,
        "MAX_CUMULATED_403_ERRORS": max_cumulated_403_errors,
        "PAUSE_ON_RATE_LIMIT": pause_on_rate_limit,
        "MAX_STALL_RETRIES": max_stall_retries,
        "TOTAL_PLAYLIST_DROP_GUARD_RATIO": total_playlist_drop_guard_ratio,
        "PLAYLIST_FETCH_TIMEOUT_SECONDS": playlist_fetch_timeout_seconds,
        "PLAYLIST_FETCH_MAX_TOTAL_SECONDS": playlist_fetch_max_total_seconds,
        "get_valid_cache_entry": cache_ops.get_valid_cache_entry,
    }
