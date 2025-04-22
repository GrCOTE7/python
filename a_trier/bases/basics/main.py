# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais

# Solution 1
import sys, os
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))

from cls import cls

cls("Script tuto/")

if __name__ == "__main__":

    lg = "\n" + "-" * 55
    print("{0: ^55}".format("Tuple"))
    print()
    print(lg)
    s = "Lionel"
    print(s[2:4])
    print()

    d = dict()
    d["M-P", "R"] = 789
    d["L", "C"] = 123

    for f, l in d:
        print(f"{f+'. ':<5} {l+'. ':<7}", ": ", d[f, l])

    print("\n" + str(d))

    n = d["L", "C"]
    print(n)
    print(": ".join(["L. C.", str(n)]))

    print(d.keys())
    print(d.values())
    print(d.items())

    print(lg)

    print("Longueur=%s" % len(d))
    print("Type=%s" % type(d))
    d.update({("A", "K"): 456})
    print(str(d) + "\n")

    # print(d.items())

    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        print(f"{str(key):<12} : ", d[key])
    print(d.pop(("A", "K")))
    print(lg)
    sorted_keys = sorted(d.keys())
    for key in sorted_keys:
        print(f"{str(key):<12} : ", d[key])

    print(lg)

    a = [1, 2, 3]
    # b = a
    b = a[::]  # <=> b = a.copy()
    b.append(4)

    print(f"{a=}\n" + f"{b=}")
    print(lg)
