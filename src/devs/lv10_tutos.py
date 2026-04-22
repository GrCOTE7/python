import flet as ft

# Réfce.: https://www.youtube.com/watch?v=wtkax34EAL8


def ab_btn(page: ft.Page):

    msg = ("Hello, Flet !", "Button clicked!")
    msg_idx = 0

    page.title = "Flet Tutorials"

    label = ft.Text(msg[0], size=30)

    def make_button_style(horizontal_padding: int) -> ft.ButtonStyle:
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=4),
            bgcolor=ft.Colors.BLUE_400,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=14),
            padding=ft.Padding(horizontal_padding, 10, horizontal_padding, 10),
        )

    def on_click(e):

        nonlocal msg_idx
        msg_idx = 1 - msg_idx
        print(msg[msg_idx])
        label.value = msg[msg_idx]
        btn.style = make_button_style(48 if msg_idx == 0 else 72)

        page.update()

    btn = ft.Button(
        content="Click me!",
        on_click=on_click,
        style=make_button_style(48),
    )

    page.add(label, btn)


def tofs(page: ft.Page):
    page.title = "Tofs"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    layout = ft.Row(
        # spacing=20,
        # run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,  # horizontal
        wrap=True,
        expand=True,
        # scroll=ft.ScrollMode.AUTO, # Inutile si mis au nivo de la page
    )

    for i in range(24):
        layout.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/300?random={i}",
                # L'image gardera sa proportion
                width=100,
                height=150,
                border_radius=ft.BorderRadius.all(7),
            )
        )

    print("tofs")
    page.add(layout)


if __name__ == "__main__":
    ft.run(ab_btn)
    ft.run(tofs)
