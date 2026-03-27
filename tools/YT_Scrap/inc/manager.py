import locale, os
import re
from typing import Optional
import inc.authors as auth
from inc import constants as cst
from inc import cache as cache_ops
from inc import flow_ops
from inc import init_ops
from inc import ttl_ops
from inc import detail_ops
from inc import persist_ops
from inc import helpers as hlp
from inc import video as vid
from inc import render as rnd

# Delegation vers sous-modules: simplifie la maintenance.
YDL_OPTS_LIST = cst.YDL_OPTS_LIST
YDL_OPTS_DETAIL = cst.YDL_OPTS_DETAIL
KNOWN_IDS_STOP_THRESHOLD = cst.KNOWN_IDS_STOP_THRESHOLD
RECENT_PLAYLIST_SCAN_STEP = cst.RECENT_PLAYLIST_SCAN_STEP
RECENT_PLAYLIST_SCAN_MAX = cst.RECENT_PLAYLIST_SCAN_MAX

is_counted_ytdlp_error = hlp.is_counted_ytdlp_error
is_adult_restricted_error = hlp.is_adult_restricted_error
is_skippable_unavailable_error = hlp.is_skippable_unavailable_error
extract_youtube_id = hlp.extract_youtube_id
extract_entry_video_id = hlp.extract_entry_video_id
remember_excluded_id = hlp.remember_excluded_id
CountedErrorTracker = hlp.CountedErrorTracker
YtDlpCountedErrorLogger = hlp.YtDlpCountedErrorLogger

timestamp2fr = vid.timestamp2fr
timestamp_fr_to_epoch = vid.timestamp_fr_to_epoch
build_video_payload = vid.build_video_payload
build_unavailable_video_payload = vid.build_unavailable_video_payload
try_extract_video_detail_android = vid.try_extract_video_detail_android
video_sort_key = vid.video_sort_key
format_remaining_time_fr = vid.format_remaining_time_fr
compute_effective_total = vid.compute_effective_total
is_scrap_complete = vid.is_scrap_complete

# Variables runtime initialisees par ini().
AUTHOR = ""
URL = ""
SCRIPT_DIR = ""
STORAGE_DIR = ""
OUTPUT_FILE = ""
OUTPUT_MD_FILE = ""
CACHE_TTL = 0
MAX_CUMULATED_403_ERRORS = 0
PAUSE_ON_RATE_LIMIT = 0
MAX_STALL_RETRIES = 0
TOTAL_PLAYLIST_DROP_GUARD_RATIO = 0.0
PLAYLIST_FETCH_TIMEOUT_SECONDS = 0
PLAYLIST_FETCH_MAX_TOTAL_SECONDS = 0
get_valid_cache_entry = None


def write_markdown(videos, total_playlist=None):
    return rnd.write_markdown_file(
        videos=videos,
        total_playlist=total_playlist,
        author=AUTHOR,
        url=URL,
        storage_dir=STORAGE_DIR,
        output_md_file=OUTPUT_MD_FILE,
    )


build_scrap_summary_row = rnd.build_scrap_summary_row
print_scrap_summary_table = rnd.print_scrap_summary_table

# ❌ Compatibilité de PyMoX-Kit & locale avec Linux/Windows
try:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
except Exception:
    # Fallback non bloquant si la locale n'est pas disponible.
    pass

# try:
#     from pymox_kit import cls, end
# except Exception:
#     # Fallback minimal si pymox_kit échoue (ex: locale fr_FR absente).
#     def cls():
#         import subprocess

#         try:
#             subprocess.run(["clear"], check=False)
#         except Exception:
#             print("\033[2J\033[H", end="")

from pymox_kit import cls, end, SB, R, YELLOW, GREEN, RED, CYAN

try:
    from suivi.tracking_store import export_markdown as tracking_export_markdown
    from suivi.tracking_store import merge_scrape as tracking_merge_scrape
    from suivi.tracking_store import set_video_state as tracking_set_video_state

    TRACKING_ENABLED = True
except Exception:
    TRACKING_ENABLED = False

# ❌ Looker ce qui n'a pas été refait ici par rapport à to_see.py et del to_see


def ini(ida):
    init_ctx = init_ops.build_init_context(
        ida=ida,
        manager_file=__file__,
        get_author_name_fn=auth.get_author_name,
    )
    globals().update(init_ctx)


def _extract_markdown_states(md_file_path):
    if not isinstance(md_file_path, str) or not os.path.isfile(md_file_path):
        return [], []

    seen_ids = []
    unseen_ids = []

    with open(md_file_path, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if not (stripped.startswith("* [x]") or stripped.startswith("* [ ]")):
                continue

            match = re.search(r"(?:[?&]v=|youtu\.be/)([A-Za-z0-9_-]+)", stripped)
            if not match:
                continue

            video_id = match.group(1)
            if stripped.startswith("* [x]"):
                seen_ids.append(video_id)
            else:
                unseen_ids.append(video_id)

    return seen_ids, unseen_ids


def _sync_tracking_after_scrap(*, author, author_url, storage_dir, source_file, videos, seen_ids, unseen_ids):
    if not TRACKING_ENABLED:
        return None

    db_path = os.path.join(storage_dir, "tracking.sqlite3")
    output_tracking_md = os.path.join(storage_dir, f"{author}_YT.md")

    merge_result = tracking_merge_scrape(
        db_path=db_path,
        author=author,
        run_items=videos,
        source_file=source_file,
    )

    if seen_ids:
        tracking_set_video_state(
            db_path=db_path,
            video_ids=seen_ids,
            state="seen",
            source="md_import",
        )

    if unseen_ids:
        tracking_set_video_state(
            db_path=db_path,
            video_ids=unseen_ids,
            state="unseen",
            source="md_import",
        )

    summary = tracking_export_markdown(
        db_path=db_path,
        author=author,
        output_md_file=output_tracking_md,
        author_url=author_url,
    )

    return merge_result, summary


def probe_latest_playlist_video_id(url: str) -> Optional[str]:
    """Récupère l'ID de la vidéo la plus récente avec une requête ultra-légère."""
    probe_opts = dict(YDL_OPTS_LIST)
    probe_opts["playlist_items"] = "1"

    try:
        infos = flow_ops.extract_playlist_with_hard_timeout(
            url=url,
            ydl_opts=probe_opts,
            timeout_seconds=min(20, PLAYLIST_FETCH_TIMEOUT_SECONDS),
            max_total_seconds=min(60, PLAYLIST_FETCH_MAX_TOTAL_SECONDS),
            cyan=CYAN,
            reset=R,
        )
    except Exception:
        return None

    if not isinstance(infos, dict):
        return None

    entries = infos.get("entries")
    if isinstance(entries, list) and entries:
        latest_entry_id = extract_entry_video_id(entries[0])
        if isinstance(latest_entry_id, str) and latest_entry_id:
            return latest_entry_id

    return None


def scrap_some(ida):
    ini(ida)
    print(f"SCRAP des vidéos de {SB}{AUTHOR}{R}\n→ {URL}")
    pre_seen_ids, pre_unseen_ids = _extract_markdown_states(OUTPUT_MD_FILE)

    def write_result_runtime(
        videos, total_playlist, excluded_ids=None, excluded_count=None, cache_valid=True
    ):
        return cache_ops.write_result(
            output_file=OUTPUT_FILE,
            storage_dir=STORAGE_DIR,
            url=URL,
            timestamp2fr=timestamp2fr,
            videos=videos,
            total_playlist=total_playlist,
            excluded_ids=excluded_ids,
            excluded_count=excluded_count,
            cache_valid=cache_valid,
        )

    def read_previous_counts_runtime():
        return cache_ops.read_previous_counts(OUTPUT_FILE)

    def compute_cache_completion_runtime(scraped, total_playlist, excluded_count):
        return flow_ops.compute_cache_completion(
            scraped=scraped,
            total_playlist=total_playlist,
            excluded_count=excluded_count,
            compute_effective_total=compute_effective_total,
            is_scrap_complete=is_scrap_complete,
        )

    def has_markdown_state_changed_runtime(
        previous_scraped,
        previous_effective_total,
        current_scraped,
        current_effective_total,
    ):
        return flow_ops.has_markdown_state_changed(
            previous_scraped=previous_scraped,
            previous_effective_total=previous_effective_total,
            current_scraped=current_scraped,
            current_effective_total=current_effective_total,
            is_scrap_complete=is_scrap_complete,
        )

    def extract_playlist_with_timeout_runtime(
        url, ydl_opts, timeout_seconds, max_total_seconds=None
    ):
        return flow_ops.extract_playlist_with_hard_timeout(
            url=url,
            ydl_opts=ydl_opts,
            timeout_seconds=timeout_seconds,
            max_total_seconds=max_total_seconds,
            cyan=CYAN,
            reset=R,
        )

    def extract_playlist_ids_runtime(entries):
        return flow_ops.extract_playlist_ids(entries, extract_entry_video_id)

    def scan_recent_entries_until_known_ids_runtime(
        url, existing_ids, excluded_ids, known_ids_target
    ):
        return flow_ops.scan_recent_entries_until_known_ids(
            url=url,
            existing_ids=existing_ids,
            excluded_ids=excluded_ids,
            known_ids_target=known_ids_target,
            recent_playlist_scan_step=RECENT_PLAYLIST_SCAN_STEP,
            recent_playlist_scan_max=RECENT_PLAYLIST_SCAN_MAX,
            ydl_opts_list=YDL_OPTS_LIST,
            playlist_fetch_timeout_seconds=PLAYLIST_FETCH_TIMEOUT_SECONDS,
            playlist_fetch_max_total_seconds=PLAYLIST_FETCH_MAX_TOTAL_SECONDS,
            extract_playlist_with_hard_timeout_fn=extract_playlist_with_timeout_runtime,
            extract_playlist_ids_fn=extract_playlist_ids_runtime,
        )

    ttl_ctx = ttl_ops.TtlOpsContext(
        output_file=OUTPUT_FILE,
        output_md_file=OUTPUT_MD_FILE,
        cache_ttl=CACHE_TTL,
        author=AUTHOR,
        url=URL,
        cyan=CYAN,
        yellow=YELLOW,
        green=GREEN,
        reset=R,
        get_valid_cache_entry_fn=get_valid_cache_entry,
        read_previous_counts_fn=read_previous_counts_runtime,
        compute_cache_completion_fn=compute_cache_completion_runtime,
        video_sort_key_fn=video_sort_key,
        format_remaining_time_fr_fn=format_remaining_time_fr,
        write_markdown_fn=write_markdown,
        build_scrap_summary_row_fn=build_scrap_summary_row,
        compute_effective_total_fn=compute_effective_total,
        is_scrap_complete_fn=is_scrap_complete,
        probe_latest_playlist_video_id_fn=probe_latest_playlist_video_id,
        write_result_fn=write_result_runtime,
        merged_excluded_count_fn=flow_ops.merged_excluded_count,
        has_markdown_state_changed_fn=has_markdown_state_changed_runtime,
    )

    detail_ctx = detail_ops.DetailOpsContext(
        ydl_opts_detail=YDL_OPTS_DETAIL,
        yt_dlp_counted_error_logger_cls=YtDlpCountedErrorLogger,
        extract_entry_video_id_fn=extract_entry_video_id,
        extract_youtube_id_fn=extract_youtube_id,
        remember_excluded_id_fn=remember_excluded_id,
        is_adult_restricted_error_fn=is_adult_restricted_error,
        is_skippable_unavailable_error_fn=is_skippable_unavailable_error,
        try_extract_video_detail_android_fn=try_extract_video_detail_android,
        build_video_payload_fn=build_video_payload,
        build_unavailable_video_payload_fn=build_unavailable_video_payload,
        author=AUTHOR,
        cyan=CYAN,
        yellow=YELLOW,
        green=GREEN,
        reset=R,
        strong=SB,
    )

    persist_ctx = persist_ops.PersistOpsContext(
        pause_on_rate_limit=PAUSE_ON_RATE_LIMIT,
        output_md_file=OUTPUT_MD_FILE,
        output_file=OUTPUT_FILE,
        write_result_fn=write_result_runtime,
        write_markdown_fn=write_markdown,
        merged_excluded_count_fn=flow_ops.merged_excluded_count,
        compute_effective_total_fn=compute_effective_total,
        has_markdown_state_changed_fn=has_markdown_state_changed_runtime,
        read_previous_counts_fn=read_previous_counts_runtime,
        build_scrap_summary_row_fn=build_scrap_summary_row,
        video_sort_key_fn=video_sort_key,
        strong=SB,
        green=GREEN,
        yellow=YELLOW,
        reset=R,
    )

    restored_from = cache_ops.bootstrap_missing_cache_from_legacy(
        output_file=OUTPUT_FILE,
        storage_dir=STORAGE_DIR,
        author=AUTHOR,
    )
    if isinstance(restored_from, str):
        print(
            f"{CYAN}Cache principal absent: restauration depuis {os.path.basename(restored_from)}.{R}"
        )

    healed_fields = cache_ops.auto_heal_cache_invariants(
        OUTPUT_FILE,
        url=URL,
        timestamp2fr=timestamp2fr,
        timestamp_fr_to_epoch=timestamp_fr_to_epoch,
    )
    if healed_fields:
        print(
            f"{YELLOW}Auto-heal cache appliqué (invariants): {', '.join(healed_fields)}{R}"
        )

    ttl_summary = ttl_ops.try_return_valid_ttl_cache(ida=ida, ctx=ttl_ctx)
    if ttl_summary is not None:
        ttl_videos = cache_ops.read_previous_state(OUTPUT_FILE)
        tracking_result = _sync_tracking_after_scrap(
            author=AUTHOR,
            author_url=URL,
            storage_dir=STORAGE_DIR,
            source_file=OUTPUT_FILE,
            videos=ttl_videos,
            seen_ids=pre_seen_ids,
            unseen_ids=pre_unseen_ids,
        )
        if tracking_result is not None:
            merge_result, tracking_summary = tracking_result
            print(
                f"{CYAN}Tracking sync (TTL): run_id={merge_result.run_id} | seen={tracking_summary['seen_count']} | not_seen={tracking_summary['not_seen_count']} | md={tracking_summary['output']}{R}"
            )
        return ttl_summary

    videos = cache_ops.read_previous_state(OUTPUT_FILE)
    initial_video_count = len(videos)
    existing_ids = {
        v.get("id")
        for v in videos
        if isinstance(v, dict) and isinstance(v.get("id"), str) and v.get("id")
    }
    excluded_ids = cache_ops.read_previous_excluded_ids(OUTPUT_FILE)
    _, total_playlist, persisted_excluded_count = (
        cache_ops.read_previous_counts(OUTPUT_FILE)
    )  # récupère total connu pour la vérification de complétude
    persisted_excluded_count = (
        persisted_excluded_count if isinstance(persisted_excluded_count, int) else 0
    )
    post_ttl_strategy = ttl_ops.decide_post_ttl_strategy(
        ida=ida,
        videos=videos,
        excluded_ids=excluded_ids,
        total_playlist=total_playlist,
        persisted_excluded_count=persisted_excluded_count,
        ctx=ttl_ctx,
    )
    if post_ttl_strategy["early_summary"] is not None:
        tracking_result = _sync_tracking_after_scrap(
            author=AUTHOR,
            author_url=URL,
            storage_dir=STORAGE_DIR,
            source_file=OUTPUT_FILE,
            videos=videos,
            seen_ids=pre_seen_ids,
            unseen_ids=pre_unseen_ids,
        )
        if tracking_result is not None:
            merge_result, tracking_summary = tracking_result
            print(
                f"{CYAN}Tracking sync (early): run_id={merge_result.run_id} | seen={tracking_summary['seen_count']} | not_seen={tracking_summary['not_seen_count']} | md={tracking_summary['output']}{R}"
            )
        return post_ttl_strategy["early_summary"]
    use_recent_incremental_scan = post_ttl_strategy["use_recent_incremental_scan"]
    previous_total_playlist = post_ttl_strategy["previous_total_playlist"]

    error_tracker = CountedErrorTracker(MAX_CUMULATED_403_ERRORS)

    if videos:
        print(
            f"État précédent détecté. {CYAN}Vérification complète des IDs pour combler les trous{R}."
        )
    else:
        print("Aucun état précédent trouvé, démarrage depuis la première vidéo.")

    stall_retries = 0
    scraped_before_pass = len(videos)
    has_fetched_playlist_this_run = False

    def log_threshold_pause_message():
        print(
            f"{RED}Seuil d'erreurs 403/rate-limit atteint ({MAX_CUMULATED_403_ERRORS}). Pause {PAUSE_ON_RATE_LIMIT}s puis reprise...{R}"
        )

    def handle_detail_exception(exc, video_url, fallback_prefix):
        if is_adult_restricted_error(exc):
            return False

        if is_counted_ytdlp_error(exc):
            error_tracker.increment(str(exc), url=video_url, source="exception")
            if error_tracker.stop_requested:
                log_threshold_pause_message()
                return True
            return False

        print(f"{fallback_prefix} {video_url}: {exc}")
        return False

    while True:
        # ── Vérification complétude avant chaque passe ──────────────────────
        current_excluded_count = flow_ops.merged_excluded_count(
            persisted_excluded_count, excluded_ids
        )
        effective_total = compute_effective_total(
            total_playlist, current_excluded_count
        )
        if (
            has_fetched_playlist_this_run
            and isinstance(effective_total, int)
            and effective_total > 0
            and len(videos) >= effective_total
        ):
            break

        if (
            isinstance(effective_total, int)
            and effective_total > 0
            and len(videos) >= effective_total
        ):
            print(
                f"{CYAN}Cache local marqué complet ({len(videos)}/{effective_total}) : vérification YouTube en cours pour détecter d'éventuelles nouveautés...{R}"
            )

        try:
            (
                entries,
                total_videos,
                has_fetched_playlist_this_run,
                use_recent_incremental_scan,
            ) = flow_ops.fetch_playlist_batch(
                use_recent_incremental_scan=use_recent_incremental_scan,
                has_fetched_playlist_this_run=has_fetched_playlist_this_run,
                existing_ids=existing_ids,
                excluded_ids=excluded_ids,
                url=URL,
                author=AUTHOR,
                known_ids_stop_threshold=KNOWN_IDS_STOP_THRESHOLD,
                ydl_opts_list=YDL_OPTS_LIST,
                playlist_fetch_timeout_seconds=PLAYLIST_FETCH_TIMEOUT_SECONDS,
                playlist_fetch_max_total_seconds=PLAYLIST_FETCH_MAX_TOTAL_SECONDS,
                cyan=CYAN,
                yellow=YELLOW,
                reset=R,
                scan_recent_entries_until_known_ids_fn=scan_recent_entries_until_known_ids_runtime,
                extract_playlist_with_hard_timeout_fn=extract_playlist_with_timeout_runtime,
            )

            total_playlist = flow_ops.resolve_total_playlist_from_batch(
                total_videos=total_videos,
                entries=entries,
                previous_total_playlist=previous_total_playlist,
                total_playlist_drop_guard_ratio=TOTAL_PLAYLIST_DROP_GUARD_RATIO,
                yellow=YELLOW,
                reset=R,
            )

            total_videos_txt = (
                str(total_videos)
                if isinstance(total_videos, int)
                else f"Nombre inconnu (au moins {len(entries)}) de"
            )
            print(f"{RED}{total_videos_txt} vidéo(s){R} trouvée(s) dans la playlist.")
            playlist_ids = extract_playlist_ids_runtime(entries)
            # Déduplication stable: évite de retraiter deux fois le même ID.
            playlist_ids = list(dict.fromkeys(playlist_ids))
            flow_ops.remove_stale_excluded_ids(
                excluded_ids=excluded_ids,
                playlist_ids=playlist_ids,
                yellow=YELLOW,
                reset=R,
            )
            missing_in_cache = [
                video_id for video_id in playlist_ids if video_id not in existing_ids
            ]

            if missing_in_cache:
                print(
                    f"{YELLOW}{len(missing_in_cache)} vidéo(s) absente(s) du cache seront (re)téléchargées.{R}"
                )
            else:
                _, persisted_excluded_count = flow_ops.handle_no_missing_ids_case(
                    effective_total=effective_total,
                    videos=videos,
                    total_playlist=total_playlist,
                    playlist_ids=playlist_ids,
                    current_excluded_count=current_excluded_count,
                    persisted_excluded_count=persisted_excluded_count,
                    yellow=YELLOW,
                    reset=R,
                )
                break

            detail_ops.process_missing_entries_detailed(
                entries=entries,
                missing_in_cache=missing_in_cache,
                existing_ids=existing_ids,
                excluded_ids=excluded_ids,
                videos=videos,
                error_tracker=error_tracker,
                on_threshold_pause=log_threshold_pause_message,
                handle_exception=handle_detail_exception,
                ctx=detail_ctx,
            )

        except Exception as e:
            print(f"{RED}Scrap interrompu: {e}{R}", flush=True)
            print(
                f"{YELLOW}Conseil: vérifier la connexion/rate-limit YouTube, puis relancer. Timeout réseau: {YDL_OPTS_LIST.get('socket_timeout')}s/requête, timeout global playlist: {PLAYLIST_FETCH_TIMEOUT_SECONDS}s.{R}",
                flush=True,
            )

        # ── Fin de passe: décider si on continue, on pause, ou on abandonne ──
        scraped_now = len(videos)
        current_excluded_count = flow_ops.merged_excluded_count(
            persisted_excluded_count, excluded_ids
        )
        effective_total = compute_effective_total(
            total_playlist, current_excluded_count
        )
        still_incomplete = (
            isinstance(effective_total, int)
            and effective_total > 0
            and not is_scrap_complete(scraped_now, effective_total)
        )

        if not error_tracker.stop_requested and not still_incomplete:
            # Passe terminée normalement et cache cohérent: on sort.
            break

        # Détection de stall: pas de progression sur cette passe
        if scraped_now <= scraped_before_pass:
            stall_retries += 1
            print(
                f"{RED}Aucune progression détectée (passe #{stall_retries}/{MAX_STALL_RETRIES}).{R}"
            )
            if stall_retries >= MAX_STALL_RETRIES:
                print(
                    f"{RED}Abandon définitif après {MAX_STALL_RETRIES} passes sans progression.{R}"
                )
                break
        else:
            stall_retries = 0

        scraped_before_pass = scraped_now

        if not error_tracker.stop_requested and still_incomplete:
            print(
                f"{YELLOW}Cache encore incomplet ({scraped_now}/{effective_total}) après passe normale: nouvelle passe immédiate.{R}"
            )
            continue

        error_tracker.reset()
        persisted_excluded_count = persist_ops.persist_intermediate_state(
            videos=videos,
            total_playlist=total_playlist,
            persisted_excluded_count=persisted_excluded_count,
            excluded_ids=excluded_ids,
            has_fetched_playlist_this_run=has_fetched_playlist_this_run,
            scraped_now=scraped_now,
            ctx=persist_ctx,
        )

    summary_row = persist_ops.finalize_scrap_state(
        ida=ida,
        author=AUTHOR,
        videos=videos,
        initial_video_count=initial_video_count,
        persisted_excluded_count=persisted_excluded_count,
        excluded_ids=excluded_ids,
        total_playlist=total_playlist,
        has_fetched_playlist_this_run=has_fetched_playlist_this_run,
        error_total=error_tracker.total_count,
        ctx=persist_ctx,
    )

    tracking_result = _sync_tracking_after_scrap(
        author=AUTHOR,
        author_url=URL,
        storage_dir=STORAGE_DIR,
        source_file=OUTPUT_FILE,
        videos=videos,
        seen_ids=pre_seen_ids,
        unseen_ids=pre_unseen_ids,
    )
    if tracking_result is not None:
        merge_result, tracking_summary = tracking_result
        print(
            f"{CYAN}Tracking sync: run_id={merge_result.run_id} | seen={tracking_summary['seen_count']} | not_seen={tracking_summary['not_seen_count']} | md={tracking_summary['output']}{R}"
        )

    return summary_row


def run_selected_authors(selected_ids):
    cls()
    nb = auth.nb_authors()
    results = []
    ids = list(selected_ids)
    for rank, author_id in enumerate(ids, start=1):
        end()
        print(
            f"{SB}{author_id:> 3}{R} {SB}{rank:> 3}{R} / {nb:> 3} → {SB}{auth.AUTHORS[author_id]}{R}"
        )
        results.append(scrap_some(author_id))
    end()
    print_scrap_summary_table(results)
    end()
    return results
