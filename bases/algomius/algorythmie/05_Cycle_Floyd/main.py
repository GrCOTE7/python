# https://www.youtube.com/watch?v=e45QoKaK8r0&list=PLo53cbpzes8ZDG62Pn4U4plWpP8_EBFal&index=5
# Résumé: Si le lièvre rattrape la tortue, c'est qu'il y a un cycle ! ;-)


class Noeud:
    """Classe représentant une liste chainée. Cette liste contient pour chaque élément une valeur ainsi que l'élément suivant"""

    def __init__(self, valeur=None, prochain=None):
        self.valeur = valeur
        self.prochain = prochain


def detectionCycleNaif(transition):
    """Fonction qui permet de détecter un cycle dans une structure de liste chaînée représentée par un dictionnaire en connaissant le point de départ : debut
    Cette fonction retourne :
    - Un booléen qui indique s'il y a un cycle (True) ou non (False)
    """
    parcours = transition

    s = set()

    while parcours:
        if parcours.valeur in s:
            return True

        s.add(parcours.valeur)

        parcours = parcours.prochain

    return False


def detectionCycleFloyd(transition):
    tortue = lievre = transition

    while lievre and lievre.prochain:
        tortue = tortue.prochain
        lievre = lievre.prochain.prochain

        if tortue == lievre:
            return True

    return False


if __name__ == "__main__":
    # Création des éléments de la liste chaînée
    transitionG = Noeud("G", None)
    transitionF = Noeud("F", transitionG)
    transitionE = Noeud("E", transitionF)
    transitionD = Noeud("D", transitionE)
    transitionC = Noeud("C", transitionD)
    transitionB = Noeud("B", transitionC)
    transitionA = Noeud("A", transitionB)

    # Création d'un cycle
    transitionA.prochain.prochain.prochain.prochain.prochain.prochain = (
        transitionA.prochain.prochain
    )

    types = ["Naif ", "Floyd"]

    for type in types:
        func = globals().get("detectionCycle" + type.strip())
        type = type.replace('i', 'ï')
        # print (type, callable(func))
        print(f"{type} : Cycle {'trouvé' if func(transitionA) else 'non trouvé'}")
