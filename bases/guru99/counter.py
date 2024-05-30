from collections import Counter
from operator import ne

name = "abra"
_count = Counter(name)
print(_count)
_count.update("cadabra")
print(_count)
print("%s : %d" % ("u", _count["a"]))
for char in _count:
    print("%s : %d" % (char, _count[char]))

list1 = ["x", "y", "z", "x", "x", "x", "y", "z"]
print("\n" + f"{Counter(list1)}")

dict1 = {"x": 4, "y": 2, "z": 2, "z": 2}
print(Counter(dict1))

tuple1 = ("x", "y", "z", "x", "x", "x", "y", "z")
dict = Counter(tuple1)
print(dict)

del dict["x"]
print("After del ['x']: ", dict)

l1 = "lionel"
l2 = "coteooo"
c1 = Counter(l1)
c2 = Counter(l2)

print(
    "\n",
    c1,
    "\n",
    c2,
    "\nSum\n",
    Counter(c1 + c2),
    "\nSub\n",
    Counter(c1 - c2),
    "\nIntersection\n",
    Counter(c1 & c2),
    "\nUnion\n",
    Counter(c1 | c2),
    "\nMost common\n",
    Counter.most_common(c1 | c2),
    "\nSubtract\n",
    c1.subtract(c2),
    c1,'\n'
)

newcounter = Counter({"x": 5, "y": 12, "z": -2, "x1": 0})
print(newcounter)
newcounter['x']=20
print(newcounter)
print(newcounter['y'], 'y')
newcounter['zorro']=7
print(newcounter)
