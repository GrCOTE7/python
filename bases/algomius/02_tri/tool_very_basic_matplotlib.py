import matplotlib.pyplot as plt

# Données à représenter
donnees = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]

# Créer le graphique à bâtons
plt.bar(range(len(donnees)), donnees)

# Personnaliser le graphique
plt.title("Graphique à bâtons")
plt.xlabel("Index")
plt.ylabel("Valeurs")

# Ajouter les valeurs au-dessus des bâtons
for i, v in enumerate(donnees):
    plt.text(i, v, str(v), ha="center", va="bottom")

# Afficher le graphique
plt.show()
