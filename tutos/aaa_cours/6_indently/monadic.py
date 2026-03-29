import flet as ft
from pymox_kit import cls, end, CLIW

from dataclasses import dataclass
from typing import Callable, Protocol, cast


def monadic(): # OOP Monadic approach

    class Result[T, E](Protocol):

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]": ...
        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]": ...
        def unwrap_or[U](self, default: U) -> T | U: ...

    @dataclass(slots=True)
    class OK[T, E=str]:
        value: T

        # def __init__(self, value: T):
        #     self.value = value

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]":
            return OK(f(self.value))

        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
            return f(self.value)

        def unwrap_or[U](self, default: U) -> T | U:
            return self.value


    @dataclass(slots=True)
    class Err[T, E](Exception):
        error: E
        # def __init__(self, error: E):
        #     self.error = error

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]":
            return cast("Result[U, E]", self)

        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
            return cast("Result[U, E]", self)

        def unwrap_or[U](self, default: U) -> U:
            return default

    def parse_int(s: str) -> Result[int, str]:
        try:
            return OK(int(s))
        except ValueError:
            return Err[int, str](f"not an integer {s!r}")
    
    
    print("Ready.")
    return parse_int


def main()-> None:
    
    cls()
    print("Monadic")
    parse_int = monadic()
    print("parse_int('42'):", parse_int('42'))
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
