import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#333333"
    page.title = "Flet Chat #20"

    chat = ft.Column()
    new_message = ft.TextField(value="Salut !", expand=True)

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""

    page.add(
        ft.Text(value="Ready → Chat #20.", size=18),
        chat,
        ft.Row(controls=[new_message, ft.Button("Send", on_click=send_click)]),
    )


if __name__ == "__main__":
    ft.run(main)
