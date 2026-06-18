import flet as ft  # type: ignore[import]
import matplotlib.pyplot as plt
import io
import base64

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import tempfile
import flet as ft


def fig_to_tempfile():
    fig, ax = plt.subplots()
    points = {
        "A": (1, 1),
        "B": (2, 3),
        "C": (3, 2),
        "D": (4, 4),
    }

    x, y = zip(*points.values())
    # marker: . , o, ^ v < > s p * x D _ latex: r"$\alpha$" beta Gamma times - r"$OKi$" - r"$\frac{1}{2}$"
    ax.plot(
        x,
        y,
        marker=r"$\gamma$",
        markersize=15,
        markerfacecolor="grey",
        color="red",
        label="Courbe de la Vie",
        linewidth=2,
        linestyle="-",
    )  # linestyle -, --, -., :
    labels = ["A", "B", "C", "D"]
    
    ax.legend(loc='lower right')

    # Ajouter les labels
    for xi, yi, label in zip(x, y, labels):
        ax.text(xi, yi, label, fontsize=16, ha='right', va='bottom', color='blue')

    ax.set_title("Exemple simple Matplotlib")

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.grid(which="major", axis='y', color="#ccc", linewidth=1)

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
                    "Un graph inséré dans une App Flet",
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
