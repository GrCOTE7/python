import os
import time


def persist_intermediate_state(
    *,
    videos,
    total_playlist,
    persisted_excluded_count,
    excluded_ids,
    has_fetched_playlist_this_run,
    pause_on_rate_limit,
    write_result_fn,
    write_markdown_fn,
    merged_excluded_count_fn,
    compute_effective_total_fn,
    video_sort_key_fn,
    scraped_now,
    green,
    yellow,
    reset,
):
    """Persiste l'etat intermediaire avant pause et retourne le compteur exclu mis a jour."""
    persisted_excluded_count = write_result_fn(
        videos=sorted(videos, key=video_sort_key_fn, reverse=True),
        total_playlist=total_playlist,
        excluded_ids=excluded_ids,
        excluded_count=merged_excluded_count_fn(persisted_excluded_count, excluded_ids),
        cache_valid=has_fetched_playlist_this_run,
    )

    write_markdown_fn(
        sorted(videos, key=video_sort_key_fn, reverse=True),
        total_playlist=compute_effective_total_fn(
            total_playlist,
            merged_excluded_count_fn(persisted_excluded_count, excluded_ids),
        ),
    )

    print(f"{green}JSON intermediaire ecrit ({scraped_now} videos).{reset}")
    print(
        f"{yellow}Pause {pause_on_rate_limit}s avant reprise (scraped={scraped_now}, total={total_playlist})...{reset}"
    )
    time.sleep(pause_on_rate_limit)
    return persisted_excluded_count


def finalize_scrap_state(
    *,
    ida,
    author,
    videos,
    initial_video_count,
    persisted_excluded_count,
    excluded_ids,
    total_playlist,
    has_fetched_playlist_this_run,
    output_md_file,
    output_file,
    read_previous_counts_fn,
    write_result_fn,
    merged_excluded_count_fn,
    compute_effective_total_fn,
    has_markdown_state_changed_fn,
    write_markdown_fn,
    build_scrap_summary_row_fn,
    video_sort_key_fn,
    error_total,
    strong,
    green,
    yellow,
    reset,
):
    """Finalise JSON/Markdown, affiche le bilan, et retourne la ligne resume."""
    videos = sorted(videos, key=video_sort_key_fn, reverse=True)
    scraped = len(videos)
    current_excluded_count = merged_excluded_count_fn(
        persisted_excluded_count, excluded_ids
    )

    previous_scraped, previous_total_playlist, previous_excluded_count = (
        read_previous_counts_fn()
    )

    current_excluded_count = write_result_fn(
        videos=videos,
        total_playlist=total_playlist,
        excluded_ids=excluded_ids,
        excluded_count=current_excluded_count,
        cache_valid=has_fetched_playlist_this_run,
    )
    if not isinstance(current_excluded_count, int):
        current_excluded_count = merged_excluded_count_fn(
            persisted_excluded_count, excluded_ids
        )

    markdown_missing = not os.path.isfile(output_md_file)
    previous_effective_total = compute_effective_total_fn(
        previous_total_playlist, previous_excluded_count
    )
    current_effective_total = compute_effective_total_fn(
        total_playlist, current_excluded_count
    )
    markdown_state_changed = has_markdown_state_changed_fn(
        previous_scraped=previous_scraped,
        previous_effective_total=previous_effective_total,
        current_scraped=scraped,
        current_effective_total=current_effective_total,
    )

    if len(videos) != initial_video_count or markdown_missing or markdown_state_changed:
        bilan = write_markdown_fn(videos, total_playlist=current_effective_total)
        if markdown_missing and len(videos) == initial_video_count:
            print(f"{yellow}Markdown regenere car fichier absent.{reset}")
        elif markdown_state_changed and len(videos) == initial_video_count:
            print(
                f"{yellow}Markdown regenere car les compteurs finaux ont change (etat partiel/complet).{reset}"
            )
    else:
        bilan = "Markdown non regenere (aucun changement detecte)"
        print("Markdown non regenere (aucun changement detecte).")

    effective_total = current_effective_total
    status = (
        "complete"
        if isinstance(effective_total, int)
        and effective_total > 0
        and scraped >= effective_total
        else "partial"
    )

    print(f"{green}Fichier JSON ecrit: {output_file}{reset}")
    print(
        f"scraped={scraped}, total_playlist={total_playlist}, excluded={current_excluded_count}, effective_total={effective_total}, status={status}"
    )
    print(f"Erreurs cumulees (403/rate-limit) total toutes passes: {error_total}")
    print(f"Fin du scrap des videos de {strong}{author}{reset}\n{bilan}.")

    return build_scrap_summary_row_fn(ida, author, videos)
