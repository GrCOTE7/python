import tkinter


def script() -> None:

    arr = list(range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]

    arr2 = arr[:5:3]
    print("arr", arr, "→", arr[:5])
    print("arr2", arr2)


def ihm():  # Interface Homme-Machine (IHM)

    maFenetre = tkinter.Tk()
    # maFenetre.title("IHM")

    monLabel = tkinter.Label(maFenetre, text="Compteur : 0")

    def onClick(event):
        print("onClick sollicité")
        global compteur
        compteur = compteur + 1
        # monLabel["text"] = f"Compteur : {compteur}"
        monLabel.config(text=f"Compteur : {compteur}")
        print(f"Compteur : {compteur}")

    monBouton = tkinter.Button(maFenetre, text="Cliquer ICI !", width=50)
    monBouton.pack()
    monBouton.bind("<Button-1>", onClick)

    # monLabel.pack(side=tkinter.TOP)
    monLabel.pack()

    maFenetre.geometry("400x200")
    maFenetre.mainloop()


if __name__ == "__main__":
    script()

    compteur = 0
    ihm()
    print("-" * 117)
