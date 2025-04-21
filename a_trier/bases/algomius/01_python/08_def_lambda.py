# https://www.youtube.com/watch?v=c3GywHt7Kdg


# 1. Fonction et retour de fonction (return yield)
# 2. Paramètre de fonctions (mutable, defaut, *tuple d'argument, **dictionnaire d'argument)
# 3. Récursivité
# 4. Lambda fonctions
# 5. Méthodes associées aux fonctions (callable, filter)


def lg():
    print("*" * 25)


paragraphe = 1

# 1. Fonction et retour de fonction (return yield)
if paragraphe == 1:

    # Fonction sans retour et sans paramètre
    def demarrage():
        print("La voiture est démarrée")

    demarrage()
    lg()

    # Fonction sans retour avec paramètre
    def boite_de_vitesse(num_vitesse):
        print("J'ai passé la vitesse", num_vitesse)

    boite_de_vitesse(1)
    lg()

    # Fonction avec retour
    def acceleration(vitesse):
        return vitesse + 10

    print("Nouvelle vitesse", acceleration(50))
    lg()

    # Utilisation de la fonction yield
    def vitesseDeLaBoite(num_vitesse):
        for i in range(1, num_vitesse + 1):
            yield i, type(2)

    print(vitesseDeLaBoite(6), type(vitesseDeLaBoite(6)))
    for i in vitesseDeLaBoite(6):
        print(i)

# 2. Paramètre de fonctions (mutable, defaut, *tuple d'argument, **dictionnaire d'argument)
elif paragraphe == 2:

    # Fonction avec un paramètre non mutable
    def acceleration(vitesse):
        vitesse + 10

    vitesse = 100
    acceleration(vitesse)
    print("Nouvelle vitesse", vitesse)
    lg()

    # Fonction avec un paramètre mutable
    def allumagePhare(element):
        element.add("Phare")

    element = {"Climatisation", "Radio"}
    allumagePhare(element)
    print("Elements allumés", element)
    lg()

    # Regroupement des paramètres sous forme de liste
    def allumage(*element):
        for i in element:
            print("Allumage de", i)

    allumage("Phares", "Radio", "Climatisation")
    print("*" * 25)

    # Utilisation d'un libellé pour les paramètres
    def test_allumage(phares, radio, clim):
        if phares:
            print("Les phares sont allumés")

        if radio:
            print("La radio est allumée")

        if clim:
            print("La climatisation est allumée")

    test_allumage(clim=True, phares=False, radio=True)
    lg()

    # Regroupement des paramètres sous forme de dictionnaire
    def test_allumage_dict(**element):
        if element["phares"]:
            print("Les phares sont allumés")

        if element["radio"]:
            print("La radio est allumée")

        if element["clim"]:
            print("La climatisation est allumée")

    test_allumage_dict(clim=True, phares=False, radio=True)
    lg()

    # Utilisation d'une valeur par défaut dans une fonction
    def destination(dest="France"):
        print("Je roule vers la destination", dest)

    destination("Italie")
    destination()

# 3. Récursivité
elif paragraphe == 3:

    # Exemple de fonction itérative
    def changement_roue(nb_roues):
        for i in range(nb_roues):
            print("Je change une roue")

        print("J'ai fini, bonne route")

    changement_roue(4)
    lg()

    # La même fonction en récursif
    def changement_roue_rec(nb_roues):
        if nb_roues > 0:
            print("Je change une roue")
            changement_roue_rec(nb_roues - 1)
        else:
            print("J'ai fini, bonne route")

    changement_roue_rec(4)


# 4. Lambda fonctions
elif paragraphe == 4:

    vitessePlus10 = lambda vitesse: vitesse + 10
    print("Ajouter 10 à la vitesse 100:", vitessePlus10(100))
    print("*" * 25)

    moyenne3Vitesses = lambda vit1, vit2, vit3: (vit1 + vit2 + vit3) / 3.0
    print("Vitesse moyenne 100, 50, 90:", moyenne3Vitesses(100, 50, 90))

# 5. Méthodes associées aux fonctions (callable, filter)
elif paragraphe == 5:

    # Test de la fonction callable sur un entier
    entier1 = 5
    print("Est-ce qu'un entier est appelable ?", callable(entier1))
    lg()

    # Test de la fonction callable sur une fonction def
    def demarrage():
        print("La voiture est démarrée")

    fonction1 = demarrage
    print("Est-ce qu'une fonction def est appelable ?", callable(fonction1))
    lg()

    # Test de la fonction callable sur une fonction lambda
    vitessePlus10 = lambda vitesse: vitesse + 10
    print("Est-ce qu'une fonction lambda est appelable ?", callable(vitessePlus10))
    lg()

    # Filtrage d'une liste à partir d'une fonction
    vitesses = [10, 140, 110, 85, 90, 45, 50]

    def filtreVitesseMax(vitesse):
        vitMax = [30, 50, 80, 90, 110, 130]
        return vitesse in vitMax

    vitessesFiltrees = filter(filtreVitesseMax, vitesses)

    print("Les vitesses de la liste correspondant à des vitesses max:")
    for vit in vitessesFiltrees:
        print(vit)

    lg()

    vitesses = [10, 140, 110, 85, 90, 45, 50]

    lst_vitesse = list(filter(lambda x: (x % 10 == 0), vitesses))

    print("Liste des vitesses multiples de 10", lst_vitesse)
