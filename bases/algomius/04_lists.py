import random

# 1. Initialisation de liste
# 2. Accès à un élément
# 3. Modification/Ajout dans la liste
# 4. Copie de liste
# 5. Concaténation
# 6. Opération sur les listes

paragraphe = 6 
if paragraphe == 1:

    # Création d'une liste vide
    liste1 = []
    print("Liste vide", liste1, type(liste1))

    # Création d'une liste avec des valeurs
    liste2 = ["oeufs", "farine", "beurre"]
    print("Liste de valeurs", liste2, type(liste2))

    # Création d'une liste de valeurs de types différents
    liste3 = ["un mot", 9, 9.65, True]
    print("Liste de plusieurs types", liste3, type(liste3))

    # Création d\'une liste de liste
    liste4 = [
        ["oeufs", "farine", "beurre"],
        ["échelle", "perceuse", "marteau"],
        ["short", "ballon", "casquette"],
    ]
    print("Liste de listes", liste4)

    # Création d\'une liste à partir d'une chaîne de caractères
    liste5 = "nom,prénom,âge,profession".split(",")
    print("Liste à partir d'une chaîne de caractères", liste5, type(liste5))
    print("Chaîne de caractères à partir d'une liste", "-".join(liste5))

    # Liste initialisée avec une valeur par défaut
    liste6 = [0] * 10
    print("Liste avec valeurs par défaut", liste6)

    # Liste initialisée avec la fonction random
    liste7 = random.sample(range(0, 100), 5)
    print("Liste avec 5 valeurs aléatoires entre 0 et 100", liste7)

elif paragraphe == 2:

    # Accès aux éléments d'une liste
    liste1 = ["oeufs", "farine", "beurre", "lait", "miel", "pain", "cacahuètes"]
    print("Element 0", liste1[0])
    print("Element a partir de 2", liste1[2:])
    print("Element jusqu'à 5", liste1[:5])
    print("Element a partir de 2 jusqu'a 5", liste1[2:5])
    print("Element - 1", liste1[-1])
    print("Element -4 à -1", liste1[-4:-1])
    print("Index de lait", liste1.index("lait"))
    print("Recherche", "farine" in liste1)
    liste2 = [
        ["oeufs", "farine", "beurre"],
        ["échelle", "perceuse", "marteau"],
        ["short", "ballon", "casquette"],
    ]
    print("Element de liste de liste", liste2[1][0])

elif paragraphe == 3:

    liste1 = ["oeufs", "farine", "beurre", "lait", "miel", "pain", "cacahuètes"]
    print("Liste départ", liste1)

    # Modification d\'un élément
    liste1[2] = "raisins"
    print("beurre -> raisins", liste1)

    # Ajout d'un élément à la liste
    liste1.append("eau")
    print("Ajouter de l'eau", liste1)

    # Insertion d'un élément dans la liste
    liste1.insert(1, "avocats")
    print("Insertion d'avocats", liste1)

    # Suppression d'un élément
    liste1.remove("miel")
    print("Suppression du miel", liste1)
    del liste1[0]
    print("Suppression du premier élément", liste1)
    monObjet = liste1.pop()
    print("Element de la liste", monObjet)
    print("Liste sans l'élément", liste1)

    # Vidage de la liste
    liste1.clear()
    print("Liste vidée", liste1)

elif paragraphe == 4:

    # affectation dans les listes n'est pas une copie
    liste1 = ["oeufs", "farine", "beurre", "lait", "miel", "pain", "cacahuètes"]
    liste2 = liste1
    print("Liste 1", liste1)
    print("Liste 2", liste2)
    print("*" * 78)
    liste1[0] = "moutarde"
    print("Liste 1", liste1)
    print("Liste 2", liste2)
    print("*" * 78)

    # Utilisation de la fonction copy
    liste2 = liste1[::]
    liste1[0] = "oeufs"
    print("Liste 1", liste1)
    print("Liste 2", liste2)
    print("*" * 78)

elif paragraphe == 5:

    liste1 = ["oeufs", "farine", "beurre"]
    liste2 = ["lait", "miel", "pain", "cacahuètes"]
    liste3 = ["glace", "céréales"]

    # Concaténation en réutilisant une liste existante
    liste1 += liste3
    print("Liste 1", liste1)
    print("Liste 2", liste2)
    print("Liste 3", liste3)
    print("*" * 78)

    # Concaténation dans une nouvelle variable
    liste4 = liste1 + liste2
    print("Liste 1", liste1)
    print("Liste 2", liste2)
    print("Liste 3", liste3)
    print("Liste 4", liste4)
    print("*" * 78)

elif paragraphe == 6:

    # Longueur de la liste
    liste1 = ["oeufs", "farine", "beurre", "lait", "miel", "pain", "cacahuètes"]
    print("Longueur de la liste", len(liste1))

    # Tri de la liste
    liste1.sort()
    print("Trier la liste", liste1)

    # Inversement de la liste
    liste1.reverse()
    print("Inverser la liste", liste1)

    # Tri de la liste de façon décroissante
    liste2 = ["oeufs", "farine", "beurre", "lait", "miel", "pain", "cacahuètes"]
    liste2.sort(reverse=True)
    print("Trier la liste en sens inverse", liste2)
