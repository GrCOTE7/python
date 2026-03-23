def unmutable():  # int, float, bool, string...

    def add1(v):
        v += 1

    a = 10
    add1(a)
    print(a)


def mutable():  # list, dict, set...

    def modif(liste):
        liste.append("nouveau")
        return liste

    arr = ["a", "b"]
    arr2 = modif(arr)
    print("", id(arr), arr, "\n", id(arr2), arr2)


def unmutable_mutable():

    def modif(liste):
        liste = liste[:]  # copie
        liste.append("nouveau")
        return liste

    arr = ["a", "b"]
    arr2 = modif(arr)
    print("", id(arr), arr, "\n", id(arr2), arr2)


def soluce_courante():

    def ajoute_au_panier_bete(article, chariot=[]):
        chariot.append(article)
        return chariot

    def ajoute_au_panier(article, chariot=None):
        if chariot is None:
            chariot = []
        chariot.append(article)
        return chariot

    print("1:", ajoute_au_panier_bete("Chaussures"))
    print("2:", ajoute_au_panier_bete("T-Shirt"))
    print("-" * 77)
    print("1:", ajoute_au_panier("Chaussures"))
    print("2:", ajoute_au_panier("T-Shirt"))


    # Bonnes pratiques:
    # - Jamais de variables mutables par défaut dans les fonctions
    # - Si modifie un objet, faire une copie

if __name__ == "__main__":
    # unmutable()
    # mutable()
    # unmutable_mutable()

    soluce_courante()
