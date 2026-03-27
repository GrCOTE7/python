from typing import TYPE_CHECKING, cast

import yt_dlp
from yt_dlp.utils import DownloadError

if TYPE_CHECKING:
    from yt_dlp.YoutubeDL import _Params


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
    ydl_opts_detail,
    yt_dlp_counted_error_logger_cls,
    extract_entry_video_id_fn,
    extract_youtube_id_fn,
    remember_excluded_id_fn,
    is_adult_restricted_error_fn,
    is_skippable_unavailable_error_fn,
    try_extract_video_detail_android_fn,
    build_video_payload_fn,
    build_unavailable_video_payload_fn,
    author,
    cyan,
    yellow,
    green,
    reset,
    strong,
):
    """Traite le detail des videos manquantes et met a jour les structures en place."""
    ydl_opts_detail_runtime = dict(ydl_opts_detail)
    detail_logger = yt_dlp_counted_error_logger_cls(error_tracker)
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

            current_id = extract_entry_video_id_fn(entry)

            if isinstance(current_id, str) and current_id in existing_ids:
                continue

            video_url = entry.get("url") or entry.get("webpage_url")
            if not video_url and isinstance(current_id, str) and current_id:
                video_url = f"https://www.youtube.com/watch?v={current_id}"
            if not video_url:
                continue

            print(
                f"{cyan}[progress] Video globale {strong}{idx} / {total_entries} - {round(100*idx/total_entries,1)} %{reset} {cyan}| Executees : {strong}{run_processed} ( {(run_processed) / missing_count * 100:.1f} % ) {reset}{error_tracker.progress_suffix()} | {strong}{author}{reset}"
            )

            try:
                video_detail = ydl_detail.extract_info(video_url, download=False)
            except DownloadError as exc:
                if is_adult_restricted_error_fn(exc) or is_skippable_unavailable_error_fn(exc):
                    if is_adult_restricted_error_fn(exc):
                        skipped_video_id = remember_excluded_id_fn(
                            excluded_ids, current_id, video_url
                        )
                        if skipped_video_id:
                            print(
                                f"{yellow}Video exclue du total (adult): {skipped_video_id}{reset}"
                            )
                    else:
                        skipped_video_id = (
                            current_id
                            if isinstance(current_id, str) and current_id
                            else extract_youtube_id_fn(video_url)
                        )
                        if skipped_video_id:
                            excluded_ids.discard(skipped_video_id)
                            if skipped_video_id not in existing_ids:
                                android_detail = try_extract_video_detail_android_fn(
                                    video_url, fallback_video_id=skipped_video_id
                                )
                                if isinstance(android_detail, dict):
                                    videos.append(build_video_payload_fn(android_detail))
                                    print(
                                        f"{green}Metadonnees recuperees via client Android: {skipped_video_id}{reset}"
                                    )
                                else:
                                    videos.append(
                                        build_unavailable_video_payload_fn(
                                            entry=entry,
                                            video_id=skipped_video_id,
                                            video_url=video_url,
                                        )
                                    )
                                    print(
                                        f"{yellow}Video indisponible ajoutee en fallback: {skipped_video_id}{reset}"
                                    )
                                existing_ids.add(skipped_video_id)
                                run_processed += 1
                            else:
                                print(
                                    f"{yellow}Video indisponible/private (deja connue): {skipped_video_id}{reset}"
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
                    else extract_youtube_id_fn(video_url)
                )
                if candidate_id:
                    if detail_logger.is_adult_candidate(candidate_id):
                        remember_excluded_id_fn(excluded_ids, candidate_id, video_url)
                        print(
                            f"{yellow}Video exclue du total (adult via logs): {candidate_id}{reset}"
                        )
                    else:
                        excluded_ids.discard(candidate_id)
                        if candidate_id not in existing_ids:
                            android_detail = try_extract_video_detail_android_fn(
                                video_url, fallback_video_id=candidate_id
                            )
                            if isinstance(android_detail, dict):
                                videos.append(build_video_payload_fn(android_detail))
                                print(
                                    f"{green}Metadonnees recuperees via client Android: {candidate_id}{reset}"
                                )
                            else:
                                videos.append(
                                    build_unavailable_video_payload_fn(
                                        entry=entry,
                                        video_id=candidate_id,
                                        video_url=video_url,
                                    )
                                )
                                print(
                                    f"{yellow}Video indisponible ajoutee en fallback: {candidate_id}{reset}"
                                )
                            existing_ids.add(candidate_id)
                            run_processed += 1
                        else:
                            print(
                                f"{yellow}Video non exploitable ignoree (deja connue): {candidate_id}{reset}"
                            )
                else:
                    print(
                        f"{yellow}Video non exploitable sans ID detectable: {video_url}{reset}"
                    )
                continue

            video = build_video_payload_fn(video_detail)
            video_id = video.get("id")
            if video_id in existing_ids:
                continue
            videos.append(video)
            if video_id:
                existing_ids.add(video_id)
                if video_id in excluded_ids:
                    excluded_ids.discard(video_id)
                    print(
                        f"{green}ID retire de excluded_ids apres revalidation reussie: {video_id}{reset}"
                    )
            run_processed += 1

    return run_processed
