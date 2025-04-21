# https://www.youtube.com/watch?v=euiip1cCna0

# 1. boucle avec condition d'arrêt (while, break, continue)
# 2. boucle avec itération (for, range, else)
# 3. boucle sur un objet iterable (list, set, tuple, dict, string) et next
# 4. Fonctions associées aux boucles (enumerate, zip, map, any, all)


from tkinter import dnd


def lg():
    print("*" * 25)


paragraphe = 4

POMPE = "Je fais une pompe"
# 1. boucle avec condition d'arrêt (while, break, continue)
if paragraphe == 1:

    energie = 100

    while energie > 0:
        print(POMPE)
        energie -= 10

    lg()

    energie = 50

    while True:
        if energie > 0:
            print(POMPE)
            energie -= 10
        else:
            break

    lg()

    energie = 100
    compteur = 0

    while energie > 0:
        print(POMPE)
        compteur += 1
        energie -= 10

        if compteur % 2:
            continue

        print("J'en suis à", compteur, "pompes")

# 2. boucle avec itération (for, range, else)
elif paragraphe == 2:

    for i in range(10):
        print(POMPE + ", j'en suis à", f"{i+1:2d}")

    lg()

    for i in range(4, 10):
        print(POMPE + ", j'en suis à", i)

    lg()

    for i in range(2, 10, 2):
        print(POMPE, "mais j'en compte 2 car j'ai deux bras", i)

    lg()

    for i in range(10, 0, -1):
        print(POMPE, "il m'en reste", i - 1)

    lg()

    for i in range(10):
        print(POMPE, "j'en suis à", i + 1)
    else:
        print("Ouf terminé!!!!")

    lg()

    energie = 50

    for i in range(10):
        print(POMPE, "j'en suis à", i + 1)
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

    lg()

    dict1 = {"pompe": 10, "traction": 5, "squat": 10, "crunch": 20}

    for cle, val in dict1.items():
        print("Pour l'exercice", cle, "je fais", val, "répétitions")

    lg()

    for lettre in "musculation":
        print("La lettre est", lettre)

    lg()

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
        print("Je travaille sur l'exercice:", f"{i:8s}", "en position", pos)

    lg()

    exercice = ["pompe", "traction", "squat", "crunch"]
    répétition = [10, 5, 10, 20]

    for exer, rep in zip(exercice, répétition):
        print(f"{rep:2d}", "répétitions pour l'exercice", exer)

    lg()

    performance = [20, 12, 50, 44]
    objectif = list(map(lambda x: x * 1.5, performance))
    print("Liste de mes performances", performance)
    print("Liste de mes objectifs", objectif)

    lg()

    lists = [[True, False] * 4, [True] * 8, [False] * 8]

    for i in range(3):
        print(f"list{i+1} =", lists[i])
    for i in range(3):
        print(
            f"any(list{i+1}): Au moins un résultat vrai dans list{i+1}", any(lists[i])
        )
    for i in range(3):
        print(f"all(list{i+1}): Tous les résultats vrai dans list{i+1}", all(lists[i]))
