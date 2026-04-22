import asyncio
import flet as ft
from dataclasses import dataclass

try:
    from examples.lv24_simus import simulate_chat
except ImportError:
    from lv24_simus import simulate_chat

# ❌  Simu login
# ❌  Simu msgs avec lv24_simus.py


@dataclass
class Message:  # noqa: B903
    user_name: str
    text: str
    message_type: str


@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(self.message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user_name),
            ),
            ft.Column(
                tight=True,
                spacing=5,
                controls=[
                    ft.Text(self.message.user_name, weight=ft.FontWeight.BOLD),
                    ft.Text(self.message.text, selectable=True),
                ],
            ),
        ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def main(page: ft.Page):
    AUTO_LOGIN = True
    # AUTO_LOGIN = False
    SIMULATE_USERS = True
    # SIMULATE_USERS = False

    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat #24"

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.store.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"{join_user_name.value} has joined the chat.",
                    message_type="login_message",
                )
            )

    async def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.store.get("user_name") or "",
                    new_message.value,
                    message_type="chat_message",
                )
            )
            new_message.value = ""
            page.update()
            await new_message.focus()
            page.run_task(scroll_to_end)

    async def scroll_to_end():
        # Retry with small delays to survive focus/layout races on the last message.
        for delay in (0, 0.03, 0.08):
            await asyncio.sleep(delay)
            await chat.scroll_to(offset=-1, duration=80)

    def append_chat_control(control: ft.Control):
        chat.controls.append(control)
        page.update()
        page.run_task(scroll_to_end)

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(
                message.text,
                italic=True,
                color=ft.Colors.ON_SURFACE_VARIANT,
                size=12,
            )
        append_chat_control(m)

    def publish_simulated_message(user_name: str, text: str, message_type: str):
        page.pubsub.send_all(
            Message(
                user_name=user_name,
                text=text,
                message_type=message_type,
            )
        )

    async def run_simulations():
        await simulate_chat(publish_simulated_message)

    page.pubsub.subscribe(on_message)

    # A dialog asking for a user display name
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        value="Lionel" if AUTO_LOGIN else "",
        autofocus=True,
        on_submit=join_chat_click,
    )

    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.Button(content="Join chat", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(welcome_dlg)

    # Chat messages
    chat = ft.Column(
        expand=True,
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
    )

    # A new message entry form
    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    # Add everything to the page
    page.add(
        ft.Container(
            content=chat,
            border=ft.Border.all(1, ft.Colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            controls=[
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED,
                    tooltip="Send message",
                    on_click=send_message_click,
                ),
            ]
        ),
    )

    if AUTO_LOGIN and (join_user_name.value or "").strip():
        join_chat_click(None)

    if SIMULATE_USERS:
        page.run_task(run_simulations)


if __name__ == "__main__":
    ft.run(main)
