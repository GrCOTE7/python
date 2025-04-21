from time import time, sleep


def calculate_time_spent(function):
    """calcule le temps que met une fonction à s'executer."""

    def wrapper():
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # On appelle cela le temps "epoch".
        start = time()

        result = function()

        end = time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans
        # "start", et celui qui sera gardé dans votre variable 'end'. ;)
        time_spent = end - start
        print(f"Secondes passées: {time_spent:.2f}")

        return result

    return wrapper


@calculate_time_spent
def calculate_the_trajectory():
    """Calcule la trajectoire du vaisseau."""
    print("Calcul en cours...")
    sleep(3)  # on met le programme en pause pendant 3 secondes !
    print("Calcul terminé !")


calculate_the_trajectory()
