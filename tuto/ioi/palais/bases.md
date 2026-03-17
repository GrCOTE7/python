# Palais

Le palais est un carré de taille 4×4, et le robot se trouve au départ dans le coin en bas à gauche.

Votre robot doit passer une et une seule fois dans chacune des pièces, puis se retrouver dans sa case de départ.

À noter: Dans [la résolution initiale - line ~314](..\old_algorea.py), le script ne fait qu'écrire le pathn sans le calculer.

## → 🎯 Ordre optimal pour comprendre les 6 méthodes

1️⃣ BT — BackTracking “pur” (le plus intuitif)

C’est la base de tout.

Tu explores, tu avances, tu te bloques, tu reviens en arrière.

C’est comme résoudre un labyrinthe.

C’est visuel, concret, facile à comprendre.

C’est la fondation sur laquelle reposent les méthodes plus avancées.

👉 On commence par ça, c’est indispensable.

2️⃣ BTH — BackTracking + Heuristiques (la version intelligente)

C’est BT, mais avec des règles qui t’évitent de te coincer.

On choisit les cases “fragiles” d’abord

On évite de créer des zones isolées

On réduit énormément les essais

👉 C’est la version “propre” et efficace du BT.

👉 Très pédagogique, très utile.

3️⃣ GR — Greedy / Heuristique gloutonne (rapide, mais pas garanti)

Greedy = Glouton

Ici, tu ne reviens pas en arrière.

Tu choisis toujours le meilleur coup local.

Exemple : aller vers la case qui a le moins de voisins libres.

Très simple

Très rapide

Parfois ça marche tout seul

Parfois ça échoue → on combine avec BT

👉 C’est une étape naturelle après BTH.

4️⃣ CO — Construction directe (méthode mathématique)

Ici, on ne cherche plus :

On construit directement un cycle hamiltonien.

Motifs serpentins

Grilles pair×pair

Transformations (rotations, symétries, décalage du point de départ)

👉 C’est élégant, puissant, mais demande un peu de recul.

👉 C’est ici que notre matrice de référence entre en jeu :

5️⃣ DP — Dynamic Programming (programmation dynamique)

Là, on passe dans le monde des états :
position actuelle

ensemble des cases visitées (bitmask)

C’est très propre, très rigoureux, mais :

ça explose vite

ça demande de comprendre les bitmasks

c’est plus abstrait

👉 On le place en 5ᵉ car il faut déjà être à l’aise avec BT et les heuristiques.

6️⃣ SAT/ILP — Encodage dans un solveur général

Code : SAT = SATisfiability, ILP = Integer Linear Programming

C’est la méthode “ingénieur industriel” :

on encode le problème en logique booléenne (SAT)

ou en contraintes linéaires (ILP)

et un solveur général trouve la solution

C’est puissant, mais :

pas intuitif

pas pédagogique pour commencer demande de comprendre comment encoder un problème

👉 On le garde pour la fin.

---

🧘 Pourquoi BT est fondamental

Parce que :

BTH = BT + intelligence

GR = BT sans retour arrière

DP = BT mais avec mémoire

SAT = BT mais délégué à un solveur

CO = solution trouvée sans BT, mais BT permet de la vérifier

BT est la racine de toutes les autres méthodes.

## 1️⃣ BT — BackTracking “pur” (le plus intuitif)

## Pseudo-code

function explore(case, visited, path):
    if toutes les cases sont visitées:
        return case adjacent à A

```bash
    pour chaque voisin v de case:
        si v non visité:
            visited[v] = vrai
            path.append(v)

            si explore(v, visited, path):
                return vrai

            visited[v] = faux
            path.pop()

    return faux
```

## Diagramm

```mermaid
flowchart TD

    Start([Debut]) --> Entry[if __name__ == main]
    Entry --> Cls[cls]
    Cls --> Main[main]

    ConstMoves[MOVE_DEFINITIONS]
    ConstMoves --> ConstOffsets[OFFSETS]
    ConstMoves --> ConstArrows[ARROW_BY_DELTA]

    Main --> Find[find_hamiltonian_cycle]
    Main --> EndCall[end]

    Find --> InitVisited[Init visited set with start]
    InitVisited --> InitPath[Init path with start]
    InitPath --> ComputeTotal[total = ROWS * COLS]
    ComputeTotal --> CallBT[Call backtrack start]
    CallBT --> FindResult{backtrack true}
    FindResult -->|no| ReturnNone[Return None]
    FindResult -->|yes| ReturnPath[Return path]

    Main --> CycleCheck{cycle is None}
    ReturnNone --> CycleCheck
    ReturnPath --> CycleCheck
    CycleCheck -->|yes| PrintNoCycle[Print no cycle message]
    CycleCheck -->|no| PrintCycle[Print cycle positions]

    PrintCycle --> BuildOrder[Build order dict]
    BuildOrder --> PrintNums[Print number grid]
    PrintNums --> BuildPairs[Build pairs with zip]
    BuildPairs --> BuildArrows[Build arrows dict]
    BuildArrows --> PrintArrows[Print arrow grid]

    BuildArrows --> Dir[direction]
    ConstArrows --> Dir

    CallBT --> BTCheckLen{len path == total}
    BTCheckLen -->|yes| BTCheckReturn{start in neighbors current}
    BTCheckReturn -->|yes| BTReturnTrue[Return true]
    BTCheckReturn -->|no| BTReturnFalse[Return false]
    BTCheckLen -->|no| BTLoop[for v in neighbors current]

    BTLoop --> Neigh[neighbors]
    ConstOffsets --> Neigh
    BTLoop --> BTVisited{v in visited}
    BTVisited -->|yes| BTLoop
    BTVisited -->|no| BTMark[Add v to visited]
    BTMark --> BTAdd[path append v]
    BTAdd --> BTRecurse[Call backtrack v]
    BTRecurse -->|true| BTSuccess[Return true]
    BTRecurse -->|false| BTRestore[Remove v and pop]
    BTRestore --> BTLoop
    BTLoop --> BTFail[Return false]

```

2️⃣ BTH — BackTracking + Heuristiques (la version intelligente)

❌

3️⃣ GR — Greedy / Heuristique gloutonne (rapide, mais pas garanti)

❌

4️⃣ CO — Construction directe (méthode mathématique)

❌

5️⃣ DP — Dynamic Programming (programmation dynamique)

❌

6️⃣ SAT/ILP — Encodage dans un solveur général

❌
