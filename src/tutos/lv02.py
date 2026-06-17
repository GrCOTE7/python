import flet as ft  # type: ignore[import]
import matplotlib.pyplot as plt
import io
import base64

import matplotlib.pyplot as plt
import tempfile
import flet as ft


def fig_to_tempfile():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [3, 1, 4])
    ax.set_title("Exemple simple Matplotlib")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(tmp.name)
    plt.close(fig)
    return tmp.name


def tuto_lv02(page):
    page.title = "Tutos #02 - Graphique Matplotlib"

    img_path = fig_to_tempfile()

    page.add(
        ft.Stack(
            controls=[
                ft.Text(
                    "Un graph inséré dans une Flet App",
                    top=0,
                    left=0,
                    color="cyan",
                    size=30,
                ),
                ft.Image(src=img_path, top=50, width=500, height=400, fit="contain") # type: ignore
            ],
        )
    )


if __name__ == "__main__":

    ft.run(tuto_lv02)
