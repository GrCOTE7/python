Dict = {"Tim": 18, "Charlie": 12, "Tiffany": 22, "Robert": 25}
Dict.update({"Peter": 21, "Sarah": 23})

Students = list(Dict.keys())
Students.sort()

for S in Students:
    print(": ".join((S, str(Dict[S]))))

print()

Ages = list(Dict.values())
Ages.sort()

for A in Ages:
    for key, value in Dict.items():
        if value == A:
            print(": ".join((key, str(A))))

print("\nLength : %d" % len(Dict))


Boys = {"Tim": 18, "Charlie": 12, "Robert": 25}
Girls = {"Tiffany": 22}


def compare_dicts(dict1, dict2):
    if len(dict1) < len(dict2):
        return -1
    elif len(dict1) > len(dict2):
        return 1
    else:
        # Si les dictionnaires ont la même longueur, comparez les éléments
        for key in dict1:
            if key not in dict2:
                return -1  # ou toute autre logique de comparaison
        return 0  # Les dictionnaires sont considérés comme égaux


print(compare_dicts(Girls, Boys))
