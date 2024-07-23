import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules.IterativeSorts import IterativeSortArr
from pprint import pprint
import random

# tableaux = [[3, 1, 2], [1, 3, 2], [1, 2, 3]]
t_src = random.sample(range(1, 99), 55)
tableaux = []
tableaux = IterativeSortArr(t_src)

print('Début:',tableaux[0])


class GraphApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Animation du Tri Itératif")
        self.running = True

        # Ajouter des événements pour fermer la fenêtre
        self.master.bind("<Button-1>", self.close_on_click)
        self.master.bind("<Key>", self.close_on_keypress)

        # Obtenir la résolution de l'écran
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Taille de la fenêtre
        window_width = 1500
        window_height = 800
        x = 1800 + (screen_width - window_width) // 2
        y = -50 + (screen_height - window_height) // 2

        # Positionner la fenêtre au centre de l'écran
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Créer un cadre de fond
        self.background_frame = tk.Frame(self.master)
        self.background_frame.place(relwidth=1, relheight=1)

        # Créer la figure et l'axe pour le graphique
        self.fig, self.ax = plt.subplots(figsize=(15, 8))
        self.fig.patch.set_facecolor("lightgrey")  # Couleur de fond de la figure

        # Intégrer la figure matplotlib dans la fenêtre tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.background_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        # self.canvas.get_tk_widget().config(bg="green")  # Couleur de fond du canevas

        # Ajouter un label pour le message
        self.message_label = tk.Label(
            self.master,
            text="Affichage des étapes en cours...",
            width="50",
            fg="green",
            bg="lightgrey",
            font=("Helvetica", 24),
        )
        self.message_label.pack()

        # Démarrer l'animation
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_graph,
            frames=len(tableaux),
            interval=100,
            repeat=False,
        )

        # Configurer la fermeture de la fenêtre
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Forcer le focus sur la fenêtre tkinter
        self.master.focus_force()

    def update_graph(self, index):
        if not self.running:
            return

        tableau = tableaux[index]
        self.ax.clear()
        self.ax.bar(range(len(tableau)), tableau)
        self.ax.set_title(f"Tri itératif - Étape {index+1} / {len(tableaux)}")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Valeurs")

        # Afficher les valeurs au-dessus des bâtons
        for i, v in enumerate(tableau):
            self.ax.text(i, v, str(v), ha="center", va="bottom")

        if index == len(tableaux) - 1:
            self.master.after(0, self.change_background)

    def change_background(self):
        msg = "Cliquez ou appuyez sur une touche pour fermer la fenêtre."
        print("Le script a terminé son exécution.")
        print(msg)

        # Changer la couleur de fond pour indiquer que c'est terminé
        self.fig.patch.set_facecolor("#eee")

        # Mettre à jour le titre de la fenêtre
        self.master.title("Animation terminée - " + msg)
        self.ax.set_title(
            f"Tri itératif - Étape {len(tableaux)} / {len(tableaux)} - {msg}"
        )
        self.canvas.draw()

        # Afficher le message dans le label
        self.message_label.config(text=msg, fg="blue", bg="grey")

    def close_on_click(self, event):
        self.on_closing()

    def close_on_keypress(self, event):
        self.on_closing()

    def on_closing(self):
        self.running = False
        self.master.quit()
        self.master.destroy()


    def main(self = None): 
        root = tk.Tk()
        GraphApp(root)
        root.mainloop()


if __name__ == "__main__":
    GraphApp.main()
