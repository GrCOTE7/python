import flet
from pymox_kit import cls, end

from dataclasses import dataclass
from typing import Callable, Protocol, cast

# ❌ → 6:43


def monadic():  # OOP Monadic approach
    """_summary_
        Le nom monadic vient de “monade” en programmation fonctionnelle :

    - Ok et Err encapsulent une valeur dans un contexte (succès ou erreur).
    - map transforme la valeur seulement si on est en succès.
    - bind enchaîne des opérations qui renvoient elles-mêmes un résultat du même type.
    - En cas de Err, la chaîne se coupe automatiquement sans planter.
    Donc ici, “monadic” veut dire : “on suit un style monadique pour propager les erreurs proprement”.

    Returns:
            _type_: _description_
    """

    class Result[T, E](Protocol):

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]": ...
        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]": ...
        def unwrap_or[U](self, default: U) -> T | U: ...

    @dataclass(slots=True)
    class Ok[T, E = str]:
        value: T

        def __str__(self) -> str:
            return f"value = {self.value}"

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]":
            return OK(f(self.value))

        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
            return f(self.value)

        def unwrap_or[U](self, default: U) -> T | U:
            return self.value

    @dataclass(slots=True)
    class Err[T, E](Exception):
        error: E

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]":
            return cast("Result[U, E]", self)

        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
            return cast("Result[U, E]", self)

        def unwrap_or[U](self, default: U) -> U:
            return default

    def parse_int(s: str) -> Result[int, str]:
        try:
            return Ok(int(s))
        except ValueError:
            return Err[int, str](f"not an integer {s!r}")

    return parse_int


def main() -> None:

    cls()
    print("Monadic")
    parse_int = monadic()
    print("parse_int('42'):", parse_int("42"))
    print("parse_int('a'):", parse_int("a"))
    pass


if __name__ == "__main__":

    cls()
    main()
    end()

# Une opération renvoie soit un succès (OK(value)), soit une erreur (Err(error)).
# map applique une fonction seulement si on est en OK.
# bind enchaîne une fonction qui renvoie elle-même un Result.
# unwrap_or(default) donne la valeur si OK, sinon une valeur de secours.
# Intuition simple:

# Sans style monadique: plein de try/except ou if erreur: ... à chaque étape.
# Avec style monadique: tu “passes” le résultat d’étape en étape; si une étape est Err, le reste est court-circuité proprement.
# Mini lecture de ton cas:

# parse_int("42") -> OK(42)
# parse_int("abc") -> Err("not an integer 'abc'")
# Pourquoi c’est utile:

# Code plus lisible pour les pipelines de transformation.
# Gestion d’erreur uniforme.
# Moins de duplication de logique de contrôle.
