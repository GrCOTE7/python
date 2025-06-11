import random
from re import S
import sys
from pathlib import Path
from types import LambdaType

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *

if __name__ == "__main__":
    cls(" old.algorea.org_chap7_enCours")

    def case():
        cls()
        
        # 2 4 2 2 1 2 1 2 1 1 1 2 1 1 2 1 1 2 1 1 3 1 2 1 2
        # from database import *

        # a= loadTable('regions')
        # b= loadTable('villes') 

        # r = joinTables(a, 'capitale', b, 'ville', 'inner')
        # r= sortByColumn(r,'table2_ville', 'asc')
        # r= selectColumns(r,['table1_capitale', 'table1_region', 'table2_departement', 'table2_nb_habitants'])

        # displayTable(r)

        ls()

    case()

    exit()

    # print(
    #     *(n := int(input())) and (n := n * i for i in range(1, int(input()) + 1)),
    #     sep="\n",
    # )
