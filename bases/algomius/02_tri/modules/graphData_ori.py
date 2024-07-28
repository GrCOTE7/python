    # TEMPLATE : À copier, définir data et graph_params et appeler graphData(data, graph_params) - Supprimer dans votre script, les nombreux commentaires retrouvables ici, reconnaissable par: ## :-)
    
    # from modules.graphData import graphData

    ## 1) On défini l'échantillon de valeurs uniques à trier (Nombre et valeur des extrêmes, la + petite et la + grande) et si on accepter d'avoir des doubles.
    ##À noter:  Si que uniques, respecter :
    ## numbers_number <> max_value (Logique, sinon, impossible)
    # data = {
    #     "max_value": 9,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
    #     "numbers_number": 12,  # Mini 1e0 + 1 (Soit 2)
    #     "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
    #     "twice_authorized": 1,  # 0 : Pas de double 1 si OK
    # }

    ## 2) [Facultatif] On défini aussi les params d'affichage du graphique
    # graph_params = {
    #     "op_name": "Tri itératif",
    #     "speed": 0.5,  # Délai entre 2 changements (En secondes)
    #     "screen_number": 2,  # Pour faire que le graphique sorte sur le 2ème écran et ne pas perdre la main sur l'éditeur (et le code)
    # }

    ## On demande les données et le graphique correspondant
    # graphData(data, graph_params)




def getTableaux(data):
    """
    À partir de data, on construit un tableau trié pra la fonction définie dans data['op_name']
    Args:
        data
    Returns:
        array: Liste des tableaux de chaque étape du tri
    """

    import random

    # 2fix Appel dynamique du module ad'hoc selon data['op_name'] - Pour l'heure, en dur: IterativeSortArr
    # Si indéfini (Car tout graph_params est optionnel), sera le module de tri globalement le + performant

    from IterativeSorts import IterativeSortArr

    tableaux = IterativeSortArr(
        random.choices(
            range(data["min_value"], (int)(data["max_value"] + 1)),
            k=(int)(data["numbers_number"]),
        )
        if data["twice_authorized"]
        else random.sample(
            range(data["min_value"], (int)(data["max_value"] + 1)),
            (int)(data["numbers_number"]),
        )
    )
    return tableaux


def graphData(data, graph_params=None):
    """
    Vérifie les data fournies pour contrôler que le tableau initial puisse être généré, et permettre l'affichage du graphique

    Si elles sont OK :
    - Appelle le module de tri correspondant à graph_params['op_name']
    - Appelle le module MatPlotLib
    Sinon : Message et fin du process
    """

    if validData(data):
        tableaux = getTableaux(data)

        # print(tableaux, graph_params)

        from MatPlotLib import GraphApp

        GraphApp.main(tableaux, graph_params)

    else:
        print("<>" * 52, "Vérifiez vos valeurs !", "<>" * 53)


def validData(data):
    """
    return True si les données sont valides
    Args :
        data (dict): (int) minima, (int) maxima, (int) nombre de nombres, (bool) double accepté

    Returns :
        bool : True si toutes les entrées cohérentes sinon False
    """
    return (
        data["numbers_number"] > 1
        and data["max_value"] <= 1e18
        and data["min_value"] <= data["max_value"]
        and data["numbers_number"] < (data["max_value"] - data["min_value"] + 1)
        if not data["twice_authorized"]
        else True
    )

    # tableaux = IterativeSortArr(
    #     random.choices(
    #         range(data["min_value"], (int)(data["max_value"] + 1)),
    #         k=(int)(data["numbers_number"]),
    #     )
    #     if data["twice_authorized"]
    #     else random.sample(
    #         range(data["min_value"], (int)(data["max_value"] + 1)),
    #         (int)(data["numbers_number"]),
    #     )
    # )


if __name__ == "__main__":
    data = {
        "max_value": 10,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
        "numbers_number": 7,  # Mini 1e0 + 1 (Soit 2)
        "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
        "twice_authorized": 1,  # 0 : Pas de double 1 si OK
    }

    # 2) [Facultatif] On défini aussi les params d'affichage du graphique
    graph_params = {
        "op_name": "Tri itératif",
        "speed": 0.5,  # Délai entre 2 changements (En secondes)
        "screen_number": 2,  # Pour faire que le graphique sorte sur le 2ème écran et ne pas perdre la main sur l'éditeur (et le code)
    }

    # On demande les données et le graphique correspondant
    graphData(data, graph_params)
