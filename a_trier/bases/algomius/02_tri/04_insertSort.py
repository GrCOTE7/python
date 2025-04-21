import random

# 2 façons de faire la même chose
l = [random.randint(1, 9) for _ in range(9)]
l2 = random.choices(range(1, 10), k=9)

l3 = random.sample(range(1, 10), 9)  # Uniques

print(l)
print(l2)
print(l3)
