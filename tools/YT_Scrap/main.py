from inc.runner import run_scrap
import inc.authors as auth
import argparse


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
        
    selection = 0,1,6
    selection = 0, 6
    run_scrap(selection)
