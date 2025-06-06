from re import S
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *

if __name__ == "__main__":
    cls(" old.algorea.org_chap7")

    def resolve(d, f, ps):
        print(sum(1 for p in ps if p[0] <= f and p[1] >= d))

    def case():

        n = 3

        minTemp = 0
        maxTemp = 100

        # n, minTemp, maxTemp = (int(input()) for _ in range(3))

        tps = [15,50,75]

        for i in range(n):
            # t= minTemp <= int(input()) <= maxTemp
            t= minTemp <= tps[i] <= maxTemp
            print("Rien à signaler" if t else "Alerte !!")
            if not t:
                break  # Sortir de la boucle dès qu'une alerte est affichée

        # for i in range(n):
        #     temp = random.randint(minTemp, maxTemp)
        #     print(f"La température est de {temp}°C")

        pass

    case()

    exit()

#################
# Souvenir du Grand Evènement
#################
# Zones de couleur
# print(*[
#     next(
#         (
#             "Dans une zone " + z[0]
#             for z in [
#                 ["jaune", [(25, 20), (50, 45)]],
#                 ["bleue", [(10, 10), (85, 55)]],
#                 ["rouge", [(15, 60), (45, 70)]],
#                 ["rouge", [(60, 60), (85, 70)]],
#                 ["jaune", [(0, 0), (90, 70)]],
#             ]
#             if c[0] >= z[1][0][0]
#             and c[0] <= z[1][1][0]
#             and c[1] >= z[1][0][1]
#             and c[1] <= z[1][1][1]
#         ),
#         "En dehors du théâtre",
#     )
#     for c in [(int(input()), int(input())) for _ in range(int(input()))]
# ],
# sep="\n"
# )
#################
# L'espion est démasqué
# print(
#     *[
#         [
#             "Impossible",
#             "Peu probable",
#             "Peu probable",
#             "Probable",
#             "Probable",
#             "Très probable",
#         ][sum([178 <= t <= 182, a >= 34, p < 70, c == 0, b == 1])]
#         for t, a, p, c, b in [
#             (
#                 int(input(f"Enter value for {label}: "))
#                 for label in ["t", "a", "p", "c", "b"]
#             )
#             for _ in range(int(input("Enter the number of people: ")))
#         ]
#     ],
#     sep="\n",
# )

#################
# Sur la piste de l'espion
# print(
#     (
#         lambda d, f, n: sum(
#             1
#             for e, s in [(int(input()) for _ in range(2)) for _ in range(n)]
#             if e <= f and s >= d
#         )
#     )(*[int(input()) for _ in range(3)])
# )
