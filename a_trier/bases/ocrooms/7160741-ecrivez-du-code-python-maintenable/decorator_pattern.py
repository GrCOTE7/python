"""Exemple de design pattern decorator"""


def decorate_function(function):
    """Cette fonction va générer le décorateur."""

    # notez *args et **kwargs. Ce sont des paramètres dynamiques
    # qui permet au décorateur de s'adapter à tout type de fonction !
    # N'hésitez pas à vous documenter sur l'unpacking pour en apprendre
    # davantage.
    def wrapper(*args, **kwargs):
        """Voici le "vrai" décorateur.
        C'est ici que l'on change la fonction de base
        en rajoutant des choses avant et après.
        """
        print("Do something at the start (Take off, etc...)")
        result = function(*args, **kwargs)
        print("Do something at the end (Land Ship, etc...)\n")
        return result

    wrapper.__doc__ = function.__doc__
    return wrapper


@decorate_function
def travelling_through(planet_goal):
    """Voyage à travers les étoiles"""
    print(f"{travelling_through.__doc__}: C'est parti pour {planet_goal} !")


# Maintenant, nous pouvons utiliser la fonction décorée directement.

travelling_through("la Lune")
travelling_through("Saturne")
