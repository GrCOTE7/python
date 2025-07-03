import flet as ft
import os
from weasyprint import HTML


# ATTENTION: Avoir une CLI avec: py -m http.server 8000
import flet as ft


def main(page: ft.Page):
    page.title = "Aperçu PDF"

    def open_pdf(e):
        page.launch_url("http://localhost:8000/threading_vs_asyncio.pdf")

    page.add(
        ft.Text("📄 Aperçu du PDF :", style="headlineSmall"),
        ft.ElevatedButton("Ouvrir le PDF", on_click=open_pdf),
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
