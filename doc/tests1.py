def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.01
    """
    return sum(values) / len(values)


import doctest

print(average([20, 30, 70]))
print(doctest.testmod())
