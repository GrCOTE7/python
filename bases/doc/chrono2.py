""" Exemple de chronométrage"""

from tools.chronometer import chrono

TIMES = int(2e8)


@chrono
def method1(value):
    """Affectations unitaires"""
    a = b = 0
    for _ in range(TIMES):
        t = a
        a = b
        b = t
        a = 1
        b = 2


@chrono
def method2():
    """Affectations multiples (tuples)"""
    a = b = 0
    for _ in range(TIMES):
        a, b = b, a
        a = 1
        b = 2
    print(method2.__doc__, end=': ')

method1(method1.__doc__)
method2()
