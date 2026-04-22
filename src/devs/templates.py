import flet as ft


def bloc_template(text: str, size: int = 14, title=False) -> ft.Control:
    _PRIMLARY_COLOR = ft.Colors.GREEN_ACCENT_400
    _DISABLED_COLOR = ft.Colors.GREY_600
    return ft.Container(
        padding=ft.Padding.symmetric(vertical=4, horizontal=12),
        border=ft.Border.all(1, _PRIMLARY_COLOR),
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.BorderRadius.all(7),
        content=ft.Row(
            controls=[
                ft.Text(
                    text,
                    weight=ft.FontWeight.BOLD if title else ft.FontWeight.NORMAL,
                    color=_PRIMLARY_COLOR if title else ft.Colors.WHITE,
                    size=size + (4 if title else 0),
                )
            ],
            alignment=(
                ft.MainAxisAlignment.CENTER if title else ft.MainAxisAlignment.START
            ),
        ),
    )


@ft.control
class rapidTemplate(ft.Column):

    title_text: str = "RapidTest"
    detail_items: list[str | ft.Control] | None = None

    def init(self):
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 7

        self.controls = [bloc_template(self.title_text, title=True)]

        if self.detail_items:
            for item in self.detail_items:
                if isinstance(item, str):
                    self.controls.append(bloc_template(item, size=12))
                else:
                    self.controls.append(item)
