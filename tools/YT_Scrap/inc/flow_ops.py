import threading
import time
from typing import TYPE_CHECKING, cast

import yt_dlp

if TYPE_CHECKING:
    from yt_dlp.YoutubeDL import _Params


def extract_playlist_ids(entries, extract_entry_video_id):
    return [
        entry_id
        for entry in entries
        for entry_id in [extract_entry_video_id(entry)]
        if isinstance(entry_id, str) and entry_id
    ]


def merged_excluded_count(persisted_excluded_count, excluded_ids):
    """Consolide le compteur persistant avec les IDs exclus en memoire."""
    base = persisted_excluded_count if isinstance(persisted_excluded_count, int) else 0
    return max(base, len(excluded_ids))


def compute_cache_completion(
    scraped, total_playlist, excluded_count, compute_effective_total, is_scrap_complete
):
    """Retourne (effective_total, is_complete) pour eviter les blocs repetitifs."""
    effective_total = compute_effective_total(total_playlist, excluded_count)
    return effective_total, is_scrap_complete(scraped, effective_total)


def has_markdown_state_changed(
    previous_scraped,
    previous_effective_total,
    current_scraped,
    current_effective_total,
    is_scrap_complete,
):
    """Detecte un changement d'etat partiel/complet ou de total effectif."""
    return previous_effective_total != current_effective_total or is_scrap_complete(
        previous_scraped, previous_effective_total
    ) != is_scrap_complete(current_scraped, current_effective_total)


def extract_playlist_with_hard_timeout(
    url,
    ydl_opts,
    timeout_seconds,
    max_total_seconds=None,
    cyan="",
    reset="",
):
    """Execute yt-dlp avec timeout d'inactivite + garde-fou global."""
    result_holder = {}
    error_holder = {}

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
                f"Timeout playlist apres {timeout_seconds}s sans activite reseau detectee (logs yt-dlp inactifs)."
            )

        if elapsed >= effective_max_total:
            raise TimeoutError(
                f"Timeout playlist global apres {effective_max_total}s (garde-fou)."
            )

        if elapsed >= next_heartbeat and idle_for >= 5:
            print(
                f"{cyan}... Attente de la reponse YouTube ( {elapsed:>{elapsed_width}}s ecoulees / {effective_max_total}s max, activite il y a {idle_for}s ) ...{reset}",
                flush=True,
            )
            next_heartbeat += 5
        elif elapsed >= next_heartbeat:
            next_heartbeat += 5

        thread.join(1)

    if "exc" in error_holder:
        raise error_holder["exc"]

    return result_holder.get("data")


def scan_recent_entries_until_known_ids(
    url,
    existing_ids,
    excluded_ids,
    known_ids_target,
    recent_playlist_scan_step,
    recent_playlist_scan_max,
    ydl_opts_list,
    playlist_fetch_timeout_seconds,
    playlist_fetch_max_total_seconds,
    extract_playlist_with_hard_timeout_fn,
    extract_playlist_ids_fn,
):
    """Charge progressivement le haut de playlist jusqu'a retrouver N IDs connus consecutifs."""
    upper_bound = 0
    best_entries = []
    detected_total = None
    known_streak = 0

    while upper_bound < recent_playlist_scan_max:
        upper_bound = min(
            upper_bound + recent_playlist_scan_step, recent_playlist_scan_max
        )
        scan_opts = dict(ydl_opts_list)
        scan_opts["playlist_items"] = f"1:{upper_bound}"

        infos = extract_playlist_with_hard_timeout_fn(
            url,
            scan_opts,
            timeout_seconds=min(20, playlist_fetch_timeout_seconds),
            max_total_seconds=min(120, playlist_fetch_max_total_seconds),
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

        playlist_ids = list(dict.fromkeys(extract_playlist_ids_fn(entries)))
        known_streak = 0
        for video_id in playlist_ids:
            if video_id in existing_ids or video_id in excluded_ids:
                known_streak += 1
            else:
                known_streak = 0

            if known_streak >= known_ids_target:
                return best_entries, detected_total, known_streak, upper_bound

        if len(entries) < upper_bound:
            return best_entries, detected_total, known_streak, upper_bound

    return best_entries, detected_total, known_streak, upper_bound


def fetch_playlist_batch(
    use_recent_incremental_scan,
    has_fetched_playlist_this_run,
    existing_ids,
    excluded_ids,
    *,
    url,
    author,
    known_ids_stop_threshold,
    ydl_opts_list,
    playlist_fetch_timeout_seconds,
    playlist_fetch_max_total_seconds,
    cyan,
    yellow,
    reset,
    scan_recent_entries_until_known_ids_fn,
    extract_playlist_with_hard_timeout_fn,
):
    """Recupere les entrees playlist selon la strategie active (incremental/complet)."""
    started_at = time.time()
    if use_recent_incremental_scan and not has_fetched_playlist_this_run:
        print(
            f"{cyan}Connexion a YouTube (mode incremental): scan des entrees recentes jusqu'a {known_ids_stop_threshold} IDs deja connus...{reset}",
            flush=False,
        )
        (
            recent_entries,
            recent_total_videos,
            known_streak,
            scanned_limit,
        ) = scan_recent_entries_until_known_ids_fn(
            url,
            existing_ids,
            excluded_ids,
            known_ids_target=known_ids_stop_threshold,
        )
        has_fetched_playlist_this_run = True

        if (
            isinstance(recent_entries, list)
            and known_streak >= known_ids_stop_threshold
        ):
            entries = recent_entries
            total_videos = recent_total_videos
            print(
                f"{cyan}Mode incremental valide: {known_streak} IDs connus consecutifs retrouves dans les {len(entries)} premieres entrees (borne {scanned_limit}).{reset}"
            )
        else:
            print(
                f"{yellow}Mode incremental insuffisant ({known_streak}/{known_ids_stop_threshold} IDs connus consecutifs, borne {scanned_limit}) : bascule en scan complet.{reset}"
            )
            use_recent_incremental_scan = False
            print(
                f"{cyan}Connexion a YouTube pour recuperer la playlist complete ({author})...{reset}",
                flush=False,
            )
            playlist_infos = extract_playlist_with_hard_timeout_fn(
                url,
                ydl_opts_list,
                playlist_fetch_timeout_seconds,
                playlist_fetch_max_total_seconds,
            )
            if isinstance(playlist_infos, dict):
                entries = playlist_infos.get("entries", [])
                total_videos = playlist_infos.get("playlist_count")
            else:
                entries = []
                total_videos = None
    else:
        print(
            f"{cyan}Connexion a YouTube pour recuperer la playlist ({author})...{reset}",
            flush=False,
        )
        playlist_infos = extract_playlist_with_hard_timeout_fn(
            url,
            ydl_opts_list,
            playlist_fetch_timeout_seconds,
            playlist_fetch_max_total_seconds,
        )
        has_fetched_playlist_this_run = True
        if isinstance(playlist_infos, dict):
            entries = playlist_infos.get("entries", [])
            total_videos = playlist_infos.get("playlist_count")
        else:
            entries = []
            total_videos = None

    elapsed = round(time.time() - started_at, 1)
    print(f"{cyan}Playlist recuperee en {elapsed}s.{reset}", flush=True)
    return (
        entries,
        total_videos,
        has_fetched_playlist_this_run,
        use_recent_incremental_scan,
    )


def resolve_total_playlist_from_batch(
    total_videos,
    entries,
    previous_total_playlist,
    total_playlist_drop_guard_ratio,
    yellow,
    reset,
):
    """Calcule total_playlist a partir du batch courant avec garde-fou de baisse."""
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
                drop_ratio > total_playlist_drop_guard_ratio
                and not detected_matches_entries
            ):
                print(
                    f"{yellow}Protection total_playlist: nouveau total detecte {detected_total_playlist} inferieur de {drop_ratio * 100:.2f}% a l'ancien {previous_total_playlist}. Ancienne valeur conservee dans le JSON.{reset}"
                )
                total_playlist = previous_total_playlist
        return total_playlist

    return previous_total_playlist if isinstance(previous_total_playlist, int) else None


def remove_stale_excluded_ids(excluded_ids, playlist_ids, yellow, reset):
    """Retire les IDs exclus absents de la playlist courante."""
    if not excluded_ids:
        return

    playlist_id_set = set(playlist_ids)
    stale_excluded_ids = {
        video_id for video_id in excluded_ids if video_id not in playlist_id_set
    }
    if stale_excluded_ids:
        excluded_ids.difference_update(stale_excluded_ids)
        print(
            f"{yellow}{len(stale_excluded_ids)} ID(s) exclus obsoletes retires (absents de la playlist courante).{reset}"
        )


def handle_no_missing_ids_case(
    effective_total,
    videos,
    total_playlist,
    playlist_ids,
    current_excluded_count,
    persisted_excluded_count,
    yellow,
    reset,
):
    """Gere le cas sans IDs manquants et retourne (break_loop, persisted_excluded_count)."""
    if isinstance(effective_total, int) and len(videos) < effective_total:
        hidden_count_from_playlist = 0
        if isinstance(total_playlist, int) and total_playlist > 0:
            hidden_count_from_playlist = max(0, total_playlist - len(playlist_ids))

        if (
            hidden_count_from_playlist > 0
            and hidden_count_from_playlist > current_excluded_count
        ):
            persisted_excluded_count = hidden_count_from_playlist
            print(
                f"{yellow}Aucun ID manquant detecte mais {hidden_count_from_playlist} video(s) sont comptees par YouTube sans ID exploitable: excluded_count ajuste a {persisted_excluded_count}.{reset}"
            )
        print(
            f"{yellow}Aucun trou detecte sur les IDs remontes par yt-dlp, mais cache encore incomplet ({len(videos)}/{effective_total}). Etat conserve en partiel.{reset}"
        )
    else:
        print("Aucun trou detecte dans le cache pour les IDs connus de la playlist.")

    return True, persisted_excluded_count
