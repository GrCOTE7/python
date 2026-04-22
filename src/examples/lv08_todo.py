from dataclasses import field
from typing import Callable
import flet as ft

_PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
_DISABLED_COLOR = ft.Colors.GREY_600


# _WIDTH = INFINITE  # 350
@ft.control
class Task(ft.Column):

    task_name: str = ""
    on_task_delete: Callable[["Task"], None] = field(default=lambda task: None)

    def init(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(
            expand=1,
            on_submit=self.save_clicked,
        )

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            icon_color=_PRIMLARY_COLOR,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            icon_color=ft.Colors.RED_ACCENT_200,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=_PRIMLARY_COLOR,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    async def edit_clicked(self, e):
        # Checkbox.label peut être str | Control | None ; TextField.value attend str.
        self.edit_name.value = str(self.display_task.label or "")
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
        await self.edit_name.focus()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.on_task_delete(self)


@ft.control
class TodoApp(ft.Column):

    def init(self):

        self.title = ft.Container(
            padding=ft.Padding.symmetric(vertical=4, horizontal=12),
            border=ft.Border.all(1, _PRIMLARY_COLOR),
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(10),
            content=ft.Row(
                controls=[
                    ft.Text(
                        "GC7 Todo List #8",
                        weight=ft.FontWeight.BOLD,
                        color=_PRIMLARY_COLOR,
                        size=24,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

        self.new_task = ft.TextField(
            text_size=18,
            hint_style=ft.TextStyle(italic=True, color=ft.Colors.GREY_400, size=14),
            color=ft.Colors.WHITE,
            hint_text="What needs to be done?",
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(7),
            border_color=_PRIMLARY_COLOR,
            expand=True,
            on_change=self.task_changed,
            on_submit=self.add_clicked,
            autofocus=True,
        )

        self.add_btn = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_color=_DISABLED_COLOR,
            icon_size=28,
            width=52,
            height=52,
            disabled=True,
            mouse_cursor=ft.MouseCursor.BASIC,
            on_click=self.add_clicked,
            tooltip="Add a new task",
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLACK,
                side=ft.BorderSide(1, _DISABLED_COLOR),
                shape=ft.RoundedRectangleBorder(radius=7),
            ),
        )

        self.tasks = ft.Column(
            controls=[
                Task(task_name=task_name, on_task_delete=self.task_delete)
                for task_name in [
                    "Une première tâche",
                    "Une seconde tâche",
                ]
            ],
            spacing=-5,
        )

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 7

        self.controls = [
            self.title,
            ft.Row(
                controls=[self.new_task, self.add_btn],
            ),
            self.tasks,
        ]

        self.show_cli_tasks()

    def task_changed(self, e):
        has_text = bool(self.new_task.value)
        self.add_btn.disabled = not has_text
        self.add_btn.mouse_cursor = (
            ft.MouseCursor.CLICK if has_text else ft.MouseCursor.BASIC
        )
        self.add_btn.icon_color = _PRIMLARY_COLOR if has_text else _DISABLED_COLOR
        self.add_btn.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLACK,
            side=ft.BorderSide(1, _PRIMLARY_COLOR if has_text else _DISABLED_COLOR),
            shape=ft.RoundedRectangleBorder(radius=8),
        )
        self.add_btn.update()

    async def add_clicked(self, e):
        task = Task(task_name=self.new_task.value, on_task_delete=self.task_delete)
        self.tasks.controls.append(task)
        self.tasks.update()

        self.new_task.value = ""
        self.add_btn.disabled = True
        self.add_btn.mouse_cursor = ft.MouseCursor.BASIC
        self.add_btn.icon_color = _DISABLED_COLOR
        self.add_btn.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLACK,
            side=ft.BorderSide(1, _DISABLED_COLOR),
            shape=ft.RoundedRectangleBorder(radius=8),
        )
        self.show_cli_tasks()
        await self.new_task.focus()
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def show_cli_tasks(self):
        print(f"\n📋 Tâches ({len(self.tasks.controls)}):")
        for i, task in enumerate(self.tasks.controls, 1):
            print(f"   {i}. {getattr(task, 'task_name', '?')}")


def todo_list(page: ft.Page):
    print("\nTodo...")

    page.bgcolor = "#202020"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    todo = TodoApp()
    page.title = "To-Do App #8"
    page.update()
    page.add(todo)

    def simu_saisie():
        print("\nSimu saisie...")
        todo.new_task.value = "Tâche simulée"
        Task(task_name=todo.new_task.value, on_task_delete=todo.task_delete)
        todo.task_changed(None)  # Met à jour le bouton
        # todo.add_clicked(None)  # click btn !

        page.update()

    simu_saisie()


if __name__ == "__main__":

    ft.run(todo_list)
