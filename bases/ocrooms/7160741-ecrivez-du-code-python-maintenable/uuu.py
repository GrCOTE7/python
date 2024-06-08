"""test"""


def get_harmonic_mean(numbers):
    """Calcule la moyenne harmonique d'une suite de nombres."""
    # try:
    total = 0
    for number in numbers:
        total += 1 / number
    return len(numbers) / total
    # except Exception:
    #     print("Warning! Division by zero!")
    # return None


print(get_harmonic_mean([1, 0]))
