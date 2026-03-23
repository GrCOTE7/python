import time
import numpy as np

import locale


def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    f = float(f)
    return locale.format_string(f"%.{dec}f", f, grouping=True)


N = 10_000_000
# N = 10
lst = list(range(N))
arr = np.array(lst)

# Liste Python
start = time.perf_counter()
lst_result = [x * 2 for x in lst]
end = time.perf_counter()
print(f"{"Liste (Py)":<10}:", nf(end - start, 3))

# NumPy
start = time.perf_counter()
arr_result = arr * 2
end = time.perf_counter()
print(f"{"NumPy":<10}:", nf(end - start, 3))

# print("lst:", *lst, "→", *lst_result)
# print("arr:", *arr, "→", *arr_result)
