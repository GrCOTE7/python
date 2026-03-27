import flet as ft
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from typing import Any, cast

from utils.posit import place_figure_on_monitor

# flet run -d -r .\tecks_libs\matplotlib\matplotlib_lib.py

# Assure que le backend est TkAgg
matplotlib.use("TkAgg")


def voitures(title="Voitures"):
    fig, ax = plt.subplots()

    types = ["Essence", "Diesel", "Hybride", "Electrique", "Autres"]
    counts = [46, 30, 12, 5, 7]
    year = 2024

    title += f" en {year}"

    if fig.canvas.manager is not None:
        fig.canvas.manager.set_window_title(title)
    ax.set_title(f"{title}")
    ax.pie(counts, labels=types, shadow=True)
    ax.axis("equal")

    place_figure_on_monitor(fig, monitor_index=1, window_width=800, window_height=500)

    plt.show()


def graphs(titre="Sinusoide"):
    def carre_cube(exposant=2, titre=""):
        global x, y, label

        # Données
        x = np.arange(-10.0, 10, 0.01)
        y = x**exposant

        label = f"y = x^{exposant}"
        return label, x, y

    def autre(titre=""):

        x = [1, 2, 3]
        y = [4, 6, 7]

        label = "y"
        return label, x, y

    def sinus(titre=""):
        x = np.arange(-2.0, 2, 0.01)
        y = np.sin(x)

        label = "sin(x)"
        return label, x, y

    label, x, y = sinus(titre=titre)
    print(titre)
    if titre not in ["Voitures"]:
        # label,  x, y = carre_cube(exposant:=2, titre := "Une " + ("hyperbole" if exposant % 2 else "parabole"))
        # label, x, y = autre(titre := "3 points")
        # label, x, y = sinus(titre := "Sinusoïde")

        fig, ax = plt.subplots()
        if fig.canvas.manager is not None:
            fig.canvas.manager.set_window_title(titre)

        ax.set(xlabel="x", ylabel=label, title=titre)
        ax.grid()
        ax.plot(x, y)

        place_figure_on_monitor(
            fig, monitor_index=1, window_width=500, window_height=800
        )

        # Affiche la fenêtre
        # plt.show(block=False)

        # Petit délai pour permettre à la fenêtre de s'afficher
        # time.sleep(0.1)

        # Empêche la fenêtre de voler le focus
        manager = plt.get_current_fig_manager()
        if manager is not None and hasattr(manager, "window"):
            window = cast(Any, manager).window
            window.attributes("-topmost", False)
            # Met la fenêtre en arrière-plan
            window.lower()

        plt.show()


if __name__ == "__main__":

    print("Ok")

    # voitures(title="Voitures")
    voitures(title="Répartition des types de voitures")
    graphs()
