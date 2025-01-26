def msg():
    print()

    nombres = 1, 2, 3, 1
    print(nombres)
    print(type(nombres)) # tuple immutable
    print(len(nombres))
    print(nombres.count(1))
    print(nombres.index(2))

    print()


if __name__ == "__main__":
    msg()
