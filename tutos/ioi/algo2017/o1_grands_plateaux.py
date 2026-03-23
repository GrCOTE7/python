import flet as ft
import o1_grands_plateaux_cases as gpc


def case(page, ls):
    # nb = int(input())

    l = gpc.case01() # [6, 1, 6, 4, 4, 4, 6, 6] → 4: 3x
    nb = len(l)

    max_nbr = l[0]
    max_cpt = cpt = 1

    for i in range(1, nb):
        if l[i] == l[i - 1]:
            cpt += 1
            if cpt > max_cpt:
                max_cpt = max(cpt, max_cpt)
                max_nbr = l[i]
        else:
            cpt = 1

    print(f"{max_nbr} → {max_cpt}")

    ls()
    page.add(ft.Text(str(l)))
    # print(min_dist)
    page.update()


if __name__ == "__main__":
    case()
    pass
