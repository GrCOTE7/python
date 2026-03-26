import time


def pi(n):
    total = 0
    for i in range(1 - 2 * n, 2 * n + 1, 4):
        total += 1 / i

    return 4 * total


start_time = time.time()
print(pi(100_000_000))
print("Time: %.3f s" % (time.time() - start_time))
