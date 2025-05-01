from tools import *

cls(f"Test pour {sb}mes tools{eb}")

if __name__ == "__main__":

    def s(totalLength: int) -> tuple:
        lengthModulo3 = totalLength % 3
        a = totalLength // 3 + int(lengthModulo3 == 2)
        b = {
            0: a,
            1: a + 1,
            2: a - 1,
        }[lengthModulo3]
        return (a, b)

    # for l in range(3, 16):
    #     gras = "\x1b[1m" if not l % 3 else "\033[0m"
    #     print(f"{gras}{l: >3} {' '*3}→{s0(l)[0]: >10}{' '*5}{s0(l)[1]: >3}\033[0m")

    for l in range(3, 16):
        gras = "\x1b[1m" if not l % 3 else "\033[0m"

        t = (1, 2, 3)

        print(f"{gras}{l: >3} {' '*3}→{str(s(l)): >10}\033[0m")

    ls()
    sl()
    print(t)

    exit()
