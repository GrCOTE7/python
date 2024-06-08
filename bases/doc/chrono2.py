""" Exemple de chronométrage"""

from chronometer import chrono

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
def method2(value):
    """Affectations multiples (tuples)"""
    a = b = 0
    for _ in range(TIMES):
        a, b = b, a
        a = 1
        b = 2


method1(method1.__doc__)

method2(method2.__doc__)
