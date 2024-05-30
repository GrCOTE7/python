# REDUCE
from functools import reduce

sequences = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, sequences)
print(sequences, '→', product)
# print(list(maping_result))
# print(*maping_result)
# print(*enumerate(maping_result, 1))
print("-" * 72)

# MAP
print("MAP")
sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
# sequences.sort()
maping_result = map(lambda x: x * x, sequences)
# print(list(maping_result))
# print(*maping_result)
print(*enumerate(maping_result, 1))
print("-" * 72)

# FILTER
print("FILTER")
sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
# sequences.sort()
filtered_result = filter(lambda x: x > 4, sequences)
# print(list(filtered_result))
print(*filtered_result)
# print(*enumerate(filtered_result))
print("-" * 72)

# Simple lambda
print((lambda x: x**2)(7))
print("-" * 72)

adder = lambda x, y: x + y
print("1 + 2 =", adder(1, 2))
s = (2, 3)
x, y = s
print(f"{s[0]} + {s[1]} =", adder(x, y))
print("-" * 72)

# What a lambda returns
string = "\nsome kind of a useless lambda"
print(lambda string: print(string))

# What a lambda returns #2
x = "some kind of a useless lambda"
(lambda ch: print(ch))(x)


# A REGULAR FUNCTION
def guru(funct, *args):
    print("With lambda: ")
    funct(*args)


def printer_one(arg):
    return print("one: " + arg)


def printer_two(arg):
    print("two: ", arg)


# CALL A REGULAR FUNCTION
guru(printer_one, "printer 1 REGULAR CALL")
guru(printer_two, "printer 2 REGULAR CALL \n")
# CALL A REGULAR FUNCTION THRU A LAMBDA
guru(lambda: printer_one("printer 1 LAMBDA CALL"))
guru(lambda: printer_two("printer 2 LAMBDA CALL"))

print("-" * 72)
