import sys
import os

script_dir = os.path.dirname(__file__)
modules_dir = os.path.join(script_dir, "modules")
sys.path.append(modules_dir)


def get_l():
    return [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]


def basicSort():
    l = get_l()
    print(f"{' ' * 4}Ori{' ' * 4}: {l}")

    s = l.copy()
    s.sort()
    print(f"{' ' * 4}sort() : {s}")

    sgc7 = l.copy()
    sgc7 = sorted(sgc7, key=lambda x: x)
    print(f"{' ' * 4}sgc7() : {sgc7}")


def runIterativeSort():
    from modules.IterativeSorts import IterativeSort

    l = get_l()
    IterativeSort(l)


def runDisplayIterativeSort():
    """
    Définition des critères pour :
    - data : La population des data l'affichage
    - graph_params : Appel de graphData(data, graph_params)
    """
    from modules.graphData import graphData

    # Voir le code nécessaire commenté directement dans le fichier graphData.py pour le copier/coller comme ci-dessous

    data = {
        "max_value": 21,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
        "numbers_number": 7,  # Mini 1e0 + 1 (Soit 2)
        "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
        "twice_authorized": 1,  # 0 : Pas de double 1 si OK
    }

    graph_params = {
        "op_name": "Tri itératif",
        "speed": 2,  # Délai entre 2 changements (En secondes)
        "screen_number": 2,  # Pour faire que le graphique sorte sur le 2ème écran et ne pas perdre la main sur l'éditeur (et le code)
    }

    graphData(data, graph_params)


if __name__ == "__main__":

    # basicSort()
    # print()
    # runIterativeSort()

    runDisplayIterativeSort()
