import sys
from pathlib import Path
from turtle import st
from tabulate import tabulate
from operator import itemgetter, attrgetter

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import dg, fg, lg, cls, exit, pf

cls("Sorts 1/2 ()")

if __name__ == "__main__":

    # print("{0: ^55}".format(f"{dg}{' Sorts 1/2 ': ^55}{fg}\n"))
    print(
        f"Note: Parties séparées par des :\n    exit()  #################################\n{f'{dg}→ Les commenter progressivement...{fg}': >55}"
    )

    # exit()  #################################

    print(
        tabulate(
            [
                [f"{dg}list.sort(){fg}", "Oui", "Non"],
                [f"{dg}sorted(list){fg}", "Non", "Oui"],
            ],
            headers=["Méthode", "Original modifié?", "Retourne new liste"],
            tablefmt="rounded_outline",
        )
    )

    print(lg)
    import time

    # time.sleep(1)
    exit()  #################################

    print()
    student_tuples = [
        ("john", "M", 15000),
        ("dave", "M", 10000),
        ("anna", "F", 7000),
    ]

    print("Sorted() on iterables:\n\n  Name  |  Sex   |  Note  ")
    print("--------|--------|--------")
    for student in sorted(student_tuples, key=lambda student: student[2]):
        print(
            f" {student[0][0].upper()+student[0][1:]:<6} | {student[1]:^6} | {student[2]:>6} "
        )
    print(lg)

    print("\nSorted().reverse() on iterables:\n\n  Name  |  Sex   |  Note  ")
    print("--------|--------|--------")
    for student in sorted(student_tuples, key=lambda student: student[2], reverse=True):
        print(
            f" {student[0][0].upper()+student[0][1:]:<6} | {student[1]:^6} | {student[2]:>6} "
        )
    print(lg)

    exit()  #################################

    class Student:
        def __init__(self, name, sex, age=None, note=None):
            self.name = name
            self.sex = sex
            self.age = age
            self.note = note

        def __repr__(self):
            return repr((self.name, self.sex, self.age, self.note))

    student_objects = [
        Student("john", "M", 25, 15),
        Student("dave", "M", 25, 13),
        Student("anna", "F", 21, 7),
    ]
    so = student_objects[::]

    pf("student_objects[0]")
    print("type(so):", type(so), "\n" + str(list(so)), end="\n" + "-" * 55 + "\n")
    pf("vars(so[0])")
    pf("vars(so[0]).keys()")
    pf("vars(so[0]).values()")

    exit()  #################################

    print("Sorted() on objects: (Sorted by age)\n\n  Name  |  Sex   |  Age   |  Note  ")
    print("--------|--------|--------|--------")
    # for student in sorted(student_objects, key=lambda student: student.age):
    # → Intéressant si opérations complexes / tri
    for student in sorted(student_objects, key=attrgetter("age"), reverse=False):
        # → +rapide si simple récupération d'attribut sans traitement
        print(
            f"  {(student.name[0]).upper()+student.name[1:]:<5} | {student.sex:^6} | {student.age:>5}  | {student.note:>5}  "
        )
    print(lg + "\n")

    exit()  #################################

    import pprint

    sorted_arr = sorted(student_tuples, key=itemgetter(1), reverse=True)
    pprint.pprint(sorted_arr, width=20)
    print(lg)

    exit()  #################################

    from prettytable import PrettyTable

    print("\n" + dg + "'PrettyTable' librairy :".center(55) + fg + "\n")
    table = PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide", 1295, 1158259, 600.5])
    table.add_divider()
    table.add_row(["Brisbane", 5905, 1857594, 1146.4], divider=True)
    table.add_rows(
        [["Darwin", 112, 120900, 1714.7], ["Hobart", 1357, 205556, 619.5]], divider=True
    )
    table.add_row(["Melbourne", 1566, 3806092, 646.9])
    table.add_row(["Perth", 5386, 1554769, 869.4])
    table.add_row(["Sydney", 2058, 4336374, 1214.8])

    print(table)

    print("\n" + dg + "All 'tabulate' librairy types :".center(55) + fg + "\n")

    # exit()  #################################
    tabulate_types = (
        "plain",
        "simple",
        "github",
        "grid",
        "outline",
        "simple_grid",
        "heavy_grid",
        "heavy_outline",
        "mixed_grid",
        "mixed_outline",
        "double_grid",
        "double_outline",
        "fancy_grid",
        "simple_outline",
        "fancy_outline",
        "rounded_grid",
        "rounded_outline",
        "orgtbl",
        "asciidoc",
        "jira",
        "presto",
        "pretty",
        "psql",
        "rst",
        "mediawiki",
        "moinmoin",
        "youtrack",
        "html",
        "unsafehtml",
        "latex",
        "latex_raw",
        "latex_booktabs",
        "latex_longtable",
        "textile",
        "tsv",
    )

    nb = len(tabulate_types)
    for i, tt in enumerate(tabulate_types):
        print(f"{dg}{tt: >40}{fg} ({i+1} / {nb})")
        table = tabulate(
            student_tuples,
            headers=["Name", "Sex", "Note"],
            tablefmt=tt,
            # showindex="always",
            intfmt=" ",
            colalign=("left", "center", "right"),
        )
        print(table)
        if i != nb - 1:
            print(lg, "777")

    print(lg * 2)

    exit()  #################################

    import locale

    locale.setlocale(locale.LC_ALL, "fr_FR")
    print("\n", f"{dg}{'Pour test rapide': >40}{fg}")

    print(
        "Au + simple :\n\n"
        + tabulate(student_tuples, headers=["Name", "Sex", "Note"])
        + "\n"
    )

    # Insertion d'un enregistrement None
    student_tuples.insert(2, None)

    formatted_student_tuples = []
    visible_indexes = []
    current_index = 0

    for student in student_tuples:
        if student is None:
            visible_indexes.append(None)
            formatted_student_tuples.append(["", "", ""])
        else:
            name, sex, note = student
            formatted_student_tuples.append(
                (
                    name[0].upper() + name[1:],
                    sex,
                    (locale.format_string("%.2f", note, grouping=True)),
                )
            )
            visible_indexes.append(
                current_index
            )  # Ajouter uniquement les index valides
            current_index += 1

    table = tabulate(
        formatted_student_tuples,
        headers=["Name", "Sex", "{0:^9} ".format("Note")],
        tablefmt="rounded_outline",
        # tablefmt="html",
        showindex=visible_indexes,
        colalign=("right", "left", "center", "right"),
        # maxcolwidths=[None, 20],
    )

    print("Avec formattages et ligne vide :\n" + table, end="")
    print("\n" + lg + "\n")

    exit()  #################################

    data = [("red", 1), ("blue", 1), ("red", 2), ("blue", 2)]
    print(tabulate(data, headers=["Color", "Order"]) + "\n")

    data = sorted(data, key=itemgetter(0))
    print(tabulate(data, headers=["Color", "Order"]))

    exit()  #################################

    print(lg + "\n")

    print(dg + "Students sorts :".center(55) + fg + "\n")

    students = [
        [
            student.name[0].upper() + student.name[1:],
            student.sex,
            student.age,
            student.note,
        ]
        for student in student_objects
    ]

    def capitalize_name(row):
        row[0] = row[0].capitalize()
        return row

    def tbl(tbl=None):
        # print(type(tbl))
        # Conversion des éléments en listes pour les rendre modifiables
        data_as_list = [list(row) for row in tbl]
        tbl = list(map(capitalize_name, data_as_list))
        print(
            tabulate(
                tbl,
                headers=["Nom", "Sexe", "Âge", "Note"],
                tablefmt="rounded_outline",
                colalign=("left", "center", "right", "right"),
            )
        )

    print("Liste d'objets originale :")
    tbl([vars(student).values() for student in student_objects])

    print("Liste d'itérables originale :")
    tbl(students)

    print("Liste d'itérables triée par le 1er critère ('Nom') :")
    sorted_students = sorted(students)
    tbl(sorted_students)

    print(
        f"Itérable → {dg}itemgetter(){fg}\nListe triée par 1 critère ('Âge' décroissant) :"
    )
    sorted_students = sorted(students, key=itemgetter(2), reverse="True")
    tbl(sorted_students)

    # Tri des objets par 'âge' décroissant
    sorted_students = sorted(student_objects, key=attrgetter("note"), reverse=True)
    # Transformation des objets en liste tabulaire pour tabulate
    formated_students = [[s.name, s.sex, s.age, s.note] for s in sorted_students]
    # Affichage
    print(
        f"Objects → {dg}attrgetter(){dg}\nListe triée par 1 critère ('Note' décroissante) :"
    )
    tbl(formated_students)

    exit()  #################################

    print(lg)

    print(f"{dg}Alternative + compacte (Pas de tri) :{fg}")
    tbl([vars(student).values() for student in student_objects])

    print(f"\n{dg}Alternative + compacte (Tri par nom) :{fg}")
    sorted_data_by_name = sorted(
        [list(vars(student).values()) for student in student_objects],
        key=lambda x: x[3],
    )

    tbl(sorted_data_by_name)

    print(
        "Trié par nom:\n",
        tabulate(
            sorted(
                [list(vars(student).values() for student in student_objects)],
                key=lambda x: x[1],
            )
        ),
    )

    print("Trié par nom:")
    tbl(sorted([list(vars(student).values()) for student in student_objects]))
    print(lg)

    print("Trié par notes décroissantes:")
    tbl(
        sorted(
            [list(vars(student).values()) for student in student_objects],
            key=lambda x: x[3],
            reverse="True",
        )
    )
    print(lg)

    print("Liste d'itérables triée par 3 critères ('Âge', 'Sexe' puis 'Nom') :")
    # sorted_students = sorted(students, key=itemgetter(2, 1, 0))
    # tbl(sorted_students)

    print("Liste d'objets triée par 2 critères ('Âge', 'Sexe' descendant) :")
    sorted_students = sorted(students, key=itemgetter(2, 1, 0))
    # sorted_students = sorted(students, key=itemgetter(2, 1, 0))
    tbl(sorted_students)
    print(lg * 2)

    exit()  #################################

    def multisort(xs, specs):
        for key, reverse in reversed(specs):
            xs.sort(key=attrgetter(key), reverse=reverse)
        return xs

    print("Liste d'objets triée par 2 critères ('Âge' descebdabt, puis 'Note') :")
    tbl([list(vars(student).values()) for student in so])
    new_so = multisort(list(student_objects), (("age", True), ("note", False)))
    tbl([list(vars(student).values()) for student in list(new_so)])
    print("\n" + "x" * 55)

    print(type(student_objects[0]), student_objects[0])
    print(type(so), so)
    print(type(so), list(so))
    print(vars(so[0]))
    print(vars(so[0]).keys())
    print(vars(so[0]).values())
    print(list(vars(so[0]).values()))

    print(lg)

    decorated = [(student.sex, i, student) for i, student in enumerate(student_objects)]
    decorated.sort()

    pf("decorated")

    print([student for grade, i, student in decorated])

    exit()  #################################
