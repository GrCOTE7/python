from getInitialList import getInitialList
from SortSelection import SortSelection
from pprint import pprint

# import getInitialList

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


def graphData(data, graph_params=None):
    """
    Vérifie les data fournies pour contrôler que le tableau initial puisse être généré, et permettre l'affichage du graphique
    avec le module getInitialList()

    Si elles sont OK :
    - Appelle le module de tri correspondant à graph_params['op_name']
    - Appelle le module MatPlotLib
    Sinon : Message et fin du process
    """
    initialList = getInitialList(data)
    if initialList: 
 
        sorts = SortSelection()
        tableaux = sorts.get_tableaux(initialList, graph_params)
        # print(" " * (len(initialList) // 2) * 3, "→")
        # pprint(tableaux)
        # print(tableaux, graph_params)
        from MatPlotLib import GraphApp

        GraphApp.main(tableaux, graph_params)

    else:
        pprint("<>" * 20 + "Vérifiez vos valeurs" + "<>" * 20, width=55)


if __name__ == "__main__":
    
    from dataTemplate import dataTemplate

    # On récupère les données nécessaires:
    # Des data pour définir l'échantillon de données
    # Des params d'affichage du graphique
    data, graphParams = dataTemplate()
    print(data, graphParams, "\n", "-" * 55)

    # On demande les données et le graphique correspondant
    graphData(data, graphParams)
 