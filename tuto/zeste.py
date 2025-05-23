import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import cls
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from pf_tools import tbl

# Réf.: https://zestedesavoir.com/tutoriels/2514/un-zeste-de-python/

if __name__ == "__main__":

    cls(" zestedesavoir.com")

    iss = ["i"]
    jss = ["j"]
    ks = ["k"]
    ms = ["m"]
    ns = ["n"]
    gs = ["gris"]
    rs = ["rose"]

    j = -2
    for i in range(12):
        iss.append(i)

        j += 1
        jss.append(j)

        k = i // 6
        ks.append(k)

        m = i
        ms.append(m)
        n = 11 - i
        ns.append(n)

        g = m - k * (m + -n)
        gs.append(g)
        r = 10 - g * 2
        rs.append(r)

        # t = 5 - r / 2
        # ts.append(t

    # tbl([[i for i in range(12)], iss, ps])
    tbl([iss, jss, ks, ms, ns, [], gs, rs])
    # v = (i * 10) // 10 - 11
    # v = ((((v**2) // (v + (v**2) + 1)) * 2) - 1) * (-1) * v
    # for i in range(12):
    #     iss.append(i)

    #     # 1ere solution qui marche
    #     # v = 5 - abs(5 - (i - (1 if i > 5 else 0)))

    #     v = 5 - abs(6 - (i - ((i - 6) // (abs(i - 6) + 1))))

    #     ps.append(v)

    # # tbl([[i for i in range(12)], iss, ps])
    # tbl([iss, ps])

    # print([(5 - abs(5 - i)) for i in range(11)])

    # print([5 - abs(5 - i) for i in range(12) if i != 11])

    # print([(5 - abs(5 - i)) + (1 if i == 6 else 0) for i in range(11)])

    # print([5 - abs(5 - (i - (1 if i > 5 else 0))) for i in range(12)])

    # print([i - ((i - 6) // (abs(i - 6) + 1)) for i in range(12)])
    # print([5 - abs(6 - (i - ((i - 6) // (abs(i - 6) + 1)))) for i in range(12)])

    # print(
    #     [
    #         5
    #         - (
    #             (6 - (i - ((i - 6) // ((i - 6) ** 2 + 1))))
    #             * ((i - 6) // ((i - 6) ** 2 + 1))
    #         )
    #         for i in range(12)
    #     ]
    # )

    # for i in range(-3, 4):
    #     j = i
    #     print(i, j, j // (j * j + 1))

    # print(input().strip())
    # exit()
# 5 4 3 2 1 0 0 1 2 3 4 5
