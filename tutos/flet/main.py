import flet as ft
from typing import Final


class Const:
    def __init__(self, **kwargs):
        object.__setattr__(self, "_data", kwargs)

    def __getattr__(self, name):
        return self._data[name]

    def __setattr__(self, name, value):
        raise AttributeError(f"Constante '{name}' non modifiable")


def main(page: ft.Page):
    print("Oki aaa 21")

    C = Const(MAX=100, PI=3.14)
    print(C.MAX, C.PI)  # 100

    # C.PI = 99     # AttributeError !

    page.add(ft.Text(str(z)))
    page.update()


txt = """
<div>
    <h1>Oki aaa 21</h1>
    <p>Voici une constante :</p>
    <ul>
        <li>MAX = 100</li>
        <li>PI = 3.14</li>
    </ul>
</div>"""

print(txt)

if __name__ == "__main__":
    z = 5
    ft.run(main)
