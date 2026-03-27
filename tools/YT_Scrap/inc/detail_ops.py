from typing import TYPE_CHECKING, cast
from dataclasses import dataclass
from typing import Any, Callable

import yt_dlp
from yt_dlp.utils import DownloadError

if TYPE_CHECKING:
    from yt_dlp.YoutubeDL import _Params


@dataclass
class DetailOpsContext:
    ydl_opts_detail: Any
    yt_dlp_counted_error_logger_cls: Callable[..., Any]
    extract_entry_video_id_fn: Callable[..., Any]
    extract_youtube_id_fn: Callable[..., Any]
    remember_excluded_id_fn: Callable[..., Any]
    is_adult_restricted_error_fn: Callable[..., Any]
    is_skippable_unavailable_error_fn: Callable[..., Any]
    try_extract_video_detail_android_fn: Callable[..., Any]
    build_video_payload_fn: Callable[..., Any]
    build_unavailable_video_payload_fn: Callable[..., Any]
    author: str
    cyan: str
    yellow: str
    green: str
    reset: str
    strong: str


def process_missing_entries_detailed(
    *,
    entries,
    missing_in_cache,
    existing_ids,
    excluded_ids,
    videos,
    error_tracker,
    on_threshold_pause,
    handle_exception,
    ctx: DetailOpsContext,
):
    """Traite le detail des videos manquantes et met a jour les structures en place."""
    ydl_opts_detail_runtime = dict(ctx.ydl_opts_detail)
    detail_logger = ctx.yt_dlp_counted_error_logger_cls(error_tracker)
    ydl_opts_detail_runtime["logger"] = detail_logger

    total_entries = len(entries)
    run_processed = 0

    with yt_dlp.YoutubeDL(cast("_Params", ydl_opts_detail_runtime)) as ydl_detail:
        missing_count = max(1, len(missing_in_cache))
        for idx, entry in enumerate(entries, start=1):
            if error_tracker.stop_requested:
                on_threshold_pause()
                break

            if not isinstance(entry, dict):
                continue

            current_id = ctx.extract_entry_video_id_fn(entry)

            if isinstance(current_id, str) and current_id in existing_ids:
                continue

            video_url = entry.get("url") or entry.get("webpage_url")
            if not video_url and isinstance(current_id, str) and current_id:
                video_url = f"https://www.youtube.com/watch?v={current_id}"
            if not video_url:
                continue

            print(
                f"{ctx.cyan}[progress] Video globale {ctx.strong}{idx} / {total_entries} - {round(100*idx/total_entries,1)} %{ctx.reset} {ctx.cyan}| Executees : {ctx.strong}{run_processed} ( {(run_processed) / missing_count * 100:.1f} % ) {ctx.reset}{error_tracker.progress_suffix()} | {ctx.strong}{ctx.author}{ctx.reset}"
            )

            try:
                video_detail = ydl_detail.extract_info(video_url, download=False)
            except DownloadError as exc:
                if ctx.is_adult_restricted_error_fn(exc) or ctx.is_skippable_unavailable_error_fn(exc):
                    if ctx.is_adult_restricted_error_fn(exc):
                        skipped_video_id = ctx.remember_excluded_id_fn(
                            excluded_ids, current_id, video_url
                        )
                        if skipped_video_id:
                            print(
                                f"{ctx.yellow}Video exclue du total (adult): {skipped_video_id}{ctx.reset}"
                            )
                    else:
                        skipped_video_id = (
                            current_id
                            if isinstance(current_id, str) and current_id
                            else ctx.extract_youtube_id_fn(video_url)
                        )
                        if skipped_video_id:
                            excluded_ids.discard(skipped_video_id)
                            if skipped_video_id not in existing_ids:
                                android_detail = ctx.try_extract_video_detail_android_fn(
                                    video_url, fallback_video_id=skipped_video_id
                                )
                                if isinstance(android_detail, dict):
                                    videos.append(ctx.build_video_payload_fn(android_detail))
                                    print(
                                        f"{ctx.green}Metadonnees recuperees via client Android: {skipped_video_id}{ctx.reset}"
                                    )
                                else:
                                    videos.append(
                                        ctx.build_unavailable_video_payload_fn(
                                            entry=entry,
                                            video_id=skipped_video_id,
                                            video_url=video_url,
                                        )
                                    )
                                    print(
                                        f"{ctx.yellow}Video indisponible ajoutee en fallback: {skipped_video_id}{ctx.reset}"
                                    )
                                existing_ids.add(skipped_video_id)
                                run_processed += 1
                            else:
                                print(
                                    f"{ctx.yellow}Video indisponible/private (deja connue): {skipped_video_id}{ctx.reset}"
                                )
                    continue
                if handle_exception(exc, video_url, "Erreur yt-dlp ignoree sur"):
                    break
                continue
            except Exception as exc:
                if handle_exception(exc, video_url, "Erreur lors du detail pour"):
                    break
                continue

            if error_tracker.stop_requested:
                on_threshold_pause()
                break

            if not isinstance(video_detail, dict):
                candidate_id = (
                    current_id
                    if isinstance(current_id, str) and current_id
                    else ctx.extract_youtube_id_fn(video_url)
                )
                if candidate_id:
                    if detail_logger.is_adult_candidate(candidate_id):
                        ctx.remember_excluded_id_fn(excluded_ids, candidate_id, video_url)
                        print(
                            f"{ctx.yellow}Video exclue du total (adult via logs): {candidate_id}{ctx.reset}"
                        )
                    else:
                        excluded_ids.discard(candidate_id)
                        if candidate_id not in existing_ids:
                            android_detail = ctx.try_extract_video_detail_android_fn(
                                video_url, fallback_video_id=candidate_id
                            )
                            if isinstance(android_detail, dict):
                                videos.append(ctx.build_video_payload_fn(android_detail))
                                print(
                                    f"{ctx.green}Metadonnees recuperees via client Android: {candidate_id}{ctx.reset}"
                                )
                            else:
                                videos.append(
                                    ctx.build_unavailable_video_payload_fn(
                                        entry=entry,
                                        video_id=candidate_id,
                                        video_url=video_url,
                                    )
                                )
                                print(
                                    f"{ctx.yellow}Video indisponible ajoutee en fallback: {candidate_id}{ctx.reset}"
                                )
                            existing_ids.add(candidate_id)
                            run_processed += 1
                        else:
                            print(
                                f"{ctx.yellow}Video non exploitable ignoree (deja connue): {candidate_id}{ctx.reset}"
                            )
                else:
                    print(
                        f"{ctx.yellow}Video non exploitable sans ID detectable: {video_url}{ctx.reset}"
                    )
                continue

            video = ctx.build_video_payload_fn(video_detail)
            video_id = video.get("id")
            if video_id in existing_ids:
                continue
            videos.append(video)
            if video_id:
                existing_ids.add(video_id)
                if video_id in excluded_ids:
                    excluded_ids.discard(video_id)
                    print(
                        f"{ctx.green}ID retire de excluded_ids apres revalidation reussie: {video_id}{ctx.reset}"
                    )
            run_processed += 1

    return run_processed
