from ctypes import alignment
import flet as ft
from theTime import theTime as tt
from theTime import nf
import os, time

import flet_lottie as fl


# Lazy  (Lent)
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
# def main(page: ft.Page):
#     rs = ft.Row(
#         wrap=True,
#         scroll="always",
#         expand=True,
#         alignment=ft.MainAxisAlignment.CENTER,
#     )

#     for i in range(5000):
#         rs.controls.append(
#             ft.Container(
#                 ft.Text(f"Item {i}", color="black"),
#                 width=100,
#                 height=100,
#                 alignment=ft.alignment.center,
#                 bgcolor=ft.Colors.AMBER_100,
#                 border=ft.border.all(1, ft.Colors.AMBER_200),
#                 border_radius=ft.border_radius.all(5),
#             ),
#         ),

#     # Utilisation d'un Container principal pour forcer le centrage
#     centered_container = ft.Container(
#         content=rs, alignment=ft.alignment.center, expand=True
#     )

#     page.add(centered_container)
#     page.update()

# Moins lent, sauf si très grand nombre d'items
# os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
# def main(page: ft.Page):

#     gvs = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=2, spacing=5)
#     page.add(gvs)

#     for i in range(10000):
#         gvs.controls.append(
#             ft.Container(
#                 ft.Text(f"Item {i}", color="#444444"),
#                 alignment=ft.alignment.center,
#                 bgcolor=ft.Colors.AMBER_100,
#                 border=ft.border.all(3, ft.Colors.BLACK45),
#                 border_radius=ft.border_radius.all(5),
#             )
#         )
#     page.update()


def main(page: ft.Page):
    lvs = ft.ListView(
        expand=1,
        spacing=5,
        item_extent=100,
    )
    page.add(lvs)

    for i in range(51000):
        lvs.controls.append(ft.Text(f"Line {nf(i,0): >9}"))
        # send page to a page
        if i % 500 == 0:
            time.sleep(1)
            page.update()
            print(tt(), page.route, 'Updated!', f"{nf(i,0): >9}")

    # Send the rest of the page
    page.update()

    # Utilisation d'un Container principal pour forcer le centrage
    centered_container = ft.Container(
        content=lvs, alignment=ft.alignment.center, expand=True
    )
    # page.add(centered_container)

    print(tt(), page.route)


ft.app(main)
