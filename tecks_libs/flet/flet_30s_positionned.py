import flet as ft
import asyncio


async def countdown_task(countdown: ft.Text, page: ft.Page):
    for i in range(300, 0, -1): # 300 secondes = 5 minutes
        countdown.value = f"{i} seconde{'s' if i > 1 else ''}"
        countdown.color = ft.Colors.RED if i > 15 or i % 2 == 0 else ft.Colors.WHITE
        page.update()
        await asyncio.sleep(1)
    await page.window.destroy()


async def main(page: ft.Page):
    screen_width = 1920
    window_width = 500

    page.window.left = screen_width - window_width
    page.window.top = 0
    page.window.width = window_width
    page.window.height = 1040
    page.window.resizable = False

    title = ft.Text("Fermeture automatique dans :", size=12)
    countdown = ft.Text(size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.RED)

    header_row = ft.Row(
        controls=[
            title,
            ft.Container(
                content=countdown, expand=True, alignment=ft.Alignment(1, 0)
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        width=window_width,
    )

    separator = ft.Divider(height=1, thickness=1, color=ft.Colors.GREY)
    page.add(header_row, separator)

    # 🔁 Lancer le compte à rebours en tâche parallèle
    asyncio.create_task(countdown_task(countdown, page))

    # 💬 Ce code s'exécute immédiatement
    print("Liste des couleurs disponibles dans ft.Colors")
    # Extraire tous les noms de couleurs
    color_names = [color.name for color in ft.Colors]

    txt = "Liste des couleurs Flet :"
    t = ft.Text(txt, size=25)
    page.add(t)

    # Créer une ligne (Row) pour chaque couleur avec nom + échantillon
    color_rows = []
    for name in color_names:
        color_sample = ft.Container(
            width=100,
            height=20,
            bgcolor=getattr(ft.Colors, name),
            border_radius=4,
            alignment=ft.Alignment(1, 0),
        )
        row = ft.Row(
            controls=[
                ft.Text(name, size=12, expand=1),  # Nom aligné à gauche
                color_sample,  # Couleur alignée à droite
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        color_rows.append(row)

    # Ajouter les lignes dans une colonne scrollable
    scrollable_column = ft.Column(
        controls=color_rows,
        width=window_width,
        spacing=5.0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    # Centrer les colonne dans la page
    page.add(
        ft.Container(
            alignment=ft.Alignment(0, 0),
            content=scrollable_column,
            expand=True,
            # margin=ft.margin.only(top=80),
            padding=ft.padding.only(left=60, right=60),
        )
    )
print(dir(ft.Colors))


ft.run(main)
