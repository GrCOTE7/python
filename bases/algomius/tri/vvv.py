from modules.IterativeSorts import IterativeSortArr
from pprint import pprint
import random
 
t_src=random.sample(range(1, 10001), 1000)
# t_src=[6, 7, 2, 8, 5]

tableaux=[]
tableaux = IterativeSortArr(t_src)

# print()
# print('tableaux:')
# pprint(tableaux, width=80, indent=2)
# pprint(tableaux)

