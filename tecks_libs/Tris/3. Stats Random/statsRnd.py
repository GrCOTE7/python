import random

# pip install matplotlib
import matplotlib.pyplot as plt


def SayHello():
    print("hello world!")


def randomNumber(f=100):
    return random.randint(0, f)


def formatX(x, d=0):
    return "{:,.{}f}".format(x, d).replace(",", " ")


if __name__ == "__main__":
    maxi = 100
    x = []
    numbersX = 10**6

    x.append(randomNumber())
    for i in range(numbersX):
        x.append(randomNumber(maxi))

    moy = sum(x) / len(x)

    # Count occurrences of each number
    counts = {}
    for num in x:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Print the counts
    print("Nombre de occurrences de chaque nombre:")
    for num, count in sorted(counts.items()):
        print(f"{num}: {formatX(count)}")

    # counts = Counter(x)
    print(
        f"Moyenne de {formatX(numbersX)} nombres aléatoires entre 0 et {formatX(maxi)}: {formatX(moy,2)}"
    )

    # plt.ylim(0, max(counts.values()) * 1.05)
    plt.ylim(min(counts.values()) * 0.98, max(counts.values()) * 1.02)
    sorted_counts = sorted(counts.items())
    # Graph en barres
    # plt.bar(counts.keys(), counts.values())
    # Graph en ligne
    plt.plot([x[0] for x in sorted_counts], [x[1] for x in sorted_counts])
    # Graph en points
    # plt.scatter(counts.keys(), counts.values())

    plt.xlabel("Nombre")
    plt.ylabel("Compte")
    plt.title("Nombre d'occurrences de chaque nombre")
    plt.show()
