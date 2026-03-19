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

### Pseudo-code

```bash

    function explore(case, visited, path):
        if toutes les cases sont visitées:
            return case adjacent à A
    
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

\+ Pédagogique

```bash
def bt(pos, step):
    if step == TOTAL_CELLS:
        if pos == START:   # cycle hamiltonien
            save_solution()
        return

    for nxt in neighbors(pos):
        if not visited[nxt]:
            visited[nxt] = True
            path[step] = nxt
            bt(nxt, step + 1)
            visited[nxt] = False

```

### Diagramm

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

## 2️⃣ BTH — BackTracking + Heuristiques (la version intelligente)

On garde le BT, mais on choisit mieux les voisins.

### ⭐ Heuristique de Warnsdorff (adaptée aux grilles)

Pour chaque voisin possible

* on calcule le nombre de mouvements possibles depuis ce voisin

* on trie les voisins du plus contraint au moins contraint.

→ on trie les voisins selon leur “degré” (nombre de sorties possibles).

```python
# Version Pédagogique (+ simple)
def degree(pos, visited):
    """Nombre de voisins libres autour de pos."""
    count = 0
    for nxt in neighbors(pos):
        if not visited[nxt]:
            count += 1
    return count

# Version Pythonique (+ typee)
def degree(pos: Pos, visited: Dict[Pos, bool]) -> int:
    """Nombre de voisins libres autour de pos."""
    return sum(1 for v in neighbors(pos) if not visited[v])


def bth(pos, step):
    if step == TOTAL_CELLS:
        if pos == START:
            save_solution()
        return

    # 1) Générer les voisins libres
    moves = [nxt for nxt in neighbors(pos) if not visited[nxt]]

    # 2) Trier selon l’heuristique (Warnsdorff)
    moves.sort(key=lambda v: degree(v, visited))


    # 3) Explorer dans cet ordre
    for nxt in moves:
        visited[nxt] = True
        path[step] = nxt
        bth(nxt, step + 1)
        visited[nxt] = False
```
### 🎯 Les méthodes BTH que tu veux intégrer

Voici la liste officielle, propre, et cohérente :

| Méthode        | Nom complet                  | Description                                                                   |
|----------------|------------------------------|-------------------------------------------------------------------------------|
| **"BTH"**      | Backtracking + Warnsdorff    | Tri par degré simple                                                          |
| **"BTH++"**    | BTH + tie‑breaking           | Tri par degré + critère secondaire                                            |
| **"BTH+++"**   | BTH + tie‑breaking dynamique | Critère secondaire dépendant du step, de la parité, ou de la distance à START |
| **"parity"**   | BTH + filtre de parité       | On élimine les voisins qui violent la parité du chemin                        |
| **"frontier"** | BTH + tie‑breaking frontière | On favorise les cases proches de la frontière                                 |


### ⭐ BTH++ = BTH + tie‑breaking (critère secondaire) ❌

L’idée est simple :

Quand deux voisins ont le même degré, on applique un deuxième critère pour les départager.

Ce deuxième critère peut être :

* la distance à la fin,
* la distance au centre,
* la parité,
* l’ordre fixe (haut, bas, gauche, droite),
* la distance à START,
* la distance à la frontière,
etc.

→ ✔ Tie‑breaking par distance au centre (+ classique)

On favorise les cases plus centrales, car les bords sont plus contraints.

### BTH++ avec tie‑breaking (ordre secondaire) BTH++ avec parité (encore plus rapide) 

2_2 ❌ Faire simplifier graph pour n'avoir qu'un ligne (sauf départ flèche)

2_3 ❌  version Mojo


## 3️⃣ GR — Greedy / Heuristique gloutonne (rapide, mais pas garanti)

❌

## 4️⃣ CO — Construction directe (méthode mathématique)

❌

## 5️⃣ DP — Dynamic Programming (programmation dynamique)

❌

## 6️⃣ SAT/ILP — Encodage dans un solveur général

❌
