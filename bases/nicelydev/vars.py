def msg():
    print()

    nombres = 1, 2, 3, 1  # tuple
    nombresSet = set(nombres)
    print(nombresSet)
    
    informations = {"Mélanie", 10, 23, "Henrique"}
    print(informations)
    print(tuple(informations)[1])

    nombres = {50, 50, 50, 10, 23, 12}
    print(nombres)
    # Affiche : {50, 10, 12, 23}

    prenoms = {'Pier', 'Pol', 'Jack'}
    print(prenoms)
    print('Pol' in prenoms)
    
    prenoms.add('Juda')
    print(prenoms)
    
    prenoms.remove('Pol')
    print(prenoms)

    print()
if __name__ == "__main__":
    msg()
