import numpy as np
import time, tools.gc7 as gc7


a = np.random.rand(10_000_000)
b = np.random.rand(10_000_000)
print(a, "→", type(a), gc7.nf(len(a), 0))

start = time.perf_counter()
result = np.sign(b - a)
end = time.perf_counter()
print("np.sign :", end - start)
print("Deltas:", gc7.nf(abs(sum(result)) / 10_000_0, 3), "%")
