import flet as ft  # type: ignore[import]
import matplotlib.pyplot as plt
import io
import base64

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import tempfile
import flet as ft

def fig_to_base64(): # Pour codespace et mobile
    # Création du graphique
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 3, 2, 4], marker='o', color='blue', label='Données')
    ax.set_title("Exemple simple Matplotlib")

    # graduations
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.grid(which="major", axis='y', color="#ccc", linewidth=1)

    # Sauvegarde en mémoire
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)

    # Conversion base64
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return img_base64

def fig_to_tempfile(): # Pour local
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

    img_base64 = fig_to_base64()

    page.add(
        ft.Stack(
            controls=[
                ft.Container(
                content=ft.Text(
                    "Un graph inséré dans une App Flet",
                    color="cyan",
                    size=25,
                ),
                width=450,
                alignment=ft.alignment.Alignment(0, 0),  # centre
                top=0,
            ),
                # ft.Image(src=img_path, top=50, width=500, height=400, fit="contain") # type: ignore
                ft.Image(
                    src=f"data:image/png;base64,{img_base64}",
                    top=15,
                    width=450,
                    height=400,
                    fit="contain",
                )
            ],
        )
    )


if __name__ == "__main__":

    ft.run(tuto_lv02)
