from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import tkinter as tk


class GraphApp:

    tableaux = []

    def default_params(self):
        self.graph_params = self.graph_params or {}

        default_values = {
            "op_name": "Opération",
            "speed": 0.5,
            "x_move": 0 if self.graph_params.get("screen_number", 1) != 2 else 1800,
        }
        # On récupère les graph_params, et si indéfini, ou pas de graph_params, on attribue aux clés les valeurs par défaut
        for key, default_value in default_values.items():
            self.graph_params.update({key: self.graph_params.get(key, default_value)})

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
            text=self.graph_params["op_name"] + ": Affichage des étapes en cours...",
            width="50",
            fg="green",
            bg="white",
            font=("Comic Sans MS", 24),
        )
        self.message_label.pack()

        self.complete = False

        # Démarrer l'animation
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_graph,
            frames=len(tableaux),
            interval=self.graph_params["speed"] * 1000,
            repeat=False,
        )

        # Configurer la fermeture de la fenêtre
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Forcer le focus sur la fenêtre tkinter
        self.master.focus_force()

    def max_values(self):
        return {
            1: 120,
            2: 60,
            3: 40,
            4: 30,
            5: 24,
            6: 20,
            7: 17,
            8: 15,
            9: 13,
            10: 12,
            11: 11,
            12: 10,
            13: 9,
            14: 8,
            15: 8,
            16: 7,
            17: 7,
            18: 7,
        }

    def get_sticks(self, tableaux_last_line):
        l_min = len(str(tableaux_last_line[0]))
        l_quasi_max = len(str(tableaux_last_line[-2]))
        nbr_v = len(tableaux_last_line)
        valeurs = self.max_values()
        show_all = (
            nbr_v <= valeurs.get(l_quasi_max, 0)
            if l_min >= 0
            else valeurs.get(l_quasi_max, 0) - 10
        )
        return [] if show_all else [0, len(tableaux_last_line) - 1]

    def update_graph(self, index):
        if not self.running:
            return

        tableau = self.tableaux[index]
        self.ax.clear()
        self.ax.bar(range(len(tableau)), tableau)
        self.ax.set_title(
            f"{self.graph_params['op_name']} - Étape{str(index+1).rjust(3)} / {len(self.tableaux)}"
        )
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Valeurs")

        # Afficher les valeurs au-dessus des bâtons
        sticks = self.get_sticks(self.tableaux[-1])
        for i, v in enumerate(tableau):
            color = "black"
            if index == i:
                color = "red"
                self.der_change = (index, v)
            if sticks == [] or i in sticks:
                self.ax.text(i, v, str(v), ha="center", va="bottom", color=color)
        # Mettre à jour le titre de la fenêtre
        if index == len(self.tableaux) - 1:
            self.master.after(0, self.change_background)

    def change_background(self):
        self.complete = True
        tableaux = self.tableaux
        msg = "Cliquez ou appuyez sur une touche pour fermer la fenêtre."
        print("\nLe script a terminé son exécution.")
        print(msg)

        # print("der étape:", self.der_change)
        self.ax.text(
            self.der_change[0],
            self.der_change[1],
            str(self.der_change[1]),
            ha="center",
            va="bottom",
            color="purple",
        )

        # Changer la couleur de fond pour indiquer que c'est terminé
        # self.fig.patch.set_facecolor("#eee")
        self.fig.patch.set_facecolor("white")

        # Mettre à jour le titre de la fenêtre
        self.master.title("Animation terminée - " + msg)
        self.ax.set_title(
            f"Tri itératif - Étape {len(tableaux)} / {len(tableaux)} (Fini  !) → {msg}"
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

    from dataTemplate import dataTemplate

    # On récupère les données nécessaires:
    # Des data pour définir l'échantillon de données
    # Des params d'affichage du graphique
    data, graphParams = dataTemplate()
    print(data)
    print(graphParams, "\n", "-" * 74)

    # On demande les données et le graphique correspondant
    from graphData import graphData

    graphData(data, graphParams)
