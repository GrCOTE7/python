import numpy as np
import matplotlib.pyplot as plt

# Paramètres
L = 10  # Longueur de la boîte
n = 1  # Nombre quantique
x = np.linspace(0, L, 1000)  # Positions dans la boîte

# Fonction d'onde
psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Probabilité de trouver la particule à une position x
prob = np.abs(psi) ** 2

# Tracer la fonction d'onde et la probabilité
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, psi)
plt.title("Fonction d'onde")
plt.subplot(1, 2, 2)
plt.plot(x, prob)
plt.title("Probabilité")
plt.show()

