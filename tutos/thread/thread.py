import flet as ft
import datetime
import threading
import time


def main(page: ft.Page):
    page.title = "Bienvenue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    clock_text = ft.Text(size=30, color="blue", text_align=ft.TextAlign.CENTER)
    name_field = ft.TextField(label="Entrez votre nom", autofocus=True)
    welcome_text = ft.Text(size=20, color="green")

    def update_clock():
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            clock_text.value = f"Heure  Lactuelle : {now}"
            page.update()
            time.sleep(1)

    def on_submit(e):
        name = name_field.value.strip()
        if name:
            welcome_text.value = f"Bienvenue, {name} !"
        else:
            welcome_text.value = "Bienvenue, invité !"
        page.update()

    submit_button = ft.ElevatedButton("Valider", on_click=on_submit)

    page.add(clock_text, name_field, submit_button, welcome_text)

    # 🧵 Lancer l'horloge dans un thread
    threading.Thread(target=update_clock, daemon=True).start()


ft.app(target=main)
