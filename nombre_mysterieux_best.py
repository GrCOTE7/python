import random

(lambda f: f(f, 0, 1000, random.randint(1, 1000), 1))(
    lambda self, min_val, max_val, x, tour: print(
        f"Tour #{tour}: {min_val} < x ? < {max_val}"
    )
    or (
        lambda guess: (
            print(
                f"Bravo ! Tu as assuré et trouvé le nombre mystérieux en {tour} tours !"
            )
            if guess == x
            else (
                self(self, guess, max_val, x, tour + 1)
                if guess < x
                else self(self, min_val, guess, x, tour + 1)
            )
        )
    )(int(input()))
)
