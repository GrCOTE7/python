"""
lv02 — fletx 0.2.0 (vrai package)
Paradigme: Xstate (état partagé) + Xview (vue/page) + Xapp (routeur).
Différence vs lv01: plus de RxInt/obx; la réactivité est manuelle
(on stocke la ref du contrôle et on appelle state.update()).
"""

import flet as ft
from typing import cast
from fletx import Xapp, Xstate, Xview, route


# ── État ──────────────────────────────────────────────────────────────────────
class CounterState(Xstate):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)
        self.count: int = 0


# ── Vue ───────────────────────────────────────────────────────────────────────
class CounterView(Xview):
    @property
    def _cstate(self) -> CounterState:
        return cast(CounterState, self.state)

    def init(self) -> None:
        # init() est appelé par Xview.__init__ — on prépare les contrôles ici
        self._txt = ft.Text(
            value=f"Count: {self._cstate.count}",
            size=24,
            weight=ft.FontWeight.BOLD,
        )

    def _increment(self, _: ft.Event[ft.Button]) -> None:
        self._cstate.count += 1
        self._txt.value = f"Count: {self._cstate.count}"
        self._cstate.update()

    def build(self) -> ft.View:
        return ft.View(
            route="/",
            controls=cast(
                list[ft.BaseControl],
                [
                    ft.Column(
                        controls=cast(
                            list[ft.Control],
                            [
                                self._txt,
                                ft.ElevatedButton(
                                    "Increment",
                                    on_click=self._increment,
                                ),
                            ],
                        ),
                        tight=True,
                    )
                ],
            ),
        )


# ── Point d'entrée ────────────────────────────────────────────────────────────
def main(page: ft.Page) -> None:
    page.title = "#02 | FletX Tuto"
    Xapp(
        page=page,
        routes=cast(list, [route("/", cast(Xview, CounterView))]),  # type: ignore[arg-type]
        state=cast(Xstate, CounterState),
        init_route="/",
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
