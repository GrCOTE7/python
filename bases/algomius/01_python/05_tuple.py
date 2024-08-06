# https://www.youtube.com/watch?v=_yRYYi3h6oA&t=8s

from collections import deque

# 1. Tuple
# 2. Set
# 3. deque

paragraphe = 3

if paragraphe == 1:

    # Création d'un tuple à partir de valeurs
    tuple1 = (1, "banane", True)
    print("Contenu de tuple1", tuple1, type(tuple1))

    # Création d'un tuple à partir d'une liste
    liste1 = [1, 2, 3]
    tuple2 = tuple(liste1)
    print("Contenu de tuple2", tuple2, type(tuple2))

    # Accès aux éléments du tuples
    print("Element 0", tuple1[0])
    print("Element 1", tuple1[1])
    print("Element 2", tuple1[2])

    # Affectation multiple
    a, b, c = tuple1
    print("Element a", a)
    print("Element b", b)
    print("Element c", c)

    # Retour de plusieurs variables d'une même fonction
    entier1 = 2
    entier2 = 3
    resultat1, resultat2 = divmod(entier1, entier2)
    print("Solution", resultat1, "reste", resultat2)

    # Création de tuple contenant des tuples
    tuple3 = ((1, 2, 3), tuple1, (True, False))
    print("Contenu de tuple3", tuple3, type(tuple3))

elif paragraphe == 2:

    # Création d'un set 0 = False, le reste est True
    set1 = {1, "banane", True}
    print("Contenu de set 1", set1, type(set1))

    # Unicité des éléments d'un set
    set2 = {1, "banane", True, "banane", 8, 1}
    print("Contenu de set 2", set2, type(set2))

    # Ajout d'éléments dans le set1
    set1.add(8)
    print("Ajout de 8 dans set 1", set1, type(set1))
    set1.update([2, 3, 4])
    print("Ajout d'une liste dans set 1", set1, type(set1))

    # Suppression dans le set
    set1.remove("banane")
    print("Suppression de banane dans set 1", set1, type(set1))
    set1.discard("pamplemousse")
    print("Suppression de pamplemousse dans set 1", set1, type(set1))

    # Opération sur les ensembles
    ensemble1 = {1, 3, 7, 8, 9, 10}
    ensemble2 = {2, 5, 6, 8, 10}

    print("Union d'ensembles", ensemble1 | ensemble2)
    print("Intersection d'ensembles", ensemble1 & ensemble2)
    print("Différence d'ensembles", ensemble1 - ensemble2)
    print("Différence symétrique d'ensembles", ensemble1 ^ ensemble2)

    # Création d'un set non modifiable
    set2 = frozenset([1, "banane", True])
    print("Contenu de set 2", set2, type(set2))

    # Unicité dans une liste
    liste1 = [1, 5, "Robert", 8, 5, "Martine", 8, "Robert", True]
    print("Contenu de liste1", liste1, type(liste1))
    liste1 = list(set(liste1))
    print("Contenu de liste1 après utilisation de set", liste1, type(liste1))

elif paragraphe == 3:

    ETAT_LISTE = "État de la liste"

    # Création d'une collection deque
    deque1 = deque(["John", "Steve", "Jack"])
    print(ETAT_LISTE, deque1)

    # Ajout d'un élément à droite
    deque1.append("Michael")
    print("Ajout de Michael", deque1)

    # Ajout d'un élement à gauche
    deque1.appendleft("Mitch")
    print("Ajout de Mitch", deque1)

    # Rotation positive
    deque1.rotate(2)
    print("Rotation positive", deque1)

    # Rotation négative
    deque1.rotate(-1)
    print("Rotation négative", deque1)
    deque1.rotate(-1)
    print("Rotation négative", deque1)

    # Récupération de l'élément de droite
    val = deque1.pop()
    print("Element récupéré", val)
    print(ETAT_LISTE, deque1)

    # Récupération de l'élément de gauche
    val = deque1.popleft()
    print("Element récupéré", val)
    print(ETAT_LISTE, deque1)
