import sys, time, math
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
from tools import cls, nf, SB, EB, exit, sl, BLUE
from pf_tools import pf

if __name__ == "__main__":

    cls("Exercice EULER # 005")

    sl(BLUE)

    def is_prime(n):
        """Vérifie si n est un nombre premier"""
        if n < 2:
            return False  # 0 et 1 ne sont pas premiers
        if n in (2, 3):
            return True  # 2 et 3 sont les deux premiers premiers !
        if n % 2 == 0 or n % 3 == 0:
            return False  # Élimination rapide des multiples de 2 et 3

        # Vérification jusqu'à √n en utilisant les nombres de la forme 6k ± 1
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True  # Si aucune division n'a réussi, c'est un nombre premier !

    def maFctn(v):
        return str(v) if is_prime(v) else None
        pass

    print(
        "Les nombres premiers jusqu'a 50 sont :\n"
        + ", ".join(filter(None, map(maFctn, range(50))))
    )
    sl()
    # print(is_prime(99991))
    # ls()

    # exit()

    import time
    import math

    # Méthode Progressive
    def gcd(a, b):
        """Calcule le plus grand commun diviseur (PGCD) de a et b"""
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        """Calcule le PPCM de a et b"""
        return a * b // gcd(a, b)

    def progressive_lcm(k):
        """Trouve le PPCM de tous les nombres jusqu'à k"""
        result = 1
        for i in range(2, k + 1):
            result = lcm(result, i)
        return result

    # start = time.time()
    # result = progressive_lcm(7)  # On teste avec k = 20
    # end = time.time()

    # print(f"Résultat: {result}")
    # print(f"Mééthode progressive : {end - start:.7f} secondes")
    # exit()

    # Méthode avec log()

    def primes_up_to(n):
        """Trouve tous les nombres premiers jusqu'à n"""
        primes = []
        for i in range(2, n + 1):
            for p in primes:
                if i % p == 0:
                    break
            else:
                primes.append(i)
        return primes

    def optimized_lcm(k):
        """Calcule le PPCM en utilisant les nombres premiers et leurs puissances maximales"""
        primes = primes_up_to(k)
        N = 1
        limit = math.sqrt(k)

        for i in primes:
            if i <= limit:
                a = math.floor(math.log(k) / math.log(i))
            else:
                a = 1
            N *= i**a

        return N

    # print(progressive_lcm(7))

    ks = [5, 7, 10, 20, 50, 100, 200, 500, 1000]
    methodProg = {}  # Méthode Progressive
    methodLog = {}  # Methode Nombres premiers et log()
    for k in ks:
        start = time.time()
        for i in range(int(1e3)):
            r = progressive_lcm(k)
        end = time.time()
        methodProg[k] = f"{(end - start)*1000:.5f}"
        start = time.time()
        for i in range(int(1e3)):
            r = optimized_lcm(k)
        end = time.time()
        methodLog[k] = f"{(end - start)*1000:.5f}"
        # res.append([k, f"{end - start:.5f}"])

        # s = " ,".join(f"methodProg[{i}]" for i in ks)
        # pf(s, 1)  # @i print('f"{vars=}")
        # s = " ,".join(f"methodLog[{i}]" for i in ks)
        # pf(s, 1)  # @i print('f"{vars=}")

    def PE005(n=20):
        start = time.time()
        prime = primes_up_to(n)  # you need a prime sieve up to n.
        end = time.time()
        print("Without sieve primes:", f"{end - start:.5} secondes")
        res = 1
        for p in prime:
            q = p
            n_p = n // p
            while q <= n_p:
                q *= p
            res *= q
        # return res # for the result itself
        res = str(res)
        return str(len(res))+" car.", res[:7] + "..." + res[-12:]  # nb of digits, start, end

    sys.set_int_max_str_digits(100000)  # Augmente la limite à 10 000 chiffres
    start = time.time()
    k = 1000000
    print(nf(k, 0), PE005(k))
    end = time.time()
    print(f"Autre Méthode + performante : {end - start:.7f} secondes")

    # r = progressive_lcm(int(10e6))
    # end = time.time()
    # print(f"Résultat: {r}")

    exit()
