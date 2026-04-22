import flet as ft
from collections import defaultdict


def icons_list_v1(page: ft.Page):
    page.title = "Liste des icônes v1"
    page.scroll = ft.ScrollMode.AUTO

    # Récupère toutes les icônes disponibles dans ft.Icons
    icon_names = [name for name in dir(ft.Icons) if name.isupper()]
    icon_names = icon_names[
        :42
    ]  # Limite à 100 icônes pour éviter une surcharge visuelle
    row = ft.ResponsiveRow()

    for name in icon_names:
        icon_data = getattr(ft.Icons, name)

        row.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(icon_data, size=30, color=ft.Colors.LIME_500),
                        ft.Text(name, size=10),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=5,
                margin=5,
                col={"xs": 2, "sm": 1},  # ajuste la largeur des items
            )
        )

    page.add(row)


def icons_list_v2(page: ft.Page):
    page.title = "Liste des icônes v2"
    page.scroll = ft.ScrollMode.AUTO

    # Récupère toutes les icônes disponibles dans ft.Icons
    icon_names = [name for name in dir(ft.Icons) if name.isupper()]
    row = ft.ResponsiveRow()

    for name in icon_names:
        icon_data = getattr(ft.Icons, name)
        row.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(icon_data, size=30, color=ft.Colors.LIME_500),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=5,
                margin=5,
                tooltip=name,
                col={"xs": 2, "sm": 1},  # ajuste la largeur des items
            )
        )

    page.add(row)


def list_by_initial_v3(page: ft.Page):
    page.title = "Liste des icônes v3 (par initiale)"
    page.scroll = ft.ScrollMode.AUTO

    icon_names = sorted(name for name in dir(ft.Icons) if name.isupper())
    grouped_list = group_by_initial(icon_names)
    initials = sorted(grouped_list)

    selected_info = ft.Text(size=16, weight=ft.FontWeight.BOLD)
    icons_row = ft.ResponsiveRow()
    active_initial = {"value": ""}
    initial_buttons = {}

    active_style = ft.ButtonStyle(
        bgcolor=ft.Colors.LIME_200,
        color=ft.Colors.BLACK,
    )
    normal_style = ft.ButtonStyle()

    def refresh_selector_styles():
        for initial, btn in initial_buttons.items():
            btn.style = (
                active_style if initial == active_initial["value"] else normal_style
            )

    def render_initial(initial: str):
        icons = grouped_list.get(initial, [])
        selected_info.value = (
            f"Groupe {initial} - {len(icons)} icones / {len(icon_names)}"
        )
        icons_row.controls.clear()

        for name in icons:
            icon_data = getattr(ft.Icons, name)
            icons_row.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(icon_data, size=30, color=ft.Colors.LIME_500),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    margin=5,
                    tooltip=name,
                    col={"xs": 2, "sm": 1},
                )
            )

    def make_on_initial_click(initial: str):
        def _on_click(_e):
            active_initial["value"] = initial
            render_initial(initial)
            refresh_selector_styles()
            page.update()

        return _on_click

    selectors = ft.ResponsiveRow()
    for initial in initials:
        btn = ft.OutlinedButton(initial, on_click=make_on_initial_click(initial))
        initial_buttons[initial] = btn
        selectors.controls.append(
            ft.Container(
                content=btn,
                col={"xs": 2, "sm": 1},
                padding=2,
            )
        )

    if initials:
        active_initial["value"] = initials[0]
        render_initial(initials[0])
        refresh_selector_styles()

    page.add(
        ft.Text("Choisissez une lettre :", size=14),
        selectors,
        ft.Divider(height=16, thickness=1),
        selected_info,
        icons_row,
    )


def group_by_initial(names):
    groups = defaultdict(list)
    for name in names:
        initial = name[0].upper()
        groups[initial].append(name)
    return dict(groups)


def icons_list(page: ft.Page):
    # Alias de compatibilite pour les imports existants.
    # icons_list_v1(page)
    # icons_list_v2(page)
    list_by_initial_v3(page)
    pass


if __name__ == "__main__":
    ft.run(icons_list)
