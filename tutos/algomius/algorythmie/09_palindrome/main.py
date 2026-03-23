# https://www.youtube.com/watch?v=ALI6TS3uSGQ&list=PLo53cbpzes8ZDG62Pn4U4plWpP8_EBFal&index=9


def estPalindromeIt(seq):
    """
    Cette fonction permet de déterminer de manière itérative si une séquence est un palindrome
    """
    deb = 0
    fin = len(seq) - 1

    while deb < fin:
        if seq[deb] != seq[fin]:
            return False
        deb = deb + 1
        fin = fin - 1

    return True


def estPalindromeRec(seq, deb=0, fin=-1):
    """
    Cette fonction permet de déterminer de manière récursive si une séquence est un palindrome
    """
    if fin == -1:
        fin = len(seq) - 1

    if deb == fin:
        return True
    elif fin == deb + 1 and seq[deb] == seq[fin]:
        return True
    elif seq[deb] == seq[fin]:
        return estPalindromeRec(seq, deb + 1, fin - 1)
    else:
        return False


def lgPlusLongPalindromeRec(seq, deb=0, fin=-1):
    """
    Cette fonction permet de déterminer de manière récursive la taille de la plus longue sous-séquence de seq qui soit un palindrome
    """
    if fin == -1:
        fin = len(seq) - 1

    if deb == fin:
        return 1
    elif seq[deb] == seq[fin] and deb + 1 == fin:
        return 2
    elif seq[deb] == seq[fin]:
        return lgPlusLongPalindromeRec(seq, deb + 1, fin - 1) + 2
    else:
        return max(
            lgPlusLongPalindromeRec(seq, deb, fin - 1),
            lgPlusLongPalindromeRec(seq, deb + 1, fin),
        )


def lgPlusLongPalindromeDyn(seq):
    """
    Cette fonction permet de déterminer de manière itérative et dynamique la taille de la plus longue sous-séquence de seq qui soit un palindrome
    """
    n = len(seq)
    matrice_plusLong = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        matrice_plusLong[i][i] = 1

    for lgPalin in range(2, n + 1):
        for deb in range(n - lgPalin + 1):
            fin = deb + lgPalin - 1
            if seq[deb] == seq[fin] and lgPalin == 2:
                matrice_plusLong[deb][fin] = 2
            elif seq[deb] == seq[fin]:
                matrice_plusLong[deb][fin] = matrice_plusLong[deb + 1][fin - 1] + 2
            else:
                matrice_plusLong[deb][fin] = max(
                    matrice_plusLong[deb][fin - 1], matrice_plusLong[deb + 1][fin]
                )

    return matrice_plusLong[0][n - 1]


def plusLongPalindromeDyn(seq):
    """
    Cette fonction permet de déterminer de manière itérative et dynamique la plus longue sous-séquence de seq qui soit un palindrome
    """
    n = len(seq)
    matrice_plusLong = [["" for x in range(n)] for x in range(n)]
    for i in range(n):
        matrice_plusLong[i][i] = seq[i]

    for lgPalin in range(2, n + 1):
        for deb in range(n - lgPalin + 1):
            fin = deb + lgPalin - 1
            if seq[deb] == seq[fin] and lgPalin == 2:
                matrice_plusLong[deb][fin] = seq[deb] + seq[fin]
            elif seq[deb] == seq[fin]:
                matrice_plusLong[deb][fin] = (
                    seq[deb] + matrice_plusLong[deb + 1][fin - 1] + seq[fin]
                )
            else:
                palinDeb = matrice_plusLong[deb][fin - 1]
                palinFin = matrice_plusLong[deb + 1][fin]
                if len(palinDeb) > len(palinFin):
                    matrice_plusLong[deb][fin] = palinDeb
                else:
                    matrice_plusLong[deb][fin] = palinFin

    return matrice_plusLong[0][n - 1]


def estPalinfromeFctNative(seq):
    return seq == seq[::-1]


if __name__ == "__main__":

    seq = "radar"
    # print (seq, estPalindromeIt(seq))
    # print(seq, estPalindromeRec(seq))
    # print(seq, estPalinfromeFctNative(seq))

    seq = "ALGOMIYOGIUSLA"
    # print(seq, lgPlusLongPalindromeRec(seq))

    print(seq, plusLongPalindromeDyn(seq))
