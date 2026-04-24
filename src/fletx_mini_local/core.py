from __future__ import annotations

from collections.abc import Callable

Observer = Callable[[], None]
_active_collector: Callable[["RxInt"], None] | None = None


class RxInt:
    def __init__(self, value: int) -> None:
        self._value = value
        self._observers: set[Observer] = set()

    @property
    def value(self) -> int:
        if _active_collector is not None:
            _active_collector(self)
        return self._value

    def set(self, value: int) -> None:
        if value == self._value:
            return
        self._value = value
        for callback in tuple(self._observers):
            callback()

    def _subscribe(self, callback: Observer) -> None:
        self._observers.add(callback)

    def _unsubscribe(self, callback: Observer) -> None:
        self._observers.discard(callback)
