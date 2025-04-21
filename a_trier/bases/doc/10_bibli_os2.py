import re

a = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")

b = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")


c = "tea for too".replace("too", "two")
print(a, b, c)


import random

z = random.choice(["apple", "pear", "banana"])

y = random.sample(range(100), 10)  # sampling without replacement

x = random.random()  # random float

w = random.randrange(6)  # random integer chosen from range(6)

print(z, y, x, w)
