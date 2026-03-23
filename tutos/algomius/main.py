import sys
from sys import argv

print("Je suis ", argv)

# py main.py 12 23
# → Je suis  ['main.py', '12']

if len(argv) == 3:
    prog, nom, age = argv
    print("Nom du programme : ", prog)
    print("Nom du user : ", nom)
    print("Age du user : ", age)
elif len(argv) < 3:
    print("Usage : py main.py <nom> <age>")
    sys.exit(0)
else:
    sys.exit(8)

# En CLI: echo %errorlevel%
