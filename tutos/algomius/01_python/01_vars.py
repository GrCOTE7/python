# La toute première: https://www.youtube.com/watch?v=3ACDFB13aVM

# 1. Généralité sur les variables
# 2. les variables entières
# 3. Les variables décimales
# 4. Les variables booléennes
# 5. Changement de type des variables


def lg(n=27):
    print("*" * n)


paragraphe = 1

if paragraphe == 1:
    entier = 1
    print("entier", entier, type(entier))

    decimal = 1.0
    print("decimal", decimal, type(decimal))

    booleen = True
    print("booleen", booleen, type(booleen))

    lg()

    # Affection multiple valeurs différentes
    var1, var2, var3 = 5, 6.2, True
    print("var1", var1, type(var1))
    print("var2", var2, type(var2))
    print("var3", var3, type(var3))

    lg()

    # Échange des valeurs de deux variables
    var1, var2 = var2, var1
    print("var1", var1, type(var1))
    print("var2", var2, type(var2))

    lg()

    # Affection multiple valeur identique
    var1 = var2 = var3 = 1
    print("var1", var1, type(var1))
    print("var2", var2, type(var2))
    print("var3", var3, type(var3))

    lg()

elif paragraphe == 2:

    entier1 = 2
    entier2 = 3
    entier3 = entier1 + entier2
    print("Entier3", entier3, type(entier3))
    print("Entier2", entier2, type(entier2))

    # le résultat devient un décimal
    resultat1 = entier3 / entier2
    print("Resultat1", resultat1, type(resultat1))

    # Résultat de la division entière
    resultat2 = entier3 // entier2
    print("Resultat2", resultat2, type(resultat2))

    # Reste de la division entière
    resultat3 = entier3 % entier2
    print("Resultat3", resultat3, type(resultat3))

    # Solution et Reste en 1 opération
    resultat4, resultat5 = divmod(entier3, entier2)
    print("Solution", resultat4, type(resultat4), "reste", resultat5, type(resultat5))

elif paragraphe == 3:

    decimal1 = 2.5
    decimal2 = 3.6
    decimal3 = decimal1 + decimal2
    print("Decimal3", decimal3, type(decimal3))

    decimal4 = float(7)
    print("Decimal4", decimal4, type(decimal4))

    decimal5 = 9.0
    print("Decimal5", decimal5, type(decimal5))

    resultat1 = decimal1 / decimal2
    print("Resultat1", resultat1, type(resultat1))

    # Résultat de la division entière
    resultat2 = decimal1 // decimal2
    print("Resultat2", resultat2, type(resultat2))

    # Reste de la division entière
    resultat3 = decimal1 % decimal2
    print("Resultat3", resultat3, type(resultat3))

    # Solution et Reste
    resultat4, resultat5 = divmod(decimal1, decimal2)
    print("Solution", resultat4, type(resultat4), "reste", resultat5, type(resultat5))

elif paragraphe == 4:

    valeurVrai = True
    valeurFaux = False

    print("Non Vrai", not valeurVrai)
    print("Non Faux", not valeurFaux)
    print("Opérateur et", valeurVrai and valeurFaux)
    print("Opérateur ou", valeurVrai or valeurFaux)
    print("Opérateur xor (1 ^ 0)", valeurVrai ^ valeurFaux)
    print("Opérateur xor (1 ^ 1)", valeurVrai ^ valeurVrai)
    print("Opérateur xor (0 ^ 0)", valeurFaux ^ valeurFaux)

    valeurBool1 = 1 < 4
    print("ValeurBool1", valeurBool1)
    valeurBool2 = 1 > 4
    print("valeurBool2", valeurBool2)
    valeurBool3 = 2 == 2
    print("valeurBool3", valeurBool3)
    valeurBool4 = 2 != 2
    print("valeurBool4", valeurBool4)
    valeurBool5 = "2" < "14"
    print("valeurBool5", valeurBool5)

    lg()

    # 0 est faux, le reste est vrai
    valeurBool6 = bool(0)
    print("valeurBool6", valeurBool6)
    valeurBool7 = bool(7)
    print("valeurBool7", valeurBool7)

    # Vide est faux, le reste est vrai (pour str, list, tuple, dict, set)
    valeurBool8 = bool("")
    print("valeurBool8", valeurBool8)
    valeurBool9 = bool("bla bla")
    print("valeurBool9", valeurBool9)

elif paragraphe == 5:
    entier1 = 5
    decimal1 = 3.6

    print(entier1, "converti en decimal", float(entier1))
    print(decimal1, "converti en entier", int(decimal1))
