# string.find(substring, start, end)
print("Lionel".find("on", 2, 4))

print("Lionel"[::-1])


def fct(*args):
    print(args)
    print(3 in args)
    print("Nombre de 3 :", args.count(3))
    print(len(args))
    print(sum(args))
    for i in args:
        print(i)


print("Value in built variable name is:  ", __name__)

fct(1, 2, 3, 3, 4, 5)
