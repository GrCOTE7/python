# https://www.youtube.com/watch?v=7Pa2YbLQ_DE

import sys
# from sys import argv

# Utilisation des fonctions d'entrée sorties en Python


# 1 - Commentaires
# 2 - Affichage
# 3 - Paramétrage du programme
# 4 - Acquisition d'information dans le programme et entrée standard
# 5 - Redirection des flux des flux de sortie :
#     --> Sortie standard
#     --> Sortie standard d'erreur
def lg(n=27):
    print("*" * n)

paragraphe = 1

if paragraphe == 1:
    # Ceci est un Commentaire
    print("Ceci n'est pas un commentaire")  # Mais ceci en est un
    """
    Ceci est un Commentaire
    sur
    plusieurs
    lignes
    """
    print("# ici le dièse n'est pas un commentaire")
    # Ici il l'est à nouveau car il n'est pas dans une chaîne de caractère

elif paragraphe == 2:
    # Écriture de plusieurs chaines
    print("Je", "suis", "content")  # Le séparateur par défaut est l'espace
    lg()
    print("Je", "suis", "content", sep="\t")  # Utilisation du séparateur tabulation
    lg()
    print("Je", "suis", "content", sep="\n")  # Utilisation du séparateur saut de ligne
    lg()

    # Écriture d'une chaîne en plusieurs fois, le saut de ligne est le séparateur par défaut
    print("Je")
    print("suis")
    print("heureux")
    lg()

    # Écriture d'une chaîne en plusieurs fois, avec un espace en séparateur de fin
    print("Je", end=" ")
    print("suis", end=" ")
    print("heureux")
    lg()

    # Vidage des buffers demandé explicitement
    print("Je suis en forme", flush=True)

elif paragraphe == 3:
    # Lecture des paramètres donnés dans le terminal
    if len(sys.argv) == 2:
        print(sys.argv)
        nom_programme, nom_utilisateur = sys.argv
        print(
            "Le nom du programme est",
            nom_programme,
            "et son utilisateur est",
            nom_utilisateur,
        )
    else:
        print("Le programme doit avoir 1 paramètre <utilisateur>")

elif paragraphe == 4:
    # Lecture d'information à partir du terminal
    # nom = input()
    # age = input()
    nom = input("Quel est votre nom? ")
    print(nom)
    age = input("Quel est votre âge? ")
    print(age)
    print("Vous êtes", nom, "et vous avez", age, "ans")

    # Utilisation du même exemple avec un fichier d'entrées
    # py 02_inOut.py < 02_entrees.txt

elif paragraphe == 5:
    # redirection de la sortie standard
    print("Message a destination de la sortie standard", file=sys.stdout)
    print("Message a destination de la sortie standard d'erreur", file=sys.stderr)

    # Utilisation du même exemple avec des fichiers

    # Redirection de la sortie standard uniquement
    # py 02_inOut.py > 02_sortie.txt

    # Redirection de la sortie standard d'erreur uniquement
    # py 02_inOut.py 2> 02_erreur.txt

    # Redirection dans deux fichiers distincts
    # py 02_inOut.py > 02_sortie.txt 2> 02_erreur.txt

    # Redirection dans le même fichier
    # py 02_inOut.py > 02_sortie.txt 2>&1
