from pprint import pprint

# 2do https://www.youtube.com/watch?v=Fhr878yNyFQ

# 1. Tri topologique avec un parcours en profondeur du graphe
# 2. Tri topologique classique
# 3. Tri topologique classique en inversant les arcs

paragraphe = 1

graph = {}
graph["chaussures"] = []
graph["chaussettes"] = ["chaussures"]
graph["caleçon"] = ["chaussures", "pantalon"]
graph["pantalon"] = ["chaussures", "ceinture"]
graph["montre"] = []
graph["chemise"] = ["ceinture", "cravate"]
graph["ceinture"] = ["veste"]
graph["cravate"] = ["veste"]
graph["veste"] = []

if paragraphe == 1:

    def tri_topologique_dfs(graph):
        lstTriee = []
        nbDejaVu = {}
        for sommet in graph.keys():
            if sommet not in nbDejaVu.keys():
                nbDejaVu[sommet] = 0
                aVisiter = [sommet]
                while aVisiter:
                    noeud = aVisiter[-1]
                    voisins = graph[noeud]
                    if nbDejaVu[noeud] == len(voisins):
                        aVisiter.pop()
                        lstTriee.append(noeud)
                    else:
                        voisin = voisins[nbDejaVu[noeud]]
                        nbDejaVu[noeud] += 1
                        if voisin not in nbDejaVu.keys():
                            nbDejaVu[voisin] = 0
                            aVisiter.append(voisin)

        return lstTriee[::-1]

    print("Tri topologique en profondeur")
    pprint(graph)
    # pprint(tri_topologique_dfs(graph))

elif paragraphe == 2:

    def tri_topologique(graph):
        nbDependance = {sommet: 0 for sommet in graph.keys()}
        for elements in graph.values():
            for i in elements:
                nbDependance[i] += 1
        sansDependance = [noeud for noeud in graph.keys() if nbDependance[noeud] == 0]
        lstTriee = []
        while sansDependance:
            noeud = sansDependance.pop()
            lstTriee.append(noeud)
            for voisin in graph[noeud]:
                nbDependance[voisin] -= 1
                if nbDependance[voisin] == 0:
                    sansDependance.append(voisin)
        return lstTriee

    print("Tri topologique classique")
    # pprint(graph)
    pprint(tri_topologique(graph))

elif paragraphe == 3:

    def tri_topologique_inverse(graph):
        sansDependance = [noeud for noeud in graph.keys() if not graph[noeud]]
        lstTriee = []
        while sansDependance:
            noeud = sansDependance.pop()
            lstTriee.append(noeud)
            for cle, element in graph.items():
                if noeud in element:
                    element.remove(noeud)
                    if not element:
                        sansDependance.append(cle)
        return lstTriee

    graph = {}
    graph["chaussures"] = ["chaussettes", "pantalon", "caleçon"]
    graph["chaussettes"] = []
    graph["caleçon"] = []
    graph["pantalon"] = ["caleçon"]
    graph["montre"] = []
    graph["chemise"] = []
    graph["ceinture"] = ["pantalon", "chemise"]
    graph["cravate"] = ["chemise"]
    graph["veste"] = ["cravate", "ceinture"]

    print("Tri topologique classique inversé")
    # pprint(graph)
    pprint(tri_topologique_inverse(graph))
