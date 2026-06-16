import flet as ft
from .templates import rapidTemplate


def a_row_bloc() -> ft.Control:
    return ft.Row(
        [ft.Text("A"), ft.Text("B"), ft.Text("C")],
        alignment=ft.MainAxisAlignment.CENTER,
    )


def different_way_to_sum_numbers(n: int = 123) -> ft.Control:

    lines = [
        f"{sum(int(digit) for digit in str(n)) = }",
        f"{sum(map(int, str(n))) = }",
        f"{sum([int(digit) for digit in str(n)]) = }",
    ]
    return ft.Text("\n".join(lines))


def different_way_to_reverse(string):

    def recursiv_reverse1(s):
        new_s = ""
        if s != "":
            new_s = recursiv_reverse1(s[1:]) + s[0]
        return new_s

    def recursiv_reverse2(s):
        if len(s) <= 1:
            return s
        return recursiv_reverse2(s[1:]) + s[0]
    
    def iter_reverse(s):
        new_s = ""
        for l in s:
            new_s = l + new_s
        return new_s

    lines = [
        f"{recursiv_reverse1(string) = }",
        f"{recursiv_reverse2(string) = }",
        f"{iter_reverse(string) = }",
        f"{''.join(reversed(string)) = }",
        f"{''.join([string[i] for i in range(len(string)-1, -1, -1)]) = }",
        f"{string[::-1] = }",
    ]

    return ft.Text("\n".join(lines))


@ft.control
class RapidTest(ft.Column):

    title: str = "RapidTest"

    def init(self):
        header = rapidTemplate()
        header.title_text = self.title
        header.init()
        self.controls = [header]


def main(page: ft.Page):
    page.title = "Dev (Rapid Test)"

    # page.bgcol²²or = "#151515"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    n = 1234567

    def rb(
        title: str,
        content: list[ft.Control],
    ) -> ft.Control:
        test = RapidTest(title=title)
        return ft.Column(controls=[test, *content])

    page.add(
        rb(
            "A simple row bloc",
            [
                ft.Text("The row bloc is:"),
                a_row_bloc(),
            ],
        ),
        rb(
            "Different ways to sum digits",
            [different_way_to_sum_numbers(n)],
        ),
        rb(
            "Different ways to reverse a string",
            [different_way_to_reverse(str(n))],
        ),
    )


if __name__ == "__main__":

    ft.run(main)
