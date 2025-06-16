import flet as ft


def main(page: ft.Page):

    page.title = "Mon APK"

    def action(e):
        label.value = "Bouton cliqué !"
        page.update()

    label = ft.Text("Hello World from Lionel")
    btn = ft.ElevatedButton("APPUYER ICI !")

    btn.on_click = action

    page.add(label, btn)


ft.app(target=main)
