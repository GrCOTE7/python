import tracemalloc
import numpy as np
from generator import generate_products_by_generator, generate_products_in_list


# Commencez à suivre l'utilisation de la mémoire
tracemalloc.start()

# Créez un grand tableau numpy
# x = np.random.rand(1000000)

products = generate_products_by_generator()

all_products = []
for product in products:
    # print(product, flush=True)

    all_products.append(product)
# print()
# print(all_products)

# Prenez un instantané de l'utilisation de la mémoire
snapshot = tracemalloc.take_snapshot()

# Arrêtez de suivre l'utilisation de la mémoire
tracemalloc.stop()

# Affichez les informations sur l'utilisation de la mémoire
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:10]:
    print(stat)

print('x'*72)
# Commencez à suivre l'utilisation de la mémoire
tracemalloc.start()

# Créez un grand tableau numpy
# x = np.random.rand(1000000)
# x = np.random.rand(100000)

products = generate_products_in_list()


# Prenez un instantané de l'utilisation de la mémoire
snapshot2 = tracemalloc.take_snapshot()

# Arrêtez de suivre l'utilisation de la mémoire
tracemalloc.stop()

# Affichez les informations sur l'utilisation de la mémoire
top_stats = snapshot2.statistics("lineno")

for stat2 in top_stats[:10]:
    print(stat2)
