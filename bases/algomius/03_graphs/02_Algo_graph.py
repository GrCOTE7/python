# 2do https://www.youtube.com/watch?v=472-NbPTe2k


from collections import deque

# 1. Parcours en largeur d'un graphe orienté non cyclique
# 2. Parcours en profondeur recursif
# 3. Parcours en profondeur itératif

généaListe = {}
généaListe["Robert"] = ["William", "Martha", "John"]
généaListe["William"] = ["Amy"]
généaListe["Amy"] = ["Steve", "Kim"]
généaListe["Steve"] = []
généaListe["Kim"] = []
généaListe["Amy"]
généaListe["Martha"] = []
généaListe["John"] = ["Alison", "Jack"]
généaListe["Alison"] = []
généaListe["Jack"] = ["Julia", "Madison"]
généaListe["Julia"] = []
généaListe["Madison"] = []

paragraphe = 1

if paragraphe == 1:
    # Parcours en largeur d'un graphe
    def parcours_largeur(graph, debut):
        A_visiter = deque()
        A_visiter.appendleft(debut)
        dejaVu = [debut]
        while A_visiter:
            noeud = A_visiter.pop()
            print("En cours de visite :", noeud)
            for voisin in graph[noeud]:
                if voisin not in dejaVu:
                    A_visiter.appendleft(voisin)

    print("Parcours en largeur")
    parcours_largeur(généaListe, "Robert")
    print("*" * 25)

elif paragraphe == 2:

    # Parcours en profondeur recursif
    def parcours_profondeur_recursive(graph, noeud, dejaVu=[]):
        print("En cours de visite :", noeud)
        dejaVu.append(noeud)
        for voisin in graph[noeud]:
            if voisin not in dejaVu:
                parcours_profondeur_recursive(graph, voisin, dejaVu)

    print("Parcours en profondeur récursif")
    parcours_profondeur_recursive(généaListe, "Robert")
    print("*" * 25)


elif paragraphe == 3:
    # Parcours en profondeur itératif
    def parcours_profondeur_iterative(graph, noeud):
        dejaVu = [noeud]
        A_visiter = [noeud]
        while A_visiter:
            noeud = A_visiter.pop()
            print("En cours de visite :", noeud)
            for voisin in graph[noeud]:
                if voisin not in dejaVu:
                    dejaVu.append(voisin)
                    A_visiter.append(voisin)

    print("Parcours en profondeur itératif")
    parcours_profondeur_iterative(généaListe, "Robert")
    print("*" * 25)
