from pprint import pprint


class SortSelection:

    def __init__(self):
        self.graph_params = None

    def get_tableaux(self, initialList, graph_params):
        self.graph_params = graph_params

        # 2do faire autres cas et factorisation
        if graph_params["op_name"] == "Tri itératif":
            from sort1_IterativeSorts import IterativeSortArr

            tableaux = IterativeSortArr(initialList)

        return tableaux


if __name__ == "__main__":
    from dataTemplate import dataTemplate
    import getInitialList

    data, graphParams = dataTemplate()

    sortTypes = {
        0: "Tri itératif",
        1: "Tri récursif",
        2: "Tri à bulles",
        3: "Tri par sélection",
    }

    graphParams["op_name"] = sortTypes[0]

    print(data, graphParams, "\n", "-" * 55)

    initialList = getInitialList.getInitialList(data)

    tableaux = SortSelection().get_tableaux(initialList, graphParams)
    print(" " * (len(initialList) // 2) * 3, "→")
    pprint(tableaux)
