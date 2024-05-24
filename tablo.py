print("7".zfill(3) + "\n")

for x in range(1, 11):
    print("{0:2d} {1:^3} {2:3d} {1:^3} {3:4d}".format(x, "|", x**2, x**3))

print()

for x in range(1, 11):
    print(
        repr(x).rjust(2), "|".center(3), repr(x * x).rjust(3), " | ".center(3), end=" "
    )
    # Note use of 'end' on previous line
    print(repr(x * x * x).rjust(4))
