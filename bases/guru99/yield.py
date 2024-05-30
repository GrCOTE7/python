def generator():
    yield "Welcome to Guru99 Python Tutorials"
    yield "Oki"


output = generator()

print(output)
print(*list(output))

output = generator()
for i in output:
    print(i)
print("-" * 72)


# Normal function
def normal_test():
    return "Hello World"


# Generator function
def generator_test():
    yield "Hello World"


print(normal_test())  # call to normal function
print(*list(generator_test()))  # call to generator function
print(next(generator_test()))
generated = generator_test()
print(next(generated))
# print(next(generated))  # nothing generated empty → error
print("-" * 72)
