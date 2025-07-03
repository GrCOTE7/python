import flet as ft
import datetime
import asyncio


def main(page: ft.Page):
    page.title = "Bienvenue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 🕒 Affichage de l'heure
    clock_text = ft.Text(size=30, color="blue", text_align=ft.TextAlign.CENTER)

    async def update_clock():
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            clock_text.value = f"Heure actuelle : {now}"
            page.update()
            await asyncio.sleep(1)

    # 🙋‍♂️ Entrée du nom
    name_field = ft.TextField(label="Entrez votre nom", autofocus=True)
    welcome_text = ft.Text(size=20, color="green")

    def on_submit(e):
        name = name_field.value.strip()
        if name:
            welcome_text.value = f"Bienvenue, {name} !"
        else:
            welcome_text.value = "Bienvenue, invité !"
        page.update()

    submit_button = ft.ElevatedButton("Valider", on_click=on_submit)

    # 📦 Ajout des éléments à la page
    page.add(clock_text, name_field, submit_button, welcome_text)

    # 🌀 Lancer la mise à jour de l'horloge en arrière-plan
    page.run_task(update_clock)


# 🚀 Lancer l'application
ft.app(target=main)
