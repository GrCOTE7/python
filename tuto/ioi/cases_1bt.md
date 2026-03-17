# → 🎯 Ordre optimal pour comprendre les 6 méthodes

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

Exemple : aller vers la case qui a le moins de 
voisins libres.

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

🧘 Pourquoi BT est fondamental

Parce que :

BTH = BT + intelligence

GR = BT sans retour arrière

DP = BT mais avec mémoire

SAT = BT mais délégué à un solveur

CO = solution trouvée sans BT, mais BT permet de la vérifier

BT est la racine de toutes les autres méthodes.
