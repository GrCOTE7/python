import os


def try_return_valid_ttl_cache(
    *,
    ida,
    output_file,
    output_md_file,
    cache_ttl,
    author,
    cyan,
    yellow,
    reset,
    get_valid_cache_entry_fn,
    read_previous_counts_fn,
    compute_cache_completion_fn,
    video_sort_key_fn,
    format_remaining_time_fr_fn,
    write_markdown_fn,
    build_scrap_summary_row_fn,
):
    """Retourne un resume immediat si le cache TTL est valide et complet."""
    cache_entry = get_valid_cache_entry_fn(output_file, cache_ttl)
    if cache_entry is None:
        return None

    cached_videos = cache_entry.get("videos")
    cache_date = cache_entry.get("timestamp_fr")
    remaining_minutes = cache_entry.get("remaining_minutes")
    scraped, total_playlist, excluded_count = read_previous_counts_fn()
    effective_total, cache_is_complete = compute_cache_completion_fn(
        scraped=scraped,
        total_playlist=total_playlist,
        excluded_count=excluded_count,
    )

    if (
        isinstance(scraped, int)
        and isinstance(total_playlist, int)
        and not cache_is_complete
    ):
        print(
            f"Cache valide mais incomplet ({scraped}/{effective_total}) : reprise du scraping pour combler les trous."
        )

    if not isinstance(cached_videos, list):
        return None

    cached_videos = sorted(cached_videos, key=video_sort_key_fn, reverse=True)
    if not cache_is_complete:
        return None

    ttl_minutes = max(1, (cache_ttl + 59) // 60)
    ttl_txt = format_remaining_time_fr_fn(ttl_minutes)
    print(f"Donnees chargees depuis le cache JSON (valide {ttl_txt}).")
    if cache_date and isinstance(remaining_minutes, int):
        remaining_txt = format_remaining_time_fr_fn(remaining_minutes)
        print(
            f"Derniere mise a jour: {cache_date} (prochaine actualisation dans environ {cyan}{remaining_txt}{reset})."
        )
    if os.path.isfile(output_md_file):
        print("Markdown non regenere (cache TTL valide).")
    else:
        write_markdown_fn(cached_videos, total_playlist=effective_total)
        print(f"{yellow}Markdown regenere car fichier absent (cache TTL valide).{reset}")

    return build_scrap_summary_row_fn(ida, author, cached_videos)


def decide_post_ttl_strategy(
    *,
    ida,
    videos,
    excluded_ids,
    total_playlist,
    persisted_excluded_count,
    url,
    author,
    output_md_file,
    cyan,
    green,
    yellow,
    reset,
    compute_effective_total_fn,
    is_scrap_complete_fn,
    probe_latest_playlist_video_id_fn,
    write_result_fn,
    merged_excluded_count_fn,
    has_markdown_state_changed_fn,
    write_markdown_fn,
    build_scrap_summary_row_fn,
    video_sort_key_fn,
):
    """Decide la strategie post-TTL: retour immediat, incremental, ou complet."""
    initial_video_count = len(videos)
    previous_total_playlist = total_playlist
    latest_cached_video_id = (
        videos[0].get("id")
        if videos
        and isinstance(videos[0], dict)
        and isinstance(videos[0].get("id"), str)
        and videos[0].get("id")
        else None
    )
    previous_effective_total = compute_effective_total_fn(
        total_playlist, persisted_excluded_count
    )
    previous_cache_is_complete = is_scrap_complete_fn(
        initial_video_count, previous_effective_total
    )

    use_recent_incremental_scan = False
    if previous_cache_is_complete:
        print(
            f"{cyan}Cache TTL expire: verification ultra-legere du dernier ID publie...{reset}"
        )
        probed_latest_video_id = probe_latest_playlist_video_id_fn(url)
        if (
            isinstance(probed_latest_video_id, str)
            and isinstance(latest_cached_video_id, str)
            and probed_latest_video_id == latest_cached_video_id
        ):
            print(
                f"{green}Dernier ID inchange ({probed_latest_video_id}) : cache conserve, scraping detaille ignore.{reset}"
            )
            sorted_videos = sorted(videos, key=video_sort_key_fn, reverse=True)
            current_excluded_count = write_result_fn(
                videos=sorted_videos,
                total_playlist=total_playlist,
                excluded_ids=excluded_ids,
                excluded_count=merged_excluded_count_fn(
                    persisted_excluded_count, excluded_ids
                ),
                cache_valid=True,
            )
            if not isinstance(current_excluded_count, int):
                current_excluded_count = merged_excluded_count_fn(
                    persisted_excluded_count, excluded_ids
                )

            current_effective_total = compute_effective_total_fn(
                total_playlist, current_excluded_count
            )
            markdown_should_refresh = has_markdown_state_changed_fn(
                previous_scraped=initial_video_count,
                previous_effective_total=previous_effective_total,
                current_scraped=len(sorted_videos),
                current_effective_total=current_effective_total,
            )

            if os.path.isfile(output_md_file) and not markdown_should_refresh:
                print("Markdown non regenere (cache prolonge apres verification du total).")
            else:
                write_markdown_fn(sorted_videos, total_playlist=current_effective_total)
                print(
                    f"{yellow}Markdown regenere (cache prolonge, fichier absent ou compteurs modifies).{reset}"
                )
            return {
                "early_summary": build_scrap_summary_row_fn(ida, author, sorted_videos),
                "use_recent_incremental_scan": False,
                "previous_total_playlist": previous_total_playlist,
            }

        if isinstance(probed_latest_video_id, str) and isinstance(
            latest_cached_video_id, str
        ):
            print(
                f"{yellow}Dernier ID change ({latest_cached_video_id} -> {probed_latest_video_id}) : scraping detaille necessaire.{reset}"
            )
            use_recent_incremental_scan = True
        else:
            print(f"{yellow}Probe ID non concluant: poursuite du scraping detaille.{reset}")

    return {
        "early_summary": None,
        "use_recent_incremental_scan": use_recent_incremental_scan,
        "previous_total_playlist": previous_total_playlist,
    }
