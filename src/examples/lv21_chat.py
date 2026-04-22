import flet as ft
from dataclasses import dataclass


@dataclass
class Message:
    user: str
    text: str


def main(page: ft.Page):
    page.bgcolor = "#202020"
    page.title = "Flet Chat #21"

    chat = ft.Column()

    new_message = ft.TextField(
        value="Salut !",
        border_color="#999999",
        focused_border_color="#aaaaaa",
        color=ft.Colors.GREY_300,
        expand=True,
    )

    def on_message(message: Message):
        chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(
            Message(user=str(page.session.index), text=new_message.value)
        )
        new_message.value = ""
        page.update()

    # --- Le container DOIT être créé AVANT on_resize ---
    container = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                new_message,
                ft.Button(
                    "Send",
                    on_click=send_click,
                    bgcolor="#cccccc",
                    color=ft.Colors.GREY_900,
                ),
            ],
        ),
    )

    page.add(
        ft.Text(value="Chat #21 Ready.", size=18),
        chat,
        container,  # ← maintenant la variable existe
    )


if __name__ == "__main__":
    ft.run(main)
