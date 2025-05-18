import sys, time
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import cls, nf, SB, EB, exit, sl

if __name__ == "__main__":

    cls("Exercice EULER # 004")

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def largest_palindrome_product():
        largest_palindrome = 0
        for i in range(999, 99, -1):  # Descending order for efficiency
            for j in range(i, 99, -1):  # Start from i to avoid redundant calculations
                product = i * j
                if is_palindrome(product) and product > largest_palindrome:
                    largest_palindrome = product
                    factors = (i, j)  # Store the factors
        return largest_palindrome, factors

    result, (factor1, factor2) = largest_palindrome_product()
    print(f"Largest palindrome: {result} = {factor1} × {factor2}")

    exit()
    # print(f"{nf(a, 0): >10}")
