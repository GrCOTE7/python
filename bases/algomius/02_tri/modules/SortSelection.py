from pprint import pprint


class SortSelection:

    def __init__(self):
        self.graph_params = None

    def get_tableaux(self, initialList, graph_params):
        self.graph_params = graph_params

        sort_modules = {
            "Tri itératif": "sort1_IterativeSorts",
            "Tri récursif": "sort2_RecursiveSort",
            "Tri à bulles": "sort3_BubbleSort",
            "Tri par insertion": "sort4_InsertionSort",
            "Tri par fusion": "sort5_MergeSort",
            "Tri rapide": "sort6_QuickSort",
            "Tri par tas": "sort7_HeapSort",
        }

        module_name = sort_modules.get(graph_params["op_name"])
        if module_name is not None:
            sort_module = __import__(module_name)
            tableaux = sort_module.SortArr(initialList)

        return tableaux


if __name__ == "__main__":
    from dataTemplate import dataTemplate
    import getInitialList

    data, graphParams = dataTemplate()

    types = {
        1: "itératif",
        2: "récursif",
        3: "à bulles",
        4: "par insertion",
        5: "par fusion",
        6: "rapide",
        7: "tas",
        8: "par comptage",
        9: "dichotomique",
        10: "complexité",
    }

    graphParams["op_name"] = sortTypes[4]

    print(data, "\n")
    print(graphParams, "\n", "-" * 55)

    initialList = getInitialList.getInitialList(data)
    # initialList = [3, 1, 4, 2]

    print(initialList, "\n")

    tableaux = SortSelection().get_tableaux(initialList, graphParams)
    # print(" " * ((len(initialList) // 2) * 3 + 10), "→")
    # pprint(tableaux)
