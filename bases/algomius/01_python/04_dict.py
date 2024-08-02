# 1. Initialisation de dictionnaire
# 2. Accès à un élément
# 3. Modification/Ajout dans un dictionnaire
# 4. Opération sur les dictionnaires

paragraphe = 4
if paragraphe == 1:

    # Création d'un dictionnaire vide
    dict1 = {}
    print("Dictionnaire vide", dict1, type(dict1))

    # Création d'un dictionnaire avec des valeurs
    dict2 = {
        "Jean-Michel": "0102030405",
        "Martine": "0504030201",
        "Robert": "0105020403",
    }
    print("Dictionnaire avec des valeurs", dict2, type(dict2))

    # Création d'un dictionnaire de valeurs de types différents
    dict3 = {
        "nom": "Dupont",
        "prenom": "Robert",
        "taille": 1.80,
        "poids": 90,
        "delhumour": True,
    }
    print("Dictionnaire de plusieurs types", dict3, type(dict3))

    # Création d'un dictionnaire avec uniquement les clés
    mesCles = ("Jean-Jacques", "Arnaud", "Sylvie")
    valDefaut = "à compléter"

    dict4 = dict.fromkeys(mesCles, valDefaut)
    print("Dictionnaire avec valeur par défaut", dict4)

    # Création d'un dictionnaire de dictionnaires
    dict5 = {
        "Jean-Michel": {"tel": "0102030405", "mail": "jm@fai.fr"},
        "Martine": {"tel": "0504030201", "mail": "titine@fai.fr"},
        "Robert": {"tel": "0105020403", "mail": "bob@fai.fr"},
    }
    print("Dictionnaire de dictionnaires", dict5)

elif paragraphe == 2:

    # Accès aux éléments d'un dictionnaire
    dict1 = {
        "Jean-Michel": "0102030401",
        "Martine": "0504030202",
        "Robert": "0105020403",
    }
    print("Numéro de Jean-Michel", dict1["Jean-Michel"])
    print("Affichage des clés", dict1.keys())
    print("Affichage des valeurs", dict1.values())
    print("Affichage sous forme de tuples", dict1.items())
    print("Recherche par clé", "Martine" in dict1.keys())
    print("Recherche par valeur", "0105020403" in dict1.values())
    dict2 = {
        "Jean-Michel": {"tel": "0102030405", "mail": "jm@fai.fr"},
        "Martine": {"tel": "0504030201", "mail": "titine@fai.fr"},
        "Robert": {"tel": "0105020403", "mail": "bob@fai.fr"},
    }
    print("Mail de Martine", dict2["Martine"]["mail"])

elif paragraphe == 3:

    dict1 = {
        "Jean-Michel": "0102030405",
        "Martine": "0504030201",
        "Robert": "0105020403",
    }
    print("Dictionnaire de départ", dict1)

    # Modification d'un élément
    dict1["Robert"] = "0606060606"
    print("Changement numéro de Robert", dict1)

    # Ajout d'un élément au dictionnaire
    dict1["Brigitte"] = "0405060708"
    print("Ajouter Brigitte au dictionnaire", dict1)
    dict1["Brigitte"] = "0405060709"

    # Suppression d'un élément
    a=dict1.pop("Jean-Michel")
    print("Suppression de Jean-Michel", dict1)
    print(a) # val du dict retiré
    del dict1["Martine"]
    print("Suppression de Martine", dict1)

    # Vidage du dictionnaire
    dict1.clear()
    print("Dictionnaire vidé", dict1)

    # Une liste peut être une valeur de dictionnaires (Mutable)
    dict1 = {
        "Jean-Michel": "0102030405",
        "Martine": "0504030201",
        "Robert": "0105020403",
    }
    dict1["Jean"] = ["0708090102", "0508070901"]
    print("Dictionnaire avec une liste en valeur", dict1)

    # Mais une liste ne peut pas être la clé d'un dictionnaire (Mutable)
    liste1 = ["Martine", "Jean"]
    dict1[liste1] = "0605040302"

elif paragraphe == 4:

    # Longueur du dictionnaire
    dict1 = {
        "Jean-Michel": "0102030405",
        "Martine": "0504030201",
        "Robert": "0105020403",
    }
    print("Longueur du dictionnaire", len(dict1))

    # Copie d'un dictionnaire
    dict2 = dict1.copy()
    # dict2 = dict1[::] # Ne marche pas
    dict2['Lionel'] = '7777777777'
    print("Dictionnaire1", dict1)
    print("Dictionnaire2 avec Ajout de Lionel", dict2)

    # Valeur par défaut d'un dictionnaire
    tel = dict1.setdefault("Martine", "à compléter")
    print("Téléphone de Martine", tel)
    tel = dict1.setdefault("Dédé", "à compléter")
    print("Téléphone de Dédé", tel)
    print("État du dict", dict1)
