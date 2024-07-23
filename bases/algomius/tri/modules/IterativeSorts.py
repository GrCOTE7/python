import random
from pprint import pprint


def IterativeSort(l):
    def showLine(i, l, un, deux):
        print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))

    for i in range(len(l) - 1):
        minInd = i

        for j in range(i + 1, len(l)):
            if l[j] < l[minInd]:
                minInd = j

        if i != minInd:
            showLine(i, l, l[i], l[minInd])
            l[i], l[minInd] = l[minInd], l[i]

    showLine(i + 1, l, "ni", "Fi")


def IterativeSortArr(l):
    res = []

    def showLine(i, l, un, deux):
        print(str(i).rjust(2), l, "→", str(un).rjust(2), "↔", str(deux).rjust(2))
        # print(str(i).rjust(2), end=' ')

    # showLine(0, l, l[0], min(l[1:]))

    for i in range(len(l) - 1):
        minInd = i

        for j in range(i + 1, len(l)):
            if l[j] < l[minInd]:
                minInd = j

        if i != minInd:
            showLine(i, l, l[i], l[minInd])
            res.append(l[:])  # Copie de l, et pas valeur finale
            l[i], l[minInd] = l[minInd], l[i]

    showLine(i + 1, l, "ni", "Fi")
    res.append(l)  # Valeur finale de l

    return res


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import tkinter as tk


class GraphApp:

    def default_params(self):
        self.graph_params = self.graph_params or {}

        self.graph_params.update(
            {"op_name": self.graph_params.get("op_name", "Opération")},
        )
        self.graph_params.update(
            {"speed": self.graph_params.get("speed", 0.5)},
        )
        self.graph_params.update(
            {"x_move": 0 if self.graph_params.get("screen_number", 1) != 2 else 1800},
        )

    def __init__(self, master, tableaux, graph_params=None):
        self.tableaux = tableaux
        self.graph_params = graph_params
        self.default_params()

        self.master = master
        self.master.title(f"Animation : {self.graph_params['op_name']}")
        self.running = True

        # Ajouter des événements pour fermer la fenêtre
        self.master.bind("<ButtonRelease-1>", self.close_on_click)
        self.master.bind("<Key>", self.close_on_keypress)

        # Obtenir la résolution de l'écran
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Taille de la fenêtre
        window_width = 1500
        window_height = 800

        x = self.graph_params["x_move"] + (screen_width - window_width) // 2
        y = -50 + (screen_height - window_height) // 2

        # Positionner la fenêtre au centre de l'écran
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Créer un cadre de fond
        self.background_frame = tk.Frame(self.master)
        self.background_frame.place(relwidth=1, relheight=1)

        # Créer la figure et l'axe pour le graphique
        self.fig, self.ax = plt.subplots(figsize=(15, 8))
        self.fig.patch.set_facecolor("#ccc")  # Couleur de fond de la figure

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
            bg="white",
            font=("Helvetica", 24),
        )
        self.message_label.pack()

        self.complete = False

        # Démarrer l'animation
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_graph,
            frames=len(tableaux),
            interval=self.graph_params['speed'] * 1000,
            repeat=False,
        )

        # Configurer la fermeture de la fenêtre
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Forcer le focus sur la fenêtre tkinter
        self.master.focus_force()

    def update_graph(self, index):
        if not self.running:
            return

        tableau = self.tableaux[index]
        self.ax.clear()
        self.ax.bar(range(len(tableau)), tableau)
        self.ax.set_title(
            f"{self.graph_params['op_name']} - Étape{str(index+1).rjust(3)} / {len(tableaux)}"
        )
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Valeurs")

        # Afficher les valeurs au-dessus des bâtons
        for i, v in enumerate(tableau):
            self.ax.text(i, v, str(v), ha="center", va="bottom")

        if index == len(tableaux) - 1:
            self.master.after(0, self.change_background)

    def change_background(self):
        self.complete = True
        tableaux = self.tableaux
        msg = "Cliquez ou appuyez sur une touche pour fermer la fenêtre."
        print("\nLe script a terminé son exécution.")
        print(msg)

        # Changer la couleur de fond pour indiquer que c'est terminé
        # self.fig.patch.set_facecolor("#eee")
        self.fig.patch.set_facecolor("white")

        # Mettre à jour le titre de la fenêtre
        self.master.title("Animation terminée - " + msg)
        self.ax.set_title(
            f"Tri itératif - Étape {len(tableaux)} / {len(tableaux)} - {msg}"
        )
        self.canvas.draw()

        # Afficher le message dans le label
        self.message_label.config(text=msg, fg="blue", bg="#eee")

    def close_on_click(self, event):
        self.on_closing()

    def close_on_keypress(self, event):
        self.on_closing()

    def on_closing(self):
        self.running = False
        self.master.quit()
        self.master.destroy()
        completeProcess = "terminé" if self.complete else "interrompu"
        print(f"\nFenêtre fermée - Process {completeProcess}.")

    @staticmethod
    def main(tableaux, graph_params=None):
        root = tk.Tk()
        GraphApp(root, tableaux, graph_params)
        root.mainloop()


if __name__ == "__main__":

    # IterativeSort([5, 6, 2, 1, 9, 8, 3, 4, 7])

    tableaux = IterativeSortArr([5, 6, 2, 1, 9, 8, 3, 4, 7])
    print("\nres:")
    pprint(tableaux)

    graph_params = {
        "op_name": "Tri itératif",
        "speed": .3,
        "screen_number": 2,
    }

    GraphApp.main(tableaux, graph_params)
    # GraphApp.main(tableaux)
