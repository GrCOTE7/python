import flet as ft
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def graph():
    x = [1, 2, 3]
    y = [4, 6, 7]

    plt.plot(x, y)
    plt.title("Graphique simple")
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")

    ax = plt.gca()

    # Grille principale : 1 unité
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))

    # Grille secondaire : 0.25 unité
    ax.xaxis.set_minor_locator(MultipleLocator(0.25))
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))

    plt.grid(which="major", color="#ccc", linewidth=1)
    plt.grid(which="minor", color="#eee", linestyle="--", linewidth=0.5)

    plt.show()


if __name__ == "__main__":

    graph()
