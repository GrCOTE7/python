def msg():
    for i in range(10):
        print()

    ma_liste = ["un", "deux", "trois", "deux", "quatre", "cinq"]

    print(ma_liste.count('deux'))
    
    print("ma_liste:", ma_liste)  # Affiche ["un", "trois", "quatre", "cinq"]

    for i in range(7):
        print()


if __name__ == "__main__":
    msg()
