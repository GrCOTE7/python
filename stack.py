squares = []
for x in range(8):
    squares.append((x, x**2))
print(squares)

# Avec fonction anonyme
squares = list(map(lambda x: x**2, range(8)))
print(squares)

squares = [x**2 for x in range(8)]
print("square = ", squares)

print("".center(72, "x"))

print("list = ", [(x, y) for x in [1, 2, 3] for y in [3, 1, 4]])
print(
    "list sans mêmes valeurs pour x et y =\n",
    [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y],
)
print(
    "Tables de multiplication =\n",
    [(x, y, x * y) for x in range(0, 11) for y in range(0, 11) if x == y],
)

print("".center(72, "x"))

l = [8, 9, 7, 5, 7, 6]
l = list(set(l))
l.sort()

print("l:", globals().get("l", "null"))
print()
print((7 * " - ").center(71, "x"))
print()

s = l.copy()
l.append(4)
print("l:", globals().get("l", "null"))

s = l.pop()

print("r:", globals().get("r", "null"))
print("l:", globals().get("l", "null"))
print("s:", globals().get("s", "null"))

print("".center(72, "x"))

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print(list(queue))  # Remaining queue in order of arrival
queue.popleft()  # The first to arrive now leaves
print(list(queue))  # Remaining queue in order of arrival
queue.popleft()  # The second to arrive now leaves
print(queue)  # Remaining queue in order of arrival
queue.appendleft("Lionel")
print(queue)  # Remaining queue in order of arrival
queue.rotate(-2)
print(queue)

print("".center(72, "x"))

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print("".center(72, "x"))

from math import pi

nl = [str(round(pi, i)) for i in range(1, 6)]
print(nl)

print("".center(72, "x"))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
print(*matrix)
print([[row[i] for row in matrix] for i in range(4)])
print("row becomes columns:")
print([row for row in matrix])
print(list(zip(*matrix)))


print("".center(72, "x"))

a = list({x for x in "abracadabra"}) # equiv set()
a.sort()
print(a)

print("".center(72, "x"))

import math

raw_data = [56.2, float("NaN"), 51.7, 55.3, 52.5, float("NaN"), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

print("".center(72, "x"))

print(sorted([n for n in raw_data if not math.isnan(n)]))

print("".center(72, "x"))

# Utilisation de l'opérateur := dans une boucle for
my_list = [1, 2, 3, 4, 5]
for i, item in enumerate(my_list):
    if (i := i + 1) % 2 == 0:
        print(f"L'élément {item} est à la position {i}.")

print("".center(72, "x"))

s = "(1, 2, 3) < (1, 2, 4)"
parts = s.split(" < ")

a = eval(parts[0])
b = eval(parts[1])
result = eval(parts[0]) < b

print(f"{a} < {b} → {result}")
