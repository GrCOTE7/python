from dataclasses import field
from typing import Callable
import sys

import flet as ft
import asyncio


@ft.control
class Task(ft.Column):
    task_name: str = ""
    on_task_delete: Callable[["Task"], None] = field(default=lambda task: None)

    def init(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)

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
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
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
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = str(self.display_task.label)
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.on_task_delete(self)


@ft.control
class TodoApp(ft.Column):
    # application's root control is a Column containing all other controls
    def init(self):
        self.new_task = ft.TextField(
            hint_text="What needs to be done in Todo App #6?",
            expand=True,
            text_style=ft.TextStyle(size=13),
        )
        self.tasks = ft.Column(
            controls=[Task(task_name="Example Task", on_task_delete=self.task_delete)]
        )
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.tasks,
        ]

    def add_clicked(self, e):
        task = Task(task_name=self.new_task.value, on_task_delete=self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()


async def todo_list(page: ft.Page):
    print("\nTodo 6...")
    is_tty = sys.stdout.isatty()
    delayed = 15

    def countdown_message(remaining: int) -> str:
        return f"Todo 6 Sync dans {remaining:2d}s..."

    countdown_text = ft.Text(
        countdown_message(delayed), size=16, color=ft.Colors.ORANGE_300
    )
    page.add(countdown_text)
    page.update()

    def render_countdown(remaining: int):
        message = countdown_message(remaining)
        if is_tty:
            # ANSI: clear current line, return to start, then write fresh content.
            sys.stdout.write(f"\x1b[2K\r{message}")
            sys.stdout.flush()
        countdown_text.value = message
        page.update()

    for remaining in range(delayed, 0, -1):
        render_countdown(remaining)
        await asyncio.sleep(1)
    render_countdown(0)
    if is_tty:
        print()

    page.controls.remove(countdown_text)
    page.update()

    page.title = "To-Do App 6 Sync"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    app = TodoApp()

    # add application's root control to the page
    page.add(app)

    print("\nTodo 6 Sync OK.\n")


if __name__ == "__main__":
    ft.run(todo_list)
