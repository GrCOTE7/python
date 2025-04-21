GUESTS_NUMBER = 10
COFFEE_PER_GUEST = 400


def serve_group():
    """Sert un groupe de clients affamés.

    S'assure d'une expérience inoubliable !
    """
    greet_guests()
    spoons = 0
    table_number = prepare_table()
    for guest in range(GUESTS_NUMBER):
        # print(guest)
        spoons += lay_spoons_on_table(2)

    

    coffee=fill_water_carafe()

    return spoons, coffee


def greet_guests():
    """Accueille les clients avec chaleur et amabilité."""
    # Add your code here to greet the guests


def prepare_table():
    """Prépare une table pour le nombre spécifié de clients."""
    tables_number = 0
    for i in range(GUESTS_NUMBER):
        tables_number += i
        print(f"Table {i+1} préparée")
    return tables_number
    # Add your code here to prepare the table


def lay_spoons_on_table(num_spoons):
    """Place le nombre spécifié de cuillères sur la table."""
    # Add your code here to lay spoons on the table
    return num_spoons


def fill_water_carafe():
    """Remplit la carafe d'eau avec la quantité spécifiée."""
    # Add your code here to fill the water carafe
    return GUESTS_NUMBER * COFFEE_PER_GUEST
    pass


guests,coffee_quantity = serve_group()
print(f"Nombre de convives: {guests} et quantité de café: {coffee_quantity} ml.")
