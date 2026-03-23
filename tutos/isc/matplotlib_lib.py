import flet as ft
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Assure que le backend est TkAgg
matplotlib.use("TkAgg")


def voitures(titre=""):

    fig, ax = plt.subplots()

    types = ["Essance", "Diesel", "Hybride", "Electrique", "Autres"]
    counts = [46, 30, 12, 5, 7]

    ax.set_title("Répartition Parc Auto")
    ax.pie(counts, labels=types, shadow=True)
    ax.axis("equal")

    plt.show()


def graphs():
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

    if titre not in ["Voitures"]:
        # label,  x, y = carre_cube(exposant:=2, titre := "Une " + ("hyperbole" if exposant % 2 else "parabole"))
        # label, x, y = autre(titre := "3 points")
        # label, x, y = sinus(titre := "Sinusoïde")

        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title(titre)

        ax.set(xlabel="x", ylabel=label, title=titre)
        ax.grid()
        ax.plot(x, y)

        # Positionnement de la fenêtre
        manager = plt.get_current_fig_manager()
        window = manager.window
        # Récupère la taille de l'écran
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Taille de la fenêtre
        window_width = 500
        window_height = 800
        # Position à droite
        x_pos = screen_width - window_width
        y_pos = (screen_height - window_height) // 2
        # Applique la position
        window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        # Affiche la fenêtre
        # plt.show(block=False)

        # Petit délai pour permettre à la fenêtre de s'afficher
        # time.sleep(0.1)

        # Empêche la fenêtre de voler le focus
        window.attributes("-topmost", False)
        # Met la fenêtre en arrière-plan
        window.lower()

        plt.show()


if __name__ == "__main__":
    print("Ok")

    voitures(titre := "Voitures")
    graphs()
