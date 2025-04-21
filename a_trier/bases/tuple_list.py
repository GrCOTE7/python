import sys

sys.path.insert(0, "./")
from tools.cls import cls

cls("tuple")

xy = (2, 5)
depl = (+1, -1)

print("xy: ", xy, "depl:", depl)

etape1 = zip(xy, depl)
print("type zip() :", etape1)

etape1 = list(etape1)
print("type list(zip()) :", type(etape1))
copie = etape1[::]

print(" " * 9, "(x1, x2) (y1, y2)\nzip(') → ", copie, "\ndécomposé :", *copie, "\n")

print("-" * 50, "\n")


etape2 = map(sum, copie)
print("type map(sum()): ", etape2)
# print(" "*5, "(x1, x2) (y1, y2)")

print("→ etape2: ", list(etape2), "\n")

new_pos = tuple(map(sum, zip(xy, depl)))
print("new_pos: ", new_pos)

print("-" * 50, "\n")

print("xy: ", xy, "depl:", depl)
print("le zip décomposé:", *zip(xy, depl))
print("avec compréhension", tuple(p + q for p, q in zip(xy, depl)))

print("-" * 50, "\n")

mytuple = ((2, 3), (4, 5))
print(p + q for p, q in mytuple)
# print('mytuple:', tuple(p+q for p, q in mytuple))
print("mytuple:", (tuple)((p + q for p, q in mytuple)))

print("-" * 50, "\n")

a = {"a": 1, "b": 2}
b = ["3"]

t = (a, b)

print("a =", a, type(a))
print("b =", b, type(b))
print("t =", t, type(t))
