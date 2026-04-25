"""
lv02 — fletx 0.1.4+ compatible (avec flet 0.84.0)
Paradigme: FletXController + RxInt + listen (UI pilotee par l'etat).
"""

import flet as ft

from fletx.core import FletXController, RxInt


class CounterController(FletXController):
    """Etat reactif du compteur."""

    count = RxInt(0)

    def increment(self) -> None:
        self.count.increment()

    def decrement(self) -> None:
        self.count.decrement()

    def reset(self) -> None:
        self.count.set(0)


def main(page: ft.Page) -> None:
    page.title = "#02 | FletX Tuto"

    ctrl = CounterController()
    counter_text = ft.Text(
        value="LV02\n\nCount: 0",
        size=24,
        weight=ft.FontWeight.BOLD,
    )
    status_text = ft.Text(value="Etat: neutre", color=ft.Colors.GREY_700)

    def sync_from_state() -> None:
        value = ctrl.count.value
        counter_text.value = f"LV02\n\nCount: {value}"
        if value > 0:
            status_text.value = "Etat: positif"
            status_text.color = ft.Colors.GREEN_700
        elif value < 0:
            status_text.value = "Etat: negatif"
            status_text.color = ft.Colors.RED_700
        else:
            status_text.value = "Etat: neutre"
            status_text.color = ft.Colors.GREY_700
        # Optionnel: reactiver page.update() si l'etat est modifie
        # hors evenement UI Flet (timer, thread, callback async externe).
        # page.update()

    count_observer = ctrl.count.listen(sync_from_state)
    sync_from_state()

    def on_disconnect(_: ft.Event[ft.Page]) -> None:
        count_observer.dispose()

    page.on_disconnect = on_disconnect

    page.add(
        ft.Column(
            controls=[
                counter_text,
                status_text,
                ft.Row(
                    controls=[
                        ft.Button("-1", on_click=lambda _: ctrl.decrement()),
                        ft.Button("Reset", on_click=lambda _: ctrl.reset()),
                        ft.Button("+1", on_click=lambda _: ctrl.increment()),
                    ],
                    tight=True,
                ),
                ft.Button(
                    "+5",
                    on_click=lambda _: ctrl.count.increment(5),
                ),
            ],
            tight=True,
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
