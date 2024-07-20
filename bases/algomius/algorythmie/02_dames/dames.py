import sys
sys.path.append('c:\\laragon\\www\\python\\tools\\')




import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)


from chrono import chrono


# 2fix: Graphic version 'dames.py' that doesn't work properly


def donneCasesLibres(listDames):
    listPossibles = [(len(listDames), i) for i in range(8)]

    listValides = [
        i
        for i in listPossibles
        if all(
            i[1] != j[1] and abs((i[0] - j[0]) / (i[1] - j[1])) != 1 for j in listDames
        )
    ]

    return listValides


def position8Dames(listDames=[]):
    """oki2"""
    global listSolutions
    if len(listDames) == 8:
        nbSols=len(listSolutions)
        if (nbSols<8 or nbSols>88):
            print(f"\n{str(nbSols).rjust(2)} : {listDames} ", end='')
        else:
            if nbSols % 27 == 0 :
                print(f"\n...\n{str(nbSols).rjust(2)} : {listDames} ", end='')    
                
            # print('.', end='')
        listSolutions.append(listDames)
    else:
        for i in donneCasesLibres(listDames):
            position8Dames(listDames + [i])


listSolutions = ["null"]

@chrono
def init(v):
    """Calcul des 92 solutions des 8 dames"""
    position8Dames()
    print(f"\nNombre de solutions : {len(listSolutions)-1}")
    
init('Délai d\'exécution')


