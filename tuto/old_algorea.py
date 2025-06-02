from re import S
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *

# Réf.: https://www.france-ioi.org/
# Code Démo Algorea: m5iycsiw
# Code ALGORÉA: yqp4gbnf

if __name__ == "__main__":
    cls(" old.algorea.org")

    def resolve(d, f, ps):
        print(sum(1 for p in ps if p[0] <= f and p[1] >= d))

    def case():

        pass

    case()

    exit()


#############
# print(
#     (
#         lambda d, f, n: sum(
#             1 for _ in range(n) if d <= int(input(f"v {_+1} ? ")) <= f
#         )
#     )(*[int(input(prompt)) for prompt in ["D ? ", "F ? "]], int(input("n ? ")))
# )
#############
# xys = [1, 6, 1, 5, 4, 9, 3, 8, 7, 6, 7, 5, 1, 5, 1, 8]
# print(
#     '\n'.join("NON"
#     if (nums := xys[i:i+8])
#     and (nums[1] <= nums[4] or nums[6] <= nums[0])
#     or (nums[3] <= nums[6] or nums[7] <= nums[2])
#     else "OUI"
#     for i in range(0, len(xys), 8)
#     )
# )
#############
# print(s if (vals := [int(input()) for _ in range(2)]) and (s := sum(vals)) else 0)
# print((nums := [1, 6, 1, 55]) and 'Max: ',nums[3], 'et', nums, "→", sorted(nums, reverse=True))
# print((nums := [1, 6, 1, 55]) and (sorted(nums, reverse=True)))
# print(*[(i, j) for i in range(2) for j in range(n)])
# print("Amies" if (nums := [int(input()) for _ in range(4)])[1] >= nums[2] and nums[3] >= nums[0] else "Ne se connaissent pas encore")
# print("↑" if (nums := [int(input("Enter a number: ")) for _ in range(2)])[0] < nums[1] else "↓")
# print('↑' if int(input("Enter a number 1: "))< int(input("Enter a number 2: ")) else '↓')
# print([int(input("Enter a number: ")) for _ in range(2)][1])
#############
# xys = [1, 1, 2, 3, 4, 5, 1, 10, 0, 0, 11, 11]
# inis = [1, 4, 1, 8, len(xys) // 2]
# sss = {}
# xMin, xMax, yMin, yMax, n = (inis[i] for i in range(5))
# print(
#     (
#         sum(
#             1
#             for i in range(n)
#             if (
#                 (x := int(xys[i * 2])) is not None
#                 and (y := int(xys[i * 2 + 1])) is not None
#                 and (
#                     (
#                         xMin <= x <= xMax
#                         and yMin <= y <= yMax
#                         and (sss.update({(x, y): 111}) or True)
#                     )
#                     or (sss.update({(x, y): 222}) and False)
#                 )
#             )
#         ),
#         sss,
#     )
# )


#############
# ops = {}
#         print(
#             sum(
#                 1
#                 for _ in range(int(input("Enter the number of operations: ")))
#                 if (a := int(input("a: "))) + (b := int(input("b: "))) > 4
#                 # Add those that meet the condition
#                 and ops.update({(a, "+", b): a + b})
#                 # Add those that do not meet the condition
#                 or ops.update({(a, "+", b): a + b}) and False
#             ),
#             ops,
#         )
#############
# Example of using list comprehensions for repetitive actions
# actions = [(gauche, 2), (ramasser, 1), (droite, 32), (deposer, 1)]
# [func() for func, count in actions for _ in range(count)]
#############
# Example of a compact input and processing
# print(
#     max(
#         [
#             int(input("Enter value: "))
#             for _ in range(int(input("Enter the number of values: ")))
#         ]
#     )
# )
#############
# Example of a compact simulation
# print(sum(1 for v in [230, 350, 113, 187, 95, 129] if abs(v - 100) >= 10))
#############
# Example of a simple sum of n items
# print(
#     sum(
#         i
#         for i in (
#             int(input("Enter value of item: "))
#             for _ in range(int(input("Enter the number of items: ")))
#         )
#         if i < 10
#     )
# )
#############
# Example of a team weight comparison
# nMembres = int(input("Enter the number of members in each team: "))
# weights = [
#     int(
#         input(
#             f"Enter weight for member {i // 2 + 1} of team {1 if i % 2 == 0 else 2}: "
#         )
#     )
#     for i in range(2 * nMembres)
# ]
# s1, s2 = sum(weights[::2]), sum(weights[1::2])
# print(
#     f"L'équipe {1 if s1 > s2 else 2} a un avantage.\nPoids total pour l'équipe 1 : {s1}\nPoids total pour l'équipe 2 : {s2}"
# )
#############
# Example of a multiplication table
# print(
#     *[
#         " ".join(map(str, row))
#         for row in [[m * n for m in range(1, 6)] for n in range(1, 6)]
#     ],
#     sep="\n",
# )
#############
#  [[ramasser(), *[droite() for _ in range(15)], deposer(), *[gauche() for _ in range(15)],] for i in range(2)]
#############
# aas = [(gauche, 2), (ramasser, 1), (droite, 32), (deposer, 1)]
# [func() for func, count in aas for _ in range(count)]
#############
# Execute each movement the specified number of times
# [
#     eval(f"{mv}()")
#     for movement in movements
#     for mv, count in [
#         (
#             movement.split()[-1],
#             int(movement.split()[0]) if len(movement.split()) > 1 else 1,
#         )
#     ]
#     for _ in range(count)
# ]
#############
# Define the number of values you will input
#     n = int(input("Enter the number of values: "))  # You will enter 6

#     # Collect the values
#     values = [int(input("Enter value: ")) for _ in range(n)]

#     # Find and print the maximum value
#     print(max(values))
# # En concentré :
# print(
#     max(
#         [
#             int(input("Enter value: "))
#             for _ in range(int(input("Enter the number of values: ")))
#         ]
#     )
# )
#####################################
# Simulation:
# pos = 120
# n = 5
# vs = [30, 113, 187, 145, 129]
# print(sum(1 for v in vs if abs(v - pos) <= 25))
# print(
#     sum(
#         (
#             lambda pos=int(input("Enter the pos: ")): (
#                 1
#                 for _ in range(int(input("Enter n: ")))
#                 if abs(int(input("Enter v: ")) - pos) <= 25
#             )
#         )()
#     )
# )
#####################################
# Simple somme de n items:
# print(
#     sum(
#         (
#             lambda n=int(input("Enter the number of items: ")): (
#                 i
#                 for i in (int(input("Enter value of item: ")) for _ in range(n))
#                 if i < 10
#             )
#         )()
#     )
# )
#####################################
# print(
#     (
#         lambda nMembres=int(input("Enter the number of members in each team: ")): (
#             lambda weights: (
#                 lambda format_output: (
#                     f"L'équipe {1 if (s1 := sum(weights[::2])) > (s2 := sum(weights[1::2])) else 2} a un avantage.\n"
#                     f"{format_output(1, s1)}\n"
#                     f"{format_output(2, s2)}"
#                 )
#             )(lambda team, weight: f"Poids total pour l'équipe {team} : {weight}")
#         )(
#             [
#                 int(
#                     input(
#                         f"Enter weight for member {i // 2 + 1} of team {1 if i % 2 == 0 else 2}: "
#                     )
#                 )
#                 for i in range(2 * nMembres)
#             ]
#         )
#     )()
# )
#####################################
# Table de multiplication
# print(*[" ".join(map(str, row)) for row in [[m * n for m in range(1, 6)] for n in range(1, 6)]], sep="\n")
#####################################
# [
#     [
#         ramasser(),
#         *[droite() for _ in range(3)],
#         deposer(),
#         *[gauche() for _ in range(3)],
#         (ls() if i < 1 else None),
#     ]
#     for i in range(2)
# ]
#####################################
# l = 8
# h, b, d, g = "haut", "bas", "droite", "gauche"
# mvs = [(h, l - 1), (d, l - 1), (b, 1)]
# for go_down in range((l - 2) // 2):
#     mvs.extend([(g, l - 2), (b, 1), (d, l - 2), (b, 1)])
# mvs.append((g, l - 1))
# [eval(mv + "()") for mv, n in mvs for _ in range(n)]
#####################################
# 108 tours de 13 kms
# senses = ["haut", "droite", "bas", "gauche"]
# [eval(f"{sens}()") for _ in range(108) for sens in senses for _ in range(13)]
#####################################
# minX, maxX, minY, maxY, n = (int(input()) for _ in range(5))
# print(sum(1 for _ in range(n) if (x := int(input())) and (y := int(input())) and minX <= x <= maxX and minY <= y <= maxY))
#####################################
# d, f, n = (int(input()) for _ in range(3))
# print(sum(1 for _ in range(n) if d <= int(input()) <= f))
#####################################
# n = int(input())
# px = [int(input()) for _ in range(n)]
# print(len(px) - px[::-1].index(min(px))) Donne la dernière pos du min
#####################################
# print(0 if (a := int(input())) == 60 else 5 if a < 10 else 40 if int(input()) >= 20 else 30)
#####################################
# arbres = {
#     "Tinuviel": lambda h, f: h <= 5 and f >= 8,
#     "Calaelen": lambda h, f: h >= 10 and f >= 10,
#     "Falarion": lambda h, f: h <= 8 and f <= 5,
#     "Dorthonion": lambda h, f: h >= 12 and f <= 7,
# }
# h = int(input())
# f = int(input())
# print("".join([nom for nom, test in arbres.items() if test(h, f)]))
#################################
# js = int(input())
# data = [int(input()) for _ in range(js)]
# print(sum(x for x in data if x > 0), sum(-x for x in data if x < 0), sep='\'n')

# print("Tarif", "réduit" if int(input()) < 21 else "plein")

# fs = {name: int(input()) for name in ["Arignon", "Evaran"]}
# print(fs)
# if abs(fs["Arignon"] - fs["Evaran"]) > 10 :
#     print ("La famille", max(fs, key=fs.get), "a un champ trop grand")

# Socles pour statues
# print(sum(list(i**2 for i in range(int(input()), int(input()) - 1, -1))))
# print(*range(100, -1, -1), "Décollage !", sep="\n")
# print("Partie de cache-cache", *range(1, 11), "J'arrive !", sep="\n")

# kms parcourus en 1j, 2j et 3j pour 3 disciplines
# print(*list((2 + 34 + 6) * i for i in range(1, 4)))

# # Parcours une damier lxl une seule fois par case et retour pos de départ
# l = 4
# h, b, d, g = "haut", "bas", "droite", "gauche"
# # Génération des commandes
# mvs = [(h, l - 1), (d, l - 1), (b, 1)]
# for go_down in range((l - 2) // 2):
#     mvs.extend([(g, l - 2), (b, 1), (d, l - 2), (b, 1)])
# mvs.append((g, l - 1))
# # Exécution des mouvements
# for mv in [sens for sens, n in mvs for _ in range(n)]:
#     # eval(mv + "()")
#     print(mv + "()")
# print()

# taille = 4
# tours = taille**2 // 4
# while tours > 0:
#     tours -= 1
#     print(tours)
#     for mvt in ["haut", "droite", "bas", "gauche"]:
#         eval(mvt + "()")
#     print()

# # 108 tours de 13 kms
# for _ in range(108):
#     for mvt in ["haut", "droite", "bas", "gauche"]:
#         for _ in range(13):
#             eval(mvt + "()")
#         print()

# for mvt in [["haut", "droite"], ["gauche", "bas"]]:
#     for _ in range(2):
#         eval(mvt[0] + "()")
#         eval(mvt[1] + "()")

# taille = 40
# for l in range(taille):
#     for r in range(taille // 2):
#         print("XO" if l % 2 else "OX", end="")
#     print()

# for l in range(ord("a"), ord("z") + 1):
#     for _ in range(3):
#         print(chr(l) + "_", end="")
#     print()
