def getInitialList(data):
    """
    À partir de data, on construit une liste qui servira de départ pour le tri
    Args:
        (bool) twice: True si on peut avoir des doublons, False sinon)
    Returns:
        array: Un tableau, base du tri | None si échoue à le créer
    """

    if validData(data):

        import random

        liste = (
            random.choices( 
                range(data["min_value"], (int)(data["max_value"] + 1)),
                k=(int)(data["numbers_number"]),
            )
            if data["twice_authorized"]
            else random.sample(
                range(data["min_value"], (int)(data["max_value"] + 1)),
                (int)(data["numbers_number"]),
            )
        )
        return liste


def validData(data):
    """
    Return True si les données sont valides, sinon False
    Args :
        data (dict): (int) minima, (int) maxima, (int) nombre de nombres, (bool) double accepté

    Returns :
        bool : True si toutes les entrées cohérentes sinon False
    """
    return (
        data["numbers_number"] > 1
        and data["max_value"] <= 1e18
        and data["min_value"] <= data["max_value"]
        and data["numbers_number"] <= (data["max_value"] - data["min_value"] + 1)
        if not data["twice_authorized"]
        else True
    )


if __name__ == "__main__":

    data = {
        "max_value": 5,  # Dans les données,  valeur maximum des items - Max: 1e18 (Soit 1 suivi de 18 zéros))
        "numbers_number": 5,  # Mini 1e0 + 1 (Soit 2)
        "min_value": 1,  # Dans les données,  valeur minimale des items (Max: 1e18)
        "twice_authorized": 0,  # 0 : Pas de double 1 si OK
    }

    print(getInitialList(data))
