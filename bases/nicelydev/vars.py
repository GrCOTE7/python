def msg():
    a = 12
    d = 45
    ville = "paris"
    note = 10
    pays = "france"
    age = 18
    print()
    print("%s est la capitale de la %s." % (ville.capitalize(), pays.capitalize()))
    print()
    print(f"{ville.capitalize()} est la capitale de la { pays.capitalize()}.")
    print()


if __name__ == "__main__":

    msg()
