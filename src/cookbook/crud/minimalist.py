import flet as ft
from dataclasses import dataclass

# --- 1) Modèle observable (données durables) ---------------------


@ft.observable
@dataclass
class Counter:
    value: int = 0


# --- 2) Composant déclaratif avec hook (état local éphémère) -----


@ft.component
def CounterView(counter: Counter):
    # Hook : état local, non persistant
    editing, set_editing = ft.use_state(True)

    def increment(_):
        counter.value += 1  # met à jour le modèle → re-render auto

    def toggle_edit(_):
        set_editing(not editing)  # met à jour le hook → re-render auto

    return ft.Column(
        controls=[
            ft.Text(
                "Minimalist Declarative Counter Example",
                size=18,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Divider(color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2),
            ft.Text(f"Compteur = {counter.value}", size=24),
            ft.Button("Incrémenter", on_click=increment),
            ft.Button(
                "Mode édition: " + ("ON" if editing else "OFF"), on_click=toggle_edit
            ),
        ]
    )


# --- 3) App Flet -------------------------------------------------


def main(page: ft.Page):
    counter = Counter()  # modèle durable

    @ft.component
    def App():
        return CounterView(counter)

    page.render(App)


if __name__ == "__main__":
    ft.run(main)
