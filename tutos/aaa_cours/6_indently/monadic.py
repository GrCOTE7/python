import flet
from pymox_kit import cls, end

from dataclasses import dataclass
from typing import Callable, Protocol, cast


class Result[T, E](Protocol):

    def map[U](self, f: Callable[[T], U]) -> "Result[U, E]": ...
    def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]": ...
    def unwrap_or[U](self, default: U) -> T | U: ...


# monadic:  # OOP Monadic approach
#     Le nom monadic vient de “monade” en programmation fonctionnelle :
#
#     - Ok et Err encapsulent une valeur dans un contexte (succès ou erreur).
#     - map transforme la valeur seulement si on est en succès.
#     - bind enchaîne des opérations qui renvoient elles-mêmes un résultat du même type.
#     - En cas de Err, la chaîne se coupe automatiquement sans planter.
#
#     Donc ici, “monadic” veut dire : “on suit un style monadique pour propager les erreurs proprement”.


@dataclass(slots=True)
class Ok[T, E = str]:
    value: T

    def __str__(self) -> str:
        return f"value = {self.value}"

    def map[U](self, f: Callable[[T], U]) -> "Result[U, E]":
        return Ok(f(self.value))

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


def ensure_positive(n: int) -> Result[int, str]:
    if n < 0:
        return Err[int, str](f"number must be positive {n}")
    return Ok(n)


def main() -> None:

    cls()
    print("Monadic")
    # parse_int = monadic()
    print("parse_int('42'):", parse_int("42"))
    print("parse_int('a'):", parse_int("a"))

    r1: Result[int, str] = parse_int("42").map(lambda x: x + 12)
    print("r1 map" + " " * 7 + ":", r1)
    r2: Result[int, str] = parse_int("42").bind(lambda x: Ok(x * 2))
    print("r2 bind" + " " * 6 + ":", r2)
    r3: int | str = parse_int("42").unwrap_or("default")
    print("r3 unwrap_or :", r3)
    r4: int | str = (
        parse_int("42")
        .map(lambda x: x + 1)
        .bind(lambda x: Ok(x * 2))
        .unwrap_or("default")
    )
    print("r4 unwrap_or :", r4)
    r5: int | str = parse_int("a").map(lambda x: x + 1).unwrap_or("default err")
    print("r5 unwrap_or :", r5)

    r6: Result[int, str] = parse_int("-5").bind(ensure_positive)
    print("r6 bind (err):", r6)
    r7: Result[int, str] = parse_int("7").bind(ensure_positive)
    print("r7 bind (ok) :", r7)


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
