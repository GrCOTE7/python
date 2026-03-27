from inc.runner import run_scrap
import inc.authors as auth
import argparse
from pathlib import Path

from build_bpl import (
    TARGET_AUTHORS,
    build_bpl,
    get_default_target_scrape_ids,
    import_states_into_tracking,
)


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lance le scraper YouTube.")
    parser.add_argument(
        "--selection",
        type=str,
        default="default",
        help="Ex: default | 1 | 0,2,5 | range:2 | all",
    )
    args = parser.parse_args()

    try:
        selection = parse_selection(args.selection)
    except Exception as exc:
        parser.error(f"selection invalide: {exc}")

    if selection is None:
        # Par defaut, on scrape la selection BPL (les chaines suivies), pas la selection historique.
        selection = get_default_target_scrape_ids()

    run_scrap(selection)

    script_dir = Path(__file__).resolve().parent
    db_path = script_dir / "cache" / "tracking.sqlite3"
    bpl_path = script_dir.parent.parent / "BPL.md"

    updated_seen, updated_unseen, ignored_not_found = import_states_into_tracking(
        db_path=db_path,
        bpl_path=bpl_path,
    )
    write_info = build_bpl(db_path=db_path, bpl_path=bpl_path, targets=TARGET_AUTHORS)
    print(
        "BPL genere "
        f"(seen_sync={updated_seen}, unseen_sync={updated_unseen}, ids_hors_db={ignored_not_found}) "
        f"-> {bpl_path} | write={write_info.get('written')} | reason={write_info.get('reason')}"
    )
