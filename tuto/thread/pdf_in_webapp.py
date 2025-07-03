import flet as ft
import os
from weasyprint import HTML


# ATTENTION: Avoir une CLI avec: py -m http.server 8000

def main(page: ft.Page):
    page.title = "Aperçu PDF"

    # Générer le PDF si nécessaire
    pdf_path = "threading_vs_asyncio.pdf"
    if not os.path.exists(pdf_path):
        HTML(string="<h1>PDF de test</h1>").write_pdf(pdf_path)

    # Bouton pour ouvrir le PDF dans un nouvel onglet
    def open_pdf(e):
        page.launch_url("http://localhost:8000/threading_vs_asyncio.pdf")

    page.add(
        ft.Text("📄 Aperçu du PDF :", style="headlineSmall"),
        ft.ElevatedButton("Ouvrir le PDF", on_click=open_pdf),
    )

ft.app(target=main, view=ft.WEB_BROWSER)
