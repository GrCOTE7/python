# https://www.youtube.com/watch?v=75aUc4R2GdA


# 1. if simple avec opérateur de condition
# 2. if simple avec chainage d'opérateur
# 3. Structure si alors sinon
# 4. if simple avec valeurs de condition
# 5. if avec multiples conditions (and, or, not)
# 6. if imbriqués

paragraphe = 6

# 1. if simple avec opérateur de condition
if paragraphe == 1:

    aime_citron = True
    aime_vanille = False
    aime_cannelle = False

    print("1. Travailler l'oeuf, 125g de sucre et un peu de sel")
    print("2. Ajouter 250g de farine et bien mélanger")
    print("3. Incorporer 125g de beurre")

    if aime_citron:
        print("4. Ajouter le zeste d'un citron")
    if aime_vanille:
        print("4. Ajouter 5 gouttes d'extrait de vanille")
    if aime_cannelle:
        print("4. Ajouter quelques grammes de cannelle")

    print("5. Couper les sablés en forme régulière")
    print("6. Faire cuire au feu moyen pendant 30 minutes")

# 2. if simple avec chaînage d'opérateur
elif paragraphe == 2:

    age = 7
    if age < 3:
        print("Je suis un bébé")
    if 3 <= age < 12:
        print("Je suis un enfant")
    if 12 <= age < 18:
        print("Je suis un adolescent")
    if 18 <= age:
        print("Je suis un adulte")

# 3. Structure si alors sinon
elif paragraphe == 3:

    age = 20
    if age < 3:
        print("Je suis un bébé")
    elif age < 12:
        print("Je suis un enfant")
    elif age < 18:
        print("Je suis un adolescent")
    else:
        print("Je suis un adulte")

    # Modification du paragraphe 1

# 4. if simple avec valeurs de condition
elif paragraphe == 4:

    # Condition sur les listes
    list1 = [1, 2, 3]
    list2 = []

    if list1:
        print("List1 n'est pas vide")

    if list2:
        print("List2 n'est pas vide")

    if 2 in list1:
        print("2 est dans list1")

    if 5 in list1:
        print("5 est dans list1")

    print("*" * 25)

    # Condition sur les nombres
    entier1 = 26
    entier2 = 0

    if entier1:
        print("Entier1 n'est pas nul")

    if entier2:
        print("Entier2 n'est pas nul")

    print("*" * 25)

    # Condition sur les chaines de caractères
    str1 = "Une chaîne non vide"
    str2 = ""

    if str1:
        print("str1 n'est pas vide")
    if str2:
        print("str2 n'est pas vide")

# 5. if avec multiples conditions (and, or, not)
elif paragraphe == 5:

    etat_du_temps = "beau"  # 'beau' 'couvert' 'pluie'
    temperature = 30

    if etat_du_temps == "beau" and temperature > 25:
        print("Je mets mon chapeau")

    if etat_du_temps != "beau" and temperature > 25:
        print("J'enlève mon pull")

    if etat_du_temps == "pluie" or etat_du_temps == "couvert":
        print("Je prends mon parapluie")

    if temperature <= 25:
        print("Je garde mon pull")

    if temperature <= 0 and not (etat_du_temps == "beau"):
        print("Je mets un bonnet en laine")

    if temperature < 0 and etat_du_temps == "beau":
        print("Je mets un bandeau sur les oreilles")

    if (etat_du_temps == "couvert" or etat_du_temps == "pluie") and temperature < 25:
        print("Je mets mon imperméable")

# 6. if imbriqués
elif paragraphe == 6:

    etat_du_temps = "beau"  # 'beau' 'couvert' 'pluie'
    temperature = 30

    if temperature > 25:
        if etat_du_temps == "beau":
            print("Je mets mon chapeau")
        elif etat_du_temps == "couvert":
            print("J'enlève mon pull")
            print("Je prends mon parapluie")
        else:
            print("J'enlève mon pull")
            print("Je prends mon parapluie")
    elif temperature > 0:
        if etat_du_temps == "beau":
            print("Je garde mon pull")
        elif etat_du_temps == "couvert":
            print("Je garde mon pull")
            print("Je prends mon parapluie")
            print("Je mets mon imperméable")
        else:
            print("Je garde mon pull")
            print("Je prends mon parapluie")
            print("Je mets mon imperméable")
    else:
        if etat_du_temps == "beau":
            print("Je mets un bandeau sur les oreilles")
        elif etat_du_temps == "couvert":
            print("Je prends mon parapluie")
            print("Je mets mon imperméable")
            print("Je mets un bonnet en laine")
        else:
            print("Je prends mon parapluie")
            print("Je mets mon imperméable")
            print("Je mets un bonnet en laine")

    # Voir pour simplifier le programme en supprimant les redondances
