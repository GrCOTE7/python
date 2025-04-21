from attr import S

Dict = {"Tim": 18, "Charlie": 12, "Tiffany": 22, "Robert": 25}
Boys = {"Tim": 18, "Charlie": 12, "Robert": 25}
Girls = {"Tiffany": 22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
    print(
        *(
            S,
            "(" + ("Masculin" if str(S in Boys.keys()) else "Féminin") + ") : ",
            str(Dict[S]) + " ans",
        )
    )
