from __future__ import annotations

from collections.abc import Callable

import flet as ft

from . import core
from .core import RxInt  # noqa: F401


def _patch_control(target: ft.Control, source: ft.Control) -> None:
    # Minimal patching strategy for tutorial controls (e.g., Text.value).
    for attr in ("value", "text", "visible", "disabled"):
        if hasattr(target, attr) and hasattr(source, attr):
            setattr(target, attr, getattr(source, attr))


def obx(builder: Callable[[], ft.Control]) -> Callable[[], ft.Control]:
    dependencies: set[RxInt] = set()

    def refresh() -> None:
        rebuilt = builder()
        _patch_control(control, rebuilt)
        control.update()

    def collect_dependency(rx_value: RxInt) -> None:
        dependencies.add(rx_value)

    previous = core._active_collector
    core._active_collector = collect_dependency
    control = builder()
    core._active_collector = previous

    for dep in dependencies:
        dep._subscribe(refresh)

    return lambda: control
