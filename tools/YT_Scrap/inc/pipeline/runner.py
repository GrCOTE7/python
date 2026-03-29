import inc.catalog.authors as auth
from inc.pipeline.manager import run_selected_authors


def default_selected_ids():
    ids = list(range(auth.nb_authors())[:3])

    for blocked_id in (3, 4, 9):
        if blocked_id in ids:
            ids.remove(blocked_id)
    return ids


def run_default():
    return run_selected_authors(default_selected_ids())


def _validate_author_ids(ids):
    max_id = auth.nb_authors() - 1
    validated = []
    for author_id in ids:
        if not isinstance(author_id, int):
            raise TypeError(f"ID invalide (type): {author_id!r}")
        if author_id < 0 or author_id > max_id:
            raise ValueError(f"ID hors bornes: {author_id} (attendu: 0..{max_id})")
        validated.append(author_id)
    return validated


def run_scrap(selection=None):
    """API unique d'execution.

    Usage:
    - run_scrap(1)
    - run_scrap(range(2))
    - run_scrap()
    """
    if selection is None:
        return run_default()

    if isinstance(selection, int):
        return run_selected_authors(_validate_author_ids([selection]))

    if isinstance(selection, (str, bytes)):
        raise TypeError("selection ne peut pas être une chaîne")

    try:
        return run_selected_authors(_validate_author_ids(list(selection)))
    except TypeError as exc:
        raise TypeError("selection doit être None, int, ou un iterable d'ids") from exc
