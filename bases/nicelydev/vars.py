def msg():
    ma_liste = ["un", "deux", "trois", "quatre", "cinq"]

    # Supprimer l'élément à l'index 1
    element = ma_liste.pop(1)
    print(element)  # Affiche "deux"
    print(ma_liste)  # Affiche ["un", "trois", "quatre", "cinq"]


if __name__ == "__main__":

    msg()
