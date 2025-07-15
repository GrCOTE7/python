import tkinter

fenetre = 0
canvas = 0

lastX = 0
lastY = 0

couleur = "black"


def onClick(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
    print(f"onClick sollicité ({lastX},{lastY})")


def onMove(event):
    global lastX, lastY
    canvas.create_line(lastX, lastY, event.x, event.y, fill=couleur, width=5)
    lastX = event.x
    lastY = event.y
    print(f"onMove sollicité ({lastX},{lastY})")


def setBlackColor(event):
    global couleur
    couleur = "black"


def setRedColor(event):
    global couleur
    couleur = "red"


def initFenetre():
    global fenetre, canvas

    fenetre = tkinter.Tk()
    fenetre.title("Dessin 1.0")

    canvas = tkinter.Canvas(fenetre, width=800, height=600, bg="white")
    canvas.pack()

    # canvas.create_rectangle(10, 10, 300, 300, fill="red")

    canvas.bind("<Button-1>", onClick)
    canvas.bind("<B1-Motion>", onMove)

    black_id = canvas.create_rectangle(10, 10, 30, 30, fill="black")
    red_id = canvas.create_rectangle(10, 40, 30, 60, fill="red")
    canvas.tag_bind(black_id, "<Button-1>", setBlackColor)
    canvas.tag_bind(red_id, "<Button-1>", setRedColor)

    # Démarrer la boucle d'événements Tkinter
    fenetre.mainloop()


initFenetre()
