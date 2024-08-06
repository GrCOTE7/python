# 2do https://www.youtube.com/watch?v=euiip1cCna0

# 1. boucle avec condition d'arrêt (while, break, continue)
# 2. boucle avec itération (for, range, else)
# 3. boucle sur un objet iterable (list, set, tuple, dict, string) et next
# 4. Fonctions associées aux boucles (enumerate, zip, map, any, all)

paragraphe = 1

# 1. boucle avec condition d'arrêt (while, break, continue)
if paragraphe == 1:

    energie = 100

    while energie > 0:
        print("Je fais une pompe")
        energie -= 10

    print("*" * 25)

    energie = 50

    while True:
        if energie > 0:
            print("Je fais une pompe")
            energie -= 10
        else:
            break

    print("*" * 25)

    energie = 100
    compteur = 0

    while energie > 0:
        print("Je fais une pompe")
        compteur += 1
        energie -= 10

        if compteur % 2:
            continue

        print("J'en suis à", compteur, "pompes")

# 2. boucle avec itération (for, range, else)
elif paragraphe == 2:

    for i in range(10):
        print("Je fais une pompe, j'en suis à", i + 1)

    print("*" * 25)

    for i in range(4, 10):
        print("Je fais une pompe, j'en suis à", i)

    print("*" * 25)

    for i in range(2, 10, 2):
        print("Je fais une pompe mais j'en compte 2 car j'ai deux bras", i)

    print("*" * 25)

    for i in range(10, 0, -1):
        print("Je fais une pompe, il m'en reste", i - 1)

    print("*" * 25)

    for i in range(10):
        print("Je fais une pompe, j'en suis à", i + 1)
    else:
        print("Ouf terminé!!!!")

    print("*" * 25)

    energie = 50

    for i in range(10):
        print("Je fais une pompe, j'en suis à", i + 1)
        energie -= 10

        if energie <= 0:
            print("J'en peux plus!!!!!")
            break
    else:
        print("Ouf terminé!!!!")

# 3. boucle sur un objet iterable (list, set, tuple, dict, string) et next
elif paragraphe == 3:

    list1 = ["pompe", "traction", "squat", "crunch"]

    for i in list1:
        print("Je travaille sur l'exercice:", i)

    print("*" * 25)

    dict1 = {"pompe": 10, "traction": 5, "squat": 10, "crunch": 20}

    for cle, val in dict1.items():
        print("Pour l'exercice", cle, "je fais", val, "répétitions")

    print("*" * 25)

    for lettre in "musculation":
        print("La lettre est", lettre)

    print("*" * 25)

    iterateur = iter(list1)

    print(next(iterateur, "C'est fini tu peux souffler"))
    print(next(iterateur, "C'est fini tu peux souffler"))
    print(next(iterateur, "C'est fini tu peux souffler"))
    print(next(iterateur, "C'est fini tu peux souffler"))
    print(next(iterateur, "C'est fini tu peux souffler"))
    print(next(iterateur, "C'est fini tu peux souffler"))
    print(next(iterateur, "C'est fini tu peux souffler"))


# 4. Fonctions associées aux boucles (enumerate, zip, map, any, all)
elif paragraphe == 4:

    list1 = ["pompe", "traction", "squat", "crunch"]

    for pos, i in enumerate(list1):
        print("Je travaille sur l'exercice:", i, "en position", pos)

    print("*" * 25)

    exercice = ["pompe", "traction", "squat", "crunch"]
    répétition = [10, 5, 10, 20]

    for exer, rep in zip(exercice, répétition):
        print(rep, "répitions pour l'exercice", exer)

    print("*" * 25)

    performance = [20, 12, 50, 44]
    objectif = list(map(lambda x: x * 1.5, performance))
    print("Liste de mes performances", performance)
    print("Liste de mes objectifs", objectif)

    print("*" * 25)

    list1 = [True, False, True, False, False, True, True, False]
    list2 = [True, True, True, True, True, True, True, True]
    list3 = [False, False, False, False, False, False, False, False]

    print("Au moins un résultat vrai dans list1", any(list1))
    print("Au moins un résultat vrai dans list2", any(list2))
    print("Au moins un résultat vrai dans list3", any(list3))

    print("Tous les résultats vrai dans list1", all(list1))
    print("Tous les résultats vrai dans list2", all(list2))
    print("Tous les résultats vrai dans list3", all(list3))
