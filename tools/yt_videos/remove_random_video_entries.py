import argparse
import json
import random
from pathlib import Path


def remove_one_random_video_from_file(json_path: Path, rng: random.Random, create_backup: bool) -> str:
    try:
        content = json_path.read_text(encoding="utf-8")
        payload = json.loads(content)
    except Exception as exc:
        return f"[ERREUR] {json_path.name}: lecture JSON impossible ({exc})"

    videos = payload.get("videos") if isinstance(payload, dict) else None
    if not isinstance(videos, list):
        return f"[IGNORE] {json_path.name}: champ 'videos' absent ou invalide"

    if len(videos) == 0:
        return f"[IGNORE] {json_path.name}: champ 'videos' vide"

    removed_index = rng.randrange(len(videos))
    removed_video = videos.pop(removed_index)

    if create_backup:
        backup_path = json_path.with_suffix(json_path.suffix + ".bak")
        backup_path.write_text(content, encoding="utf-8")

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    removed_id = removed_video.get("id") if isinstance(removed_video, dict) else None
    removed_title = removed_video.get("titre") if isinstance(removed_video, dict) else None
    details = []
    if removed_id:
        details.append(f"id={removed_id}")
    if removed_title:
        details.append(f"titre={removed_title}")
    details_txt = ", ".join(details) if details else "sans métadonnée"

    return (
        f"[OK] {json_path.name}: entrée supprimée à l'index {removed_index} "
        f"({details_txt}), vidéos restantes={len(videos)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Supprime 1 vidéo aléatoire du champ 'videos' de chaque fichier .json d'un dossier cache."
        )
    )
    parser.add_argument(
        "--cache-dir",
        default=str(Path(__file__).resolve().parent / "cache"),
        help="Dossier contenant les fichiers .json (défaut: dossier cache adjacent au script)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Seed random pour reproduire les mêmes suppressions",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Crée un fichier .bak avant modification",
    )

    args = parser.parse_args()
    cache_dir = Path(args.cache_dir)

    if not cache_dir.exists() or not cache_dir.is_dir():
        raise SystemExit(f"Dossier invalide: {cache_dir}")

    rng = random.Random(args.seed)

    json_files = sorted(cache_dir.glob("*.json"))
    if not json_files:
        print(f"Aucun fichier .json trouvé dans {cache_dir}")
        return

    print(f"Dossier cache: {cache_dir}")
    print(f"Fichiers JSON détectés: {len(json_files)}")

    ok_count = 0
    ignored_count = 0
    error_count = 0

    for json_file in json_files:
        result = remove_one_random_video_from_file(json_file, rng, args.backup)
        print(result)
        if result.startswith("[OK]"):
            ok_count += 1
        elif result.startswith("[IGNORE]"):
            ignored_count += 1
        else:
            error_count += 1

    print("-" * 72)
    print(
        f"Terminé. Modifiés={ok_count}, ignorés={ignored_count}, erreurs={error_count}, total={len(json_files)}"
    )


if __name__ == "__main__":
    main()
