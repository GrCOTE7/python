def msg():
    for i in range(10):
        print()

    ma_liste = ["un", "deux", "trois", "quatre", "cinq"]

    # Supprimer l'élément à l'index 1
    element = ma_liste.pop(1)
    print("element:", element)  # Affiche "deux"

    ma_liste.append("six")
    ma_liste.insert(0, "zero")
    ma_liste.insert(2, "deux")
    ma_liste.remove('zero')
    print("ma_liste:", ma_liste)  # Affiche ["un", "trois", "quatre", "cinq"]

    for i in range(7):
        print()


if __name__ == "__main__":
    msg()
