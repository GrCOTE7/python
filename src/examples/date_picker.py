import flet as ft
import tools.screen_utils as screen_utils
import datetime

name = "DatePicker example"


def datePicker(page: ft.Page):
    selected_date = datetime.datetime.now()
    selected_date_text = ft.Text(selected_date.strftime("Selected date: %Y-%m-%d"))

    def on_date_change(e):
        picked = getattr(e.control, "value", None)
        if picked is not None:
            picked += datetime.timedelta(hours=2)
            selected_date_text.value = picked.strftime("Selected date: %Y-%m-%d")
            print(selected_date_text.value)

        page.update()

    date_picker = ft.DatePicker(
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2026, 12, 1),
        value=selected_date,
        on_change=on_date_change,
    )
    page.overlay.append(date_picker)

    def open_date_picker(e):
        date_picker.open = True
        page.update()

    return ft.Column(
        controls=[
            ft.Button(
                "Pick date",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=open_date_picker,
            ),
            selected_date_text,
        ]
    )


def main(page: ft.Page):

    screen_utils.configure_window(page)
    page.theme_mode = ft.ThemeMode.DARK  # Comment to light

    page.add(datePicker(page))
    print("oki")


ft.run(main)
