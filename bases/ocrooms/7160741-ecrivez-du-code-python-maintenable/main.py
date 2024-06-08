"""Code maintenable"""

from re import L


def main():
    """Main script"""
    test()


def test():
    """Test script"""
    letters = ["a", "b", "c", "d", "e"]
    length = len(letters)

    while True:

        try:
            message = input(
                f"Tapez un index de 0 à {length} pour accéder à l'élement : "
            )
            index = int(message)
            print("Vous accédez à l'élément", letters[index])
            break
        except ValueError as exc:
            raise ValueError(f"{message} n'est pas un chiffre !") from exc

        except IndexError:
            continue
        except KeyboardInterrupt:
            print("Fin.")
            break


if __name__ == "__main__":
    main()
