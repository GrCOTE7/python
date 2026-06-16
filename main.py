from tools.tools import *


def test():
    sum = 0
    for i in range(1, int(1e5)):
        sum += i
    print(f"{sum = }")


def template():
    title = "ReaDy".capitalize()
    # cls(f"{title}")
    ls(CYAN)
    print(f"{title}".center(CLIW))
    sl(FRENCH)


if __name__ == "__main__":

    template()
    # print("Ok")
    test()
    exit()
