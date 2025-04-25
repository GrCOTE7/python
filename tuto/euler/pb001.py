import sys
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import nf, dg, fg, lg, cls, exit, pf, chrono

cls("Exercice EULER # 001")

if __name__ == "__main__":

    nb = 100000  # Nombre d'itérations

    bound = 1000
    # exit()

    @chrono
    def euler1_01(nTimes=1):
        for i in range(nTimes):
            s = sum(i for i in range(1, bound) if not i % 3 or not i % 5)

        print("\n#1 → ", int(s))
        return s

    @chrono
    def euler1_02(nTimes=1):
        for i in range(nTimes):
            s = (
                1.5 * (int)((bound - 1) / 3) * (int)((bound + 2) / 3)
                + 2.5 * (int)((bound - 1) / 5) * (int)((bound + 4) / 5)
                - 7.5 * (int)((bound - 1) / 15) * (int)((bound + 14) / 15)
            )
        print("\n#2 → ", int(s))
        return s

    @chrono
    def euler1_03(nTimes=1):

        def sumial(n):
            return n * (n + 1) / 2

        def sumOfMultiples(n, bound):
            return sumial((bound - 1) // n) * n

        multiples = [3, 5]
        for i in range(nTimes):
            r = (
                sumOfMultiples(3, bound)
                + sumOfMultiples(5, bound)
                - sumOfMultiples(3 * 5, bound)
            )
        print("\n#3 →", int(r))
        return r

    @chrono
    def euler1_04(nTimes=1):

        t = (bound - 1) // 3
        f = (bound - 1) // 5
        x = (bound - 1) // 15
        r = 3 * t * (t + 1) / 2 + 5 * f * (f + 1) / 2 - 15 * x * (x + 1) / 2
        print("\n#4 → ", int(r))
        return r

    @chrono
    def euler1_05(nTimes=1):

        x = bound - 1
        a = 3
        b = 5

        def sum(a, x):
            b = x // a
            return a * b * (b + 1) // 2

        res = sum(a, x) + sum(b, x) - sum(a * b, x)
        # sum (a,x) est la somme des multime de a jusqu'a x
        print("\n#5 → ", int(res))
        return res

    @chrono
    def euler1_06(nTimes=1):

        import time

        start_time = time.time()
        for i in range(10000000):
            # the values given in the problem
            num1 = 3
            num2 = 5
            max = 1000
            sum = 0
            # add the sum of all multiples of 3 less than 1000
            i = 1
            while i * num1 < max:
                sum = sum + i * num1
                i = i + 1
            # add the sum of all multiples of 5 less than 1000
            i = 1
            while i * num2 < max:
                sum = sum + i * num2
                i = i + 1
                # do not add any number that is a multiple of 3
                if i % 3 == 0:
                    i = i + 1
        print(sum)
        print("Time Elapsed: %.3f s" % (time.time() - start_time))
        return nf(sum) + " Time Elapsed: %.3f s" % (time.time() - start_time)

    @chrono
    def euler1_07(nTimes=1):

        import time

        start_time = time.time()
        for i in range(1000000):
            # the values given in the problem
            f = lambda a, n, d: (n * (2 * a + (n - 1) * d)) // 2
            res = f(3, 999 // 3, 3) + f(5, 999 // 5, 5) - f(15, 999 // 15, 15)
        print(res)
        print("Time Elapsed: %.3f s" % (time.time() - start_time))
        return nf(res) + " Time Elapsed: %.3f s" % (time.time() - start_time)

    # euler1_01(nb)
    # euler1_03(nb)

    # for i in range(3, 11):
    #     bound = 10**i
    #     print(f"{nf(bound,0)} (10 ** {i})".center(55))
    #     euler1_02(nb)
    #     euler1_04(nb)
    #     print(lg)

    euler1_04(nb)
    euler1_05(nb)
    # euler1_06(nb)
    euler1_07(nb)

    print(3 * 333 * 334 / 2 + 5 * 199 * 200 / 2 - 15 * 66 * 67 / 2)

    # print(*range(10))

    exit()
