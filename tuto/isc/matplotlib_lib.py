import flet as ft
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Assure que le backend est TkAgg
matplotlib.use("TkAgg")

# Données
exposant = 3 # CHANGE HERE !

x = np.arange(-10.0, 10, 0.01)
y = x**exposant

# Création du graphique
fig, ax = plt.subplots()
fig.canvas.manager.set_window_title(
    "Une " + ("hyperbole" if exposant % 2 else "parabole")
)
ax.plot(x, y)

ax.set(xlabel="x", ylabel=f"y = x^{exposant}", title=f"y = x^{exposant}")
ax.grid()

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
plt.show(block=False)

# Petit délai pour permettre à la fenêtre de s'afficher
# time.sleep(0.1)

# Empêche la fenêtre de voler le focus
window.attributes("-topmost", False)
# Met la fenêtre en arrière-plan
window.lower()

# Maintient la fenêtre ouverte
plt.show()
