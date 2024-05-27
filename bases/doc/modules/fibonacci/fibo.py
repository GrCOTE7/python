def showfib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    print(f"fib de {n}:")
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    print(__name__)
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f = fib

# Pour utilsation en CLI
if __name__ == "__main__":
    import sys

    print(f"{fib.__name__} de {int(sys.argv[1])}:", fib(int(sys.argv[1])))

# Dans scrip main:
# from fibo import fib, f
# Now call the function we just defined:
# fib(100)
# f(5000)
