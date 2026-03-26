import random


def SayHello():
    print("hello world!")


def randomNumber(f=100):

    return random.randint(0, f)


def formatX(x, d=0):
    return "{:,.{}f}".format(x, d).replace(",", " ")


if __name__ == "__main__":
    # SayHello()
    maxi = 100
    x = []
    numbersX = 10**6

    x.append(randomNumber())
    for i in range(numbersX):
        x.append(randomNumber(maxi))
    # print(x)
    print()
    moy = sum(x) / len(x)
    print(
        f"Moyenne de {formatX(numbersX)} nombres aléatoires entre 0 et {formatX(maxi)}: {formatX(moy,2)}"
    )
    print()
