from dataclasses import dataclass, field
import flet as ft


@ft.observable
@dataclass
class User:
    first_name: str
    last_name: str

    def update(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


@ft.observable
@dataclass
class App:
    users: list[User] = field(default_factory=list)

    def add_user(self, first_name: str, last_name: str):
        if first_name.strip() or last_name.strip():
            self.users.append(User(first_name, last_name))

    def delete_user(self, user: User):
        self.users.remove(user)


@ft.component
def UserView(user: User, delete_user) -> ft.Control:
    # Local (transient) editing state—NOT in User
    is_editing, set_is_editing = ft.use_state(False)
    new_first_name, set_new_first_name = ft.use_state(user.first_name)
    new_last_name, set_new_last_name = ft.use_state(user.last_name)

    def start_edit():
        set_new_first_name(user.first_name)
        set_new_last_name(user.last_name)
        set_is_editing(True)

    def save():
        user.update(new_first_name, new_last_name)
        set_is_editing(False)

    def cancel():
        set_is_editing(False)

    if not is_editing:
        return ft.Row(
            [
                ft.Text(f"{user.first_name} {user.last_name}"),
                ft.Button(
                    "Edit",
                    on_click=start_edit,
                    style=ft.ButtonStyle(
                        animation_duration=500,
                        mouse_cursor=ft.MouseCursor.CLICK,
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.BLUE),
                            ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.RED),
                        },
                    ),
                ),
                ft.Button(
                    "Delete",
                    on_click=lambda: delete_user(user),
                    style=ft.ButtonStyle(
                        animation_duration=500,
                        mouse_cursor=ft.MouseCursor.CLICK,
                        side={
                            ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.ORANGE),
                            ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.RED),
                        },
                    ),
                ),
            ]
        )

    return ft.Row(
        [
            ft.TextField(
                label="First Name",
                value=new_first_name,
                on_change=lambda e: set_new_first_name(e.control.value),
                expand=True,
            ),
            ft.TextField(
                label="Last Name",
                value=new_last_name,
                on_change=lambda e: set_new_last_name(e.control.value),
                expand=True,
            ),
            ft.Button("Save", on_click=save),
            ft.Button("Cancel", on_click=cancel),
        ]
    )


@ft.component
def AddUserForm(add_user) -> ft.Control:
    # Uses local buffers; calls parent action on Add
    new_first_name, set_new_first_name = ft.use_state("")
    new_last_name, set_new_last_name = ft.use_state("")

    def add_user_and_clear():
        add_user(new_first_name, new_last_name)
        set_new_first_name("")
        set_new_last_name("")

    return ft.Row(
        controls=[
            ft.TextField(
                border_color=ft.Colors.BLUE_GREY_400,
                border_width=1,
                label="First Name",
                value=new_first_name,
                on_change=lambda e: set_new_first_name(e.control.value),
                expand=True,
            ),
            ft.TextField(
                border_color=ft.Colors.BLUE_GREY_400,
                border_width=1,
                label="Last Name",
                value=new_last_name,
                on_change=lambda e: set_new_last_name(e.control.value),
                expand=True,
            ),
            ft.Button(
                "Add",
                on_click=add_user_and_clear,
                height=50,
                style=ft.ButtonStyle(
                    side=ft.BorderSide(width=2, color=ft.Colors.GREEN),
                    animation_duration=500,
                    shape=ft.RoundedRectangleBorder(radius=4),
                    mouse_cursor=ft.MouseCursor.CLICK,
                    color={
                        ft.ControlState.HOVERED: ft.Colors.RED,
                        ft.ControlState.FOCUSED: ft.Colors.BLUE_800,
                        ft.ControlState.DEFAULT: ft.Colors.WHITE_54,
                    },
                    bgcolor=ft.Colors.BLACK,
                    overlay_color={ # Effet progressif du fonds
                        ft.ControlState.HOVERED: ft.Colors.with_opacity(
                            0.2, ft.Colors.ORANGE
                        ),
                        ft.ControlState.DEFAULT: ft.Colors.with_opacity(
                            0, ft.Colors.BLACK
                        ),
                    },
                ),
            ),
        ]
    )


@ft.component
def AppView() -> ft.Control:
    app, _ = ft.use_state(
        App(
            users=[
                User("John", "Doe"),
                User("Jane", "Doe"),
                User("Fooo", "Bar"),
            ]
        )
    )

    return ft.Column(
        controls=[
            AddUserForm(app.add_user),
            *[UserView(user, app.delete_user) for user in app.users],
        ]
    )


def main(page: ft.Page):

    page.title = "CRUD Declarative Example"
    page.render(AppView)


if __name__ == "__main__":
    ft.run(main)
