import code
from random import randrange as rr

RESET: str = "\033[0m"
RED: str = "\033[1;31m"
GREEN: str = "\033[1;32m"
YELLOW: str = "\033[1;33m"
BLUE: str = "\033[1;34m"
MAGENTA: str = "\033[1;35m"
CYAN: str = "\033[1;36m"

color_multiplier: float = 1.5
number_multiplier: int = 3
win_popup: str = "Bravo ! Vous avez gagné"
lose_popup: str = "Perdu, vous avez perdu"
number_wheel_start: int = 0
number_wheel_end: int = 49

def start_roulette() -> tuple[int, int]:
    wheel_nb_result: int = rr(number_wheel_end + 1)
    wheel_color_result: int = rr(2)
    
    wheel_result: tuple[int, int] = (wheel_nb_result, wheel_color_result)
    return wheel_result

def ask_amount(wallet_player) -> float:

    amount_error: str = (
        f"montant impossible ou negatif, vous devez renseigner un montant entre {YELLOW}1{RESET} et {YELLOW}{wallet_player}{RESET} (votre wallet)"
    )
    while True:
        mise = input("Combien souhaitez vous miser?")
        try:
            mise = float(mise)
            assert mise > 0

        except ValueError:
            print(amount_error)
            continue

        if mise > wallet_player:
            print(amount_error)

        elif mise <= wallet_player:
            return mise

def transform_wheelcolor_result(wheel_result) -> str:
    if wheel_result[1] == 0:
        color_result_str: str = "noir"
    else:
        color_result_str: str = "rouge"

    return color_result_str


def color_gambl(mise, wheel_result, wallet_player):
    color_result_str: str = transform_wheelcolor_result(wheel_result)
    while True:
        color_gambl_choice = input("Noir ou Rouge? (n/r)").lower()
        if color_gambl_choice == "n":
            color_choice: int = 0
            break
        elif color_gambl_choice == "r":
            color_choice: int = 1
            break
        else:
            print("Ah niqueutamareu")

    if wheel_result[1] == color_choice:
        gain_color: float = mise * color_multiplier
        wallet_player = wallet_player + (gain_color)
        print(f"{win_popup} {GREEN}{gain_color}{RESET}€")
        print(f"{YELLOW}Roulette{RESET}: {color_result_str}")
        return wallet_player
    elif wheel_result[1] != color_choice:
        wallet_player = wallet_player - mise
        print(f"{lose_popup} {RED}{mise}{RESET}€")
        print(f"{YELLOW}Roulette{RESET}: {color_result_str}")
        return wallet_player
    else:
        print("Ah niqueutamareu")
        return wallet_player


def number_gambl(mise, wheel_result, wallet_player) -> float:

    while True:
        number_gambl_choice = input(
            f"Sur quel nombre voulez-vous miser? ({number_wheel_start}-{number_wheel_end})"
        )
        try:
            number_gambl_choice = int(number_gambl_choice)
        except ValueError:

            continue

        if number_gambl_choice == wheel_result[0]:
            gain_number: float = mise * number_multiplier
            wallet_player = wallet_player + (gain_number)
            print(f"{win_popup} {GREEN}{gain_number}{RESET}€")
            print(f"{YELLOW}Roulette{RESET}: {wheel_result[0]}")
            return wallet_player
        else:
            wallet_player = wallet_player - mise
            print(f"{lose_popup} {RED}{mise}{RESET}€")
            print(f"{YELLOW}Roulette{RESET}: {wheel_result[0]}")
            return wallet_player

# ❌ Comprendre le random vu / SeBL4RD pour qu'il arrive à m'faucher 60% de mon K en 3 tours !!! Grrrr !

if __name__ == "__main__":
    wallet_player: float = 500
    while wallet_player > 0:
        print(f"Vous possedez actuellement {BLUE}{wallet_player}{RESET}€.\n")
        player_gambl_type: str = input(
            "Que souhaitez vous miser, couleur, ou nombre? (c/n)"
        ).lower()
        wheel_result = start_roulette()
        if player_gambl_type == "c":
            mise = ask_amount(wallet_player)
            wallet_player = color_gambl(mise, wheel_result, wallet_player)
        elif player_gambl_type == "n":
            mise = ask_amount(wallet_player)
            wallet_player = number_gambl(mise, wheel_result, wallet_player)
        else:
            print("Erreur, recommencez.")
            continue
    print(f"{RED}T'es fauché connard! Dégage!{RESET}")
