# 2fix: Graphic version 'dames.py' that doesn't work properly

def donneCasesLibres(listDames):
    listPossibles = [(len(listDames), i) for i in range(8)]

    listValides = [
        i for i in listPossibles
        if all(
            i[1] != j[1] and abs((i[0] - j[0]) / (i[1] - j[1])) != 1 for j in listDames
        )
    ]

    return listValides


def position8Dames(listDames=[]):
    global listSolutions
    if len(listDames) == 8:
        print(f"{str(len(listSolutions)).rjust(2)} : {listDames}")
        listSolutions.append(listDames)
    else:
        for i in donneCasesLibres(listDames):
            position8Dames(listDames + [i])


listSolutions = ["null"]
position8Dames()
print(f"\nNombre de solutions : {len(listSolutions)-1}")
