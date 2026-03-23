import sys, time
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import cls, nf, SB, EB, exit

# Réf.: https://projecteuler.net

if __name__ == "__main__":

    cls("Exercice EULER # 001")
    # Bound = 1000
    # 233 168 - Time #  1: 73.068 s pour 1 000 000 fois
    # 233 168 - Time #  2:  0.576 s pour 1 000 000 fois
    # 233 168 - Time #  3:  0.606 s pour 1 000 000 fois
    # 233 168 - Time #  4:  0.414 s pour 1 000 000 fois
    # 233 168 - Time #  5:  0.517 s pour 1 000 000 fois
    # 233 168 - Time #  6: 35.559 s pour 1 000 000 fois
    # 233 168 - Time #  7:  0.582 s pour 1 000 000 fois
    # 233 168 - Time #  8:  0.403 s pour 1 000 000 fois

    # @chrono
    def euler1_01(nTimes=1):
        start_time = time.time()
        for i in range(nTimes):
            res = sum(i for i in range(1, bound) if not i % 3 or not i % 5)
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{1: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_02(nTimes=1):
        start_time = time.time()
        for i in range(nTimes):
            res = (
                1.5 * (int)((bound - 1) / 3) * (int)((bound + 2) / 3)
                + 2.5 * (int)((bound - 1) / 5) * (int)((bound + 4) / 5)
                - 7.5 * (int)((bound - 1) / 15) * (int)((bound + 14) / 15)
            )
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{2: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_03(nTimes=1):

        def sumial(n):
            return n * (n + 1) / 2

        def sumOfMultiples(n, bound):
            return sumial((bound - 1) // n) * n

        start_time = time.time()
        multiples = [3, 5]
        for i in range(nTimes):
            res = (
                sumOfMultiples(3, bound)
                + sumOfMultiples(5, bound)
                - sumOfMultiples(3 * 5, bound)
            )
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{3: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_04(nTimes=1):

        start_time = time.time()
        for i in range(nTimes):

            t = (bound - 1) // 3
            f = (bound - 1) // 5
            x = (bound - 1) // 15
            res = 3 * t * (t + 1) / 2 + 5 * f * (f + 1) / 2 - 15 * x * (x + 1) / 2
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{4: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_05(nTimes=1):

        start_time = time.time()
        for i in range(nTimes):

            def sum(a, x):
                b = x // a
                return a * b * (b + 1) // 2

            x = bound - 1
            a = 3
            b = 5
            res = sum(a, x) + sum(b, x) - sum(a * b, x)
            # res(a,x) est la somme des multiples de a jusqu'a x
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{5: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_06(nTimes=1):

        import time

        start_time = time.time()
        for i in range(nTimes):
            # the values given in the problem
            num1 = 3
            num2 = 5
            max = bound
            res = 0
            # add the sum of all multiples of 3 less than 1000
            i = 1
            while i * num1 < max:
                res = res + i * num1
                i = i + 1
            # add the sum of all multiples of 5 less than 1000
            i = 1
            while i * num2 < max:
                res = res + i * num2
                i = i + 1
                # do not add any number that is a multiple of 3
                if i % 3 == 0:
                    i = i + 1

        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{6: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_07(nTimes=1):

        import time

        start_time = time.time()
        for i in range(nTimes):
            # the values given in the problem
            limit = bound - 1
            f = lambda a, n, d: (n * (2 * a + (n - 1) * d)) // 2
            res = f(3, limit // 3, 3) + f(5, limit // 5, 5) - f(15, limit // 15, 15)
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{7: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # @chrono
    def euler1_08(nTimes=1):

        import time

        start_time = time.time()
        for i in range(nTimes):
            l = bound - 1  # limit
            nm3 = l // 3  # Nombre de multiples
            m3 = (
                3 * nm3 * (nm3 + 1) / 2
            )  # somme de tous les multiples de 3 dans la limite
            nm5 = l // 5
            m5 = 5 * nm5 * (nm5 + 1) / 2
            nm15 = (bound - 1) // 15
            m15 = 15 * nm15 * (nm15 + 1) / 2

            res = m3 + m5 - m15
        print(
            nf(res, 0),
            "-",
            f"Time #{SB}{8: >3}{EB}: %.3f s pour %s fois"
            % (time.time() - start_time, nf(nTimes, 0)),
        )
        return nf(res) + " Time: %.3f s" % (time.time() - start_time)

    # euler1_01(nb)
    # euler1_03(nb)

    pownb = 3
    nb = 10**pownb  # Nombre d'itérations

    pow = 3
    # bound = 10**pow
    bound = 1000

    print(
        f"limite = {nf(bound,0)} (10**{SB}{pow}{EB})".center(63) + "\n"
    )  # 63 au lieu de 55 car {dg & {fg} = car. invisibles}
    # exit()

    # euler1_01(nb)
    euler1_02(nb)
    euler1_03(nb)
    euler1_04(nb)
    euler1_05(nb)
    # euler1_06(nb)
    euler1_07(nb)
    euler1_08(nb)

    # print(*range(10))

    exit()
