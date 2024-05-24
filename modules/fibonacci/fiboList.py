def fib(n: int):  # write Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# Dans scrip main:
# from fiboList import fib

print(fib.__doc__, '\nExample if n = 7:\n', fib(7))
print(fib.__annotations__)
