from dataclasses import field
from typing import Callable
import flet as ft
import asyncio


@ft.control
class Task(ft.Column):

    task_name: str = ""
    on_task_delete: Callable[["Task"], None] = field(default=lambda task: None)

    def init(self):
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, label_style=ft.TextStyle(size=14)
        )
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
                            icon=ft.Icons.EDIT,
                            on_click=self.edit_clicked,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.TRANSPARENT,
                                shape=ft.CircleBorder(),
                            ),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            on_click=self.delete_clicked,
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.TRANSPARENT,
                                shape=ft.CircleBorder(),
                            ),
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
        # Checkbox.label peut être str | Control | None ; TextField.value attend str.
        self.edit_name.value = str(self.display_task.label or "")
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

    _PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
    _DISABLED_COLOR = ft.Colors.GREY_600
    # _WIDTH = INFINITE  # 350

    def init(self):

        # --- Titre centré ---
        self.title = ft.Container(
            padding=ft.Padding.symmetric(vertical=4, horizontal=12),
            border=ft.Border.all(1, self._PRIMLARY_COLOR),
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(12),
            content=ft.Row(
                controls=[
                    ft.Text(
                        "Todo List App #7",
                        weight=ft.FontWeight.BOLD,
                        color=self._PRIMLARY_COLOR,
                        size=24,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )

        # --- Champ de saisie ---
        self.new_task = ft.TextField(
            text_size=18,
            hint_style=ft.TextStyle(italic=True, color=self._DISABLED_COLOR),
            color=ft.Colors.WHITE,
            hint_text="What needs to be done?",
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(7),
            border_color=self._PRIMLARY_COLOR,
            expand=True,
            mouse_cursor=ft.MouseCursor.CLICK,
            on_change=self.task_changed,
            on_submit=self.add_clicked,
            autofocus=True,
        )
        # --- Bouton ajouter (désactivé par défaut) ---
        self.add_btn = ft.IconButton(
            icon=ft.Icons.ADD,
            icon_color=self._DISABLED_COLOR,
            icon_size=28,
            width=52,
            height=52,
            disabled=True,
            mouse_cursor=ft.MouseCursor.BASIC,
            on_click=self.add_clicked,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLACK,
                side=ft.BorderSide(1, self._DISABLED_COLOR),
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )

        task_sample = ft.TextStyle(size=14, color=ft.Colors.WHITE)
        self.tasks_view = ft.Column(
            controls=[
                ft.Checkbox(label="Une tâche", label_style=task_sample),
            ],
            spacing=-5,
        )

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # Espacement de base entre sections principales.
        self.spacing = 7

        # Si on veut contrôler la largeur du bloc
        # self.controls = [
        #     ft.Container(
        #         width=self._WIDTH,
        #         content=ft.Column(
        #             controls=[
        #                 self.title,
        #                 ft.Row(
        #                     controls=[self.new_task, self.add_btn],
        #                     alignment=ft.MainAxisAlignment.CENTER,
        #                 ),
        #                 self.tasks_view,
        #             ],
        #             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #             spacing=15,
        #         ),
        #     )
        # ]

        self.controls = [
            self.title,
            ft.Row(
                controls=[self.new_task, self.add_btn],
            ),
            self.tasks_view
        ]

        self.show_cli_tasks()

    # --- Mise à jour du bouton selon le champ ---
    def task_changed(self, e):
        has_text = bool(self.new_task.value)
        self.add_btn.disabled = not has_text
        self.add_btn.mouse_cursor = (
            ft.MouseCursor.CLICK if has_text else ft.MouseCursor.BASIC
        )
        self.add_btn.icon_color = (
            self._PRIMLARY_COLOR if has_text else self._DISABLED_COLOR
        )
        self.add_btn.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLACK,
            side=ft.BorderSide(
                1, self._PRIMLARY_COLOR if has_text else self._DISABLED_COLOR
            ),
            shape=ft.RoundedRectangleBorder(radius=8),
        )
        self.add_btn.update()

        # print("TodoApp tasks_view :", [task.label for task in self.tasks_view.controls])

    # --- Action bouton ---
    async def add_clicked(self, e):
        self.tasks_view.controls.append(
            ft.Checkbox(
                label=self.new_task.value,
                label_style=ft.TextStyle(size=14, color=ft.Colors.WHITE),
            )
        )
        self.tasks_view.update()
        self.new_task.value = ""
        self.add_btn.disabled = True
        self.add_btn.mouse_cursor = ft.MouseCursor.BASIC
        self.add_btn.icon_color = self._DISABLED_COLOR
        self.add_btn.style = ft.ButtonStyle(
            bgcolor=ft.Colors.BLACK,
            side=ft.BorderSide(1, self._DISABLED_COLOR),
            shape=ft.RoundedRectangleBorder(radius=8),
        )
        self.show_cli_tasks()
        await self.new_task.focus()
        self.update()

    def show_cli_tasks(self):
        print(f"\n📋 Tâches ({len(self.tasks_view.controls)}):")
        for i, task in enumerate(self.tasks_view.controls, 1):
            label = getattr(task, "label", "?")
            print(f"   {i}. {label}")


async def todo_list(page: ft.Page):
    print("\nTodo 7...")
    await asyncio.sleep(3)

    page.title = "To-Do App 7"

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.update()

    # create application instance
    todo = TodoApp()
    # add application's root control to the page
    page.add(todo)

    # # create application instance
    # app1 = TodoApp()
    # app2 = TodoApp()
    # # add application's root control to the page
    # page.add(app1, app2)

    def simu_saisie():
        print("\nSimu saisie...")
        todo.new_task.value = "Tâche simulée"
        todo.task_changed(None)  # Met à jour le bouton
        # todo.add_clicked(None)  # click btn !

        page.update()

    simu_saisie()


if __name__ == "__main__":

    ft.run(todo_list)
