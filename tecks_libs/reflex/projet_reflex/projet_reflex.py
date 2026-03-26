import reflex as rx
from pymox_kit import *

class State(rx.State):
    nom: str = ""
    compteur: int = 0

    @rx.event
    def set_nom(self, nom: str):
        self.nom = nom

    @rx.var
    def bonjour(self) -> str:
        return f"Bonjour {self.nom} !"

    @rx.event
    def on_click(self):
        self.compteur += 1

    @rx.var
    def message_compteur(self) -> str:
        return f"Tu as cliqué {self.compteur} fois."


def index():
    code = f"\x1b[0;91m"
    msg = f"{BLUE}Informatique {WHITE}Sans {RED}Complexe !{R}"
    print(msg)
    end()
    return rx.center(
        rx.vstack(
            rx.heading("Informatique Sans Complexe !"),
            rx.button("Clique-moi !", on_click=State.on_click),
            rx.text(State.message_compteur),
            # rx.text(sl()),
            rx.text('─' * 55),
            rx.input(placeholder="Ton prénom ?", on_change=State.set_nom),
            rx.text(State.bonjour),
        )
    )

app = rx.App()
app.add_page(index)
