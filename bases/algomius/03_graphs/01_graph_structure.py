# https://www.youtube.com/watch?v=ip9SGUd_cuc&t=643s

# 1. Relation non orienté et non pondérée
# 2. Relation orienté et non pondérée
# 3. Relation pondérée


paragraphe = 1

if paragraphe == 0:
    personne = {}
    personne["John"] = [180, 80]
    personne["Jack"] = [175, 75]
    print(personne)

if paragraphe == 1:

    reseauListe = {}
    reseauListe["Emma"] = ["John"]
    reseauListe["John"] = ["Emma", "Bob"]
    reseauListe["Marie"] = []
    reseauListe["Bob"] = ["John"]

    reseauMatrice = [
        [False, True, False, False],
        [True, False, False, True],
        [False, False, False, False],
        [False, True, False, False],
    ]

    print("Est-ce que John est ami avec Emma ?", "John" in reseauListe["Emma"])
    print("Même question avec une matrice :", reseauMatrice[1][0])

elif paragraphe == 2:

    généaListe = {}
    généaListe["Robert"] = ["William", "Martha", "John"]
    généaListe["William"] = ["Amy"]
    généaListe["Amy"] = []
    généaListe["Martha"] = []
    généaListe["John"] = ["Alison", "Jack"]
    généaListe["Alison"] = []
    généaListe["Jack"] = []

    print("Qui sont les enfants de John ?", généaListe["John"])

elif paragraphe == 3:

    villesListe = {}
    villesListe["Paris"] = {"Marseille": 772, "Strasbourg": 442, "Brest": 566}
    villesListe["Marseille"] = {"Paris": 772, "Strasbourg": 769, "Brest": 1219}
    villesListe["Strasbourg"] = {"Marseille": 769, "Paris": 442, "Brest": 1002}
    villesListe["Brest"] = {"Marseille": 1219, "Strasbourg": 1002, "Paris": 566}

    print("Distance entre Strasbourg et Brest :", villesListe["Brest"]["Strasbourg"])

    villesMatrice = [
        [0, 772, 442, 566],
        [772, 0, 769, 1219],
        [442, 769, 0, 1002],
        [566, 1219, 1002, 0],
    ]

    print("Distance entre Paris et Marseille :", villesMatrice[0][1])
