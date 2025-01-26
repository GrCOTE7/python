def msg():
    a = 12
    d = 45
    ville = "paris"
    note = 10
    pays = "france"
    age = 18
    print(1)
    print(ville.capitalize() + " est la capitale de la " + pays.capitalize() + ".")
    print(2)
    print(ville.capitalize(), "est la capitale de la", pays.capitalize() + ".")
    print(3)
    print("%s est la capitale de la %s." % (ville.capitalize(), pays.capitalize()))
    print(4)
    print(f"{ville.capitalize()} est la capitale de la { pays.capitalize()}.")
    print(5)
    print("{} est la capitale de la {}.".format(ville.capitalize(), pays.capitalize()))
    print()


if __name__ == "__main__":

    msg()
