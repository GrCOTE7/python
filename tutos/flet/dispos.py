from os import name
import flet as ft


def main(page: ft.Page):

    import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Mini Dashboard 🧱"
    page.scroll = "auto"

    # Titre dans une colonne
    header = ft.Column(
        [
            ft.Text("🎨 Mini Dashboard Flet", size=30, weight="bold", color="cyan"),
            ft.Text("Un exemple structuré avec Column, Row, Container et Grid"),
        ],
        spacing=5,
    )

    # Ligne de boutons
    actions = ft.Row(
        [
            ft.ElevatedButton("Ajouter", icon=ft.Icons.ADD),
            ft.OutlinedButton("Modifier", icon=ft.Icons.EDIT),
            ft.TextButton("Supprimer", icon=ft.Icons.DELETE),
        ],
        spacing=10,
    )

    # Carte stylée avec Container
    card = ft.Container(
        content=ft.Column(
            [
                ft.Text("🗂️ Statistiques", size=20, weight="bold"),
                ft.Text("42 éléments analysés", color="green"),
            ]
        ),
        padding=15,
        bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        border_radius=10,
        width=250,
    )

    # GridView de vignettes
    grid = ft.GridView(
        expand=True,
        max_extent=120,
        spacing=10,
        run_spacing=10,
        child_aspect_ratio=1,
    )

    grid.controls.extend([
        ft.Container(
            content=ft.Text(f"📦 {i+1}", size=18, text_align="center"),
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.TERTIARY_CONTAINER,
            border_radius=8,
            padding=10,
        )
        for i in range(12)
    ])

    # Organisation de tout dans une colonne principale
    page.add(
        ft.Column(
            [
                header,
                actions,
                card,
                ft.Divider(),
                ft.Text("🖼️ Galerie dynamique", size=18, weight="w600"),
                grid,
            ],
            spacing=20,
            expand=True,
        )
    )


ft.app(target=main)
