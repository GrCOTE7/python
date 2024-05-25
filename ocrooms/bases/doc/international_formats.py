import locale

print(locale.getlocale())

locale.setlocale(locale.LC_ALL, "English_United States.1252")
print(locale.getlocale())

conv = locale.localeconv()  # get a mapping of conventions
x = 1234567.8
print(locale.format_string("%.2f", x, grouping=True))

print(
locale.format_string(
        "%s%.*f", (conv["currency_symbol"], conv["frac_digits"], x), grouping=True
    )
)

locale.setlocale(locale.LC_ALL, "fr_FR")
print(locale.getlocale())

conv = locale.localeconv()  # get a mapping of conventions
print(locale.format_string("%.2f", x, grouping=True).replace('\u202f', ' '))

print(
    locale.format_string(
        "%.*f %s", (conv["frac_digits"], x, conv["currency_symbol"]), grouping=True
    ).replace("\u202f", " ")
)

import reprlib

a = reprlib.repr(set("supercalifragilisticexpialidocious"))
print(a)

example = [1, "spam", {"a": 2, "b": "spam eggs", "c": {3: 4.5, 6: []}}, "ham"]

aRepr = reprlib.Repr()
print(aRepr.repr(example))

aRepr.indent = 4
print(aRepr.repr(example))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p=Person('john', 25)
print(f'{p}: {p.__dict__}')
print(p)
print(repr(p))


import pprint

t = [[[["black", "cyan"], "white", ["green", "red"]], [["magenta", "yellow"], "blue"]]]

pprint.pprint(t, width=35)
