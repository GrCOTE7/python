import os
import time
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class PersistOpsContext:
    pause_on_rate_limit: int
    output_md_file: str
    output_file: str
    write_result_fn: Callable[..., Any]
    write_markdown_fn: Callable[..., Any]
    merged_excluded_count_fn: Callable[..., Any]
    compute_effective_total_fn: Callable[..., Any]
    has_markdown_state_changed_fn: Callable[..., Any]
    read_previous_counts_fn: Callable[..., Any]
    build_scrap_summary_row_fn: Callable[..., Any]
    video_sort_key_fn: Callable[..., Any]
    strong: str
    green: str
    yellow: str
    reset: str


def persist_intermediate_state(
    *,
    videos,
    total_playlist,
    persisted_excluded_count,
    excluded_ids,
    has_fetched_playlist_this_run,
    scraped_now,
    ctx: PersistOpsContext,
):
    """Persiste l'etat intermediaire avant pause et retourne le compteur exclu mis a jour."""
    persisted_excluded_count = ctx.write_result_fn(
        videos=sorted(videos, key=ctx.video_sort_key_fn, reverse=True),
        total_playlist=total_playlist,
        excluded_ids=excluded_ids,
        excluded_count=ctx.merged_excluded_count_fn(
            persisted_excluded_count, excluded_ids
        ),
        cache_valid=has_fetched_playlist_this_run,
    )

    ctx.write_markdown_fn(
        sorted(videos, key=ctx.video_sort_key_fn, reverse=True),
        total_playlist=ctx.compute_effective_total_fn(
            total_playlist,
            ctx.merged_excluded_count_fn(persisted_excluded_count, excluded_ids),
        ),
    )

    print(f"{ctx.green}JSON intermediaire ecrit ({scraped_now} videos).{ctx.reset}")
    print(
        f"{ctx.yellow}Pause {ctx.pause_on_rate_limit}s avant reprise (scraped={scraped_now}, total={total_playlist})...{ctx.reset}"
    )
    time.sleep(ctx.pause_on_rate_limit)
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
    error_total,
    ctx: PersistOpsContext,
):
    """Finalise JSON/Markdown, affiche le bilan, et retourne la ligne resume."""
    videos = sorted(videos, key=ctx.video_sort_key_fn, reverse=True)
    scraped = len(videos)
    current_excluded_count = ctx.merged_excluded_count_fn(
        persisted_excluded_count, excluded_ids
    )

    previous_scraped, previous_total_playlist, previous_excluded_count = (
        ctx.read_previous_counts_fn()
    )

    current_excluded_count = ctx.write_result_fn(
        videos=videos,
        total_playlist=total_playlist,
        excluded_ids=excluded_ids,
        excluded_count=current_excluded_count,
        cache_valid=has_fetched_playlist_this_run,
    )
    if not isinstance(current_excluded_count, int):
        current_excluded_count = ctx.merged_excluded_count_fn(
            persisted_excluded_count, excluded_ids
        )

    markdown_missing = not os.path.isfile(ctx.output_md_file)
    previous_effective_total = ctx.compute_effective_total_fn(
        previous_total_playlist, previous_excluded_count
    )
    current_effective_total = ctx.compute_effective_total_fn(
        total_playlist, current_excluded_count
    )
    markdown_state_changed = ctx.has_markdown_state_changed_fn(
        previous_scraped=previous_scraped,
        previous_effective_total=previous_effective_total,
        current_scraped=scraped,
        current_effective_total=current_effective_total,
    )

    if len(videos) != initial_video_count or markdown_missing or markdown_state_changed:
        bilan = ctx.write_markdown_fn(videos, total_playlist=current_effective_total)
        if markdown_missing and len(videos) == initial_video_count:
            print(f"{ctx.yellow}Markdown regenere car fichier absent.{ctx.reset}")
        elif markdown_state_changed and len(videos) == initial_video_count:
            print(
                f"{ctx.yellow}Markdown regenere car les compteurs finaux ont change (etat partiel/complet).{ctx.reset}"
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

    print(f"{ctx.green}Fichier JSON ecrit: {ctx.output_file}{ctx.reset}")
    print(
        f"scraped={scraped}, total_playlist={total_playlist}, excluded={current_excluded_count}, effective_total={effective_total}, status={status}"
    )
    print(f"Erreurs cumulees (403/rate-limit) total toutes passes: {error_total}")
    print(f"Fin du scrap des videos de {ctx.strong}{author}{ctx.reset}\n{bilan}.")

    return ctx.build_scrap_summary_row_fn(ida, author, videos)
