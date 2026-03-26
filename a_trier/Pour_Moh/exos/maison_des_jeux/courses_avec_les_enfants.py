# from robot import *
from tools.mvts import *

for n in range(1, 11):
    for _ in range(n):
        droite()
    ramasser()
    for _ in range(n):
        gauche()
    deposer()
