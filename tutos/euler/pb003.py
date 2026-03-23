import sys, time
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import cls, nf, SB, EB, exit, sl

if __name__ == "__main__":

    cls("Exercice EULER # 003")

    def generate_primes(limit):
        primes = []
        num = 2  # Premier nombre premier

        while len(primes) < limit:
            # Vérifie si num est premier
            is_prime = all(num % p != 0 for p in primes)
            if is_prime:
                primes.append(num)
            num += 1  # Passe au nombre suivant

        return primes

    def prime_factors(n):
        factors = []

        # Vérifie le facteur 2 en premier
        while n % 2 == 0:
            factors.append(2)
            n //= 2

        # Vérifie les facteurs impairs à partir de 3
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                factors.append(factor)
                n //= factor
            factor += 2

        # Si n est toujours > 1, c'est un facteur premier
        if n > 1:
            factors.append(n)

        return factors

    # Exemple d'utilisation
    num = 13195  # Remplace par ton nombre
    factors = prime_factors(num)
    print(
        f"Facteurs premiers de {num} : {factors},\nle + grand étant donc: {SB}{str(max(factors))}{EB}\n"
    )
    sl()

    # Exemple : générer les 20 premiers nombres premiers
    print(*generate_primes(20))

    exit()
    # print(f"{nf(a, 0): >10}")
