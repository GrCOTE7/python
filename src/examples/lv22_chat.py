import flet as ft
from dataclasses import dataclass


@dataclass
class Message:
    user: str
    text: str
    msg_type: str


def main(page: ft.Page):
    AUTO_LOGIN = True
    # AUTO_LOGIN = False

    title = ft.Text("Chat App #22")
    page.title = title.value

    chat = ft.Column()
    new_message = ft.TextField(expand=True)

    def on_message(message: Message):
        if message.msg_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        elif message.msg_type == "login_message":
            chat.controls.append(
                ft.Text(
                    message.text,
                    italic=True,
                    size=12,
                )
            )
        page.update()

    page.pubsub.subscribe(on_message)  # Broadcasting

    def send_click(e):

        msg = Message(
            user=page.session.store.get("user_name") or "",
            text=new_message.value,
            msg_type="chat_message",
        )
        if msg.text:
            page.pubsub.send_all(msg)
            print(new_message.value)
            new_message.value = ""

    def join_click(e):
        name = (user_name.value or "").strip()

        if not name:
            user_name.error = "Name can't be blank!"
            page.update()
        else:
            page.session.store.set("user_name", name)
            join_dialog.open = False
            msg = Message(
                user=name,
                text=f"{name} has joined the chat.",
                msg_type="login_message",
            )
            page.pubsub.send_all(msg)

        print(f"{user_name.value = }")

    user_name = ft.TextField(label="Enter your name", value="Lionel")

    join_dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title="Welcome!",
        content=ft.Column([user_name], tight=True),
        actions=[
            ft.Button(
                content="Join chat",
                on_click=join_click,
                style=ft.ButtonStyle(
                    mouse_cursor=ft.MouseCursor.CLICK,
                    shape=ft.RoundedRectangleBorder(radius=7),
                ),
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.show_dialog(join_dialog)

    if AUTO_LOGIN and (user_name.value or "").strip():
        join_click(None)

    page.add(
        title,
        chat,
        ft.Row(
            [
                new_message,
                ft.Button(
                    "Send",
                    on_click=send_click,
                    style=ft.ButtonStyle(mouse_cursor=ft.MouseCursor.CLICK),
                ),
            ]
        ),
    )


if __name__ == "__main__":
    ft.run(main)
