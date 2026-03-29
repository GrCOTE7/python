from inc.pipeline.runner import run_scrap
import inc.catalog.authors as auth
import argparse
from pathlib import Path

from inc.reporting.build_bpl import (
    TARGET_AUTHORS,
    build_bpl,
    get_default_target_scrape_ids,
    import_states_into_tracking,
)


# Override local de dev (None = desactive, ex: 0, "1", [14, 17, 11], "range:5", "all").
# DEV_SELECTION = 0, 1
# DEV_SELECTION = 14, 17, 11, 1 ,2
DEV_SELECTION = None # To obtain heart list


def parse_selection(raw_selection):
    if raw_selection is None or raw_selection.lower() == "default":
        return None

    if raw_selection.lower() == "all":
        return range(auth.nb_authors())

    if raw_selection.startswith("range:"):
        upper = int(raw_selection.split(":", 1)[1])
        return range(upper)

    if "," in raw_selection:
        return [int(item.strip()) for item in raw_selection.split(",") if item.strip()]

    return int(raw_selection)


def resolve_selection(raw_selection):
    if raw_selection is None:
        return None

    if isinstance(raw_selection, (int, range, list, tuple, set)):
        return raw_selection

    if isinstance(raw_selection, str):
        return parse_selection(raw_selection)

    raise ValueError(f"type de selection non supporte: {type(raw_selection).__name__}")


def _normalize_selection_ids(selection):
    if isinstance(selection, range):
        return list(selection)
    if isinstance(selection, int):
        return [selection]
    if isinstance(selection, (list, tuple, set)):
        return [item for item in selection if isinstance(item, int)]
    return []


def _build_targets_for_explicit_selection(selection):
    selected_ids = _normalize_selection_ids(selection)
    if not selected_ids:
        return TARGET_AUTHORS

    core_by_id = {
        item["scrap_id"]: item
        for item in TARGET_AUTHORS
        if isinstance(item.get("scrap_id"), int)
    }

    targets = []
    seen = set()
    for scrap_id in selected_ids:
        if scrap_id in seen:
            continue
        seen.add(scrap_id)

        if scrap_id in core_by_id:
            targets.append(core_by_id[scrap_id])
            continue

        author_name = auth.get_author_name(scrap_id)
        targets.append(
            {
                "author": author_name,
                "label": "Auteur",
                "scrap_id": scrap_id,
            }
        )

    return targets if targets else TARGET_AUTHORS


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lance le scraper YouTube.")
    parser.add_argument(
        "--selection",
        type=str,
        default="default",
        help="Ex: default | 1 | 0,2,5 | range:2 | all",
    )
    args = parser.parse_args()

    raw_selection = DEV_SELECTION if DEV_SELECTION is not None else args.selection

    try:
        user_selection = resolve_selection(raw_selection)
    except Exception as exc:
        parser.error(f"selection invalide: {exc}")

    if user_selection is None:
        # Par defaut, on scrape la liste coeur (7 IDs).
        effective_selection = get_default_target_scrape_ids()
        bpl_targets = TARGET_AUTHORS
    else:
        effective_selection = user_selection
        bpl_targets = _build_targets_for_explicit_selection(effective_selection)

    script_dir = Path(__file__).resolve().parent
    db_path = script_dir / "cache" / "tracking.sqlite3"
    bpl_path = script_dir.parent.parent / "BPL.md"

    # Synchronise d'abord les coches BPL vers le tracking.
    # Ainsi, le tableau CLI de run_scrap utilise l'etat le plus recent.
    pre_seen, pre_unseen, pre_ignored = import_states_into_tracking(
        db_path=db_path,
        bpl_path=bpl_path,
    )

    run_scrap(effective_selection)

    updated_seen, updated_unseen, ignored_not_found = import_states_into_tracking(
        db_path=db_path,
        bpl_path=bpl_path,
    )
    write_info = build_bpl(db_path=db_path, bpl_path=bpl_path, targets=bpl_targets)
    print(
        "BPL genere "
        f"(pre_sync seen={pre_seen}, unseen={pre_unseen}, ids_hors_db={pre_ignored}) "
        f"(seen_sync={updated_seen}, unseen_sync={updated_unseen}, ids_hors_db={ignored_not_found}) "
        f"-> {bpl_path} | write={write_info.get('written')} | reason={write_info.get('reason')}"
    )
