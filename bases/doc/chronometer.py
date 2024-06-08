from time import time, sleep


def chrono(function):
    """calcule le temps que met une fonction à s'executer."""

    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # On appelle cela le temps "epoch".
        start = time()

        result = function(*args, **kwargs)

        end = time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans
        # "start", et celui qui sera gardé dans votre variable 'end'. ;)
        time_spent = end - start
        print(f"{args[0]}: {time_spent:.2f}\"")

        return result
    wrapper.__doc__ = function.__doc__
    return wrapper


@chrono
def calculate_the_trajectory(value):
    """Calcule la trajectoire du vaisseau."""
    print("Calcul en cours...")
    sleep(3)  # on met le programme en pause pendant 3 secondes !
    print("Calcul terminé !")


if __name__ == "__main__":
    calculate_the_trajectory("Vol")
