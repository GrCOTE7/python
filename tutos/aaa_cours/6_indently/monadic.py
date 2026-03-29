import flet as ft
from pymox_kit import cls, end, CLIW

from dataclasses import dataclass
from typing import Callable, Protocol


def monadic():

    class Result[T, E](Protocol):

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]": ...
        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]": ...
        def unwrap_or[U](self, default: U) -> T | U: ...

    @dataclass(slots=True)
    class OK[T, E=str]:
        value: T

        def __init__(self, value: T):
            self.value = value

        def map[U](self, f: Callable[[T], U]) -> "Result[U, E]":
            return OK(f(self.value))

        def bind[U](self, f: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
            return f(self.value)

        def unwrap_or[U](self, default: U) -> T | U:
            return self.value

    print("Ready.")


def main():
    
    cls()
    print("Monadic")
    monadic()
    pass


if __name__ == "__main__":

    cls()
    main()
    end()
