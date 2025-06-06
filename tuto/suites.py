from re import S
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *


if __name__ == "__main__":
    cls("suites")
    # A*n**degré + B*n**(degré - 1)+ ... + Z
    resolutionsPolynomes=[
      'déterminer le degré de la suite par les différences successives']
    
    exemples=[
      '1,2,3,..., n',
      '1,2,4,8,..., n',
      '1,2,3,5,8,13,27,..., n', # Fibonacci
      '1,3,6,10,15,21,34,..., n' # Sommiel
]
    
    # Résolution = Déterminer A, B, C; etc...
    # Et replacer ces valeurs dans An**degré + Bn + C
    
    ex0 = '1' # Delta entre tous les termes
    deg0='1 → An + B'
    res0 = '''
Essai avec S(1) et S(2) pour avoir 2 équations avec 2 inconnues:
S('1) = 1
An + B → A + B = 1
S('2) = 2
2A + B = 2
On en déduit que A = 1 et B = 0.
La suite est donc définie par Sn = n.
'''
    res=''
    ex1 = '1,2,4, 8, ...'
    deg1='''
    1 → 1
    2 → 2
    3 → 4
    4 → 8
    On a un delta de 1 entre chaque terme, donc c'est une suite géométrique.
    Pour trouver la raison q, il suffit d'enlever le premier terme au deuxième :
    q = S(2)/S(1)
    q = 2/1
    q = 2
    La suite est donc définie par Sn = 2**(n-1).
    '''
    res1 = '''
2**(n-1)
'''

    ex2= '1,2,3,5,8,13,27,...'
    deg2='''
    1 → 1
    2 → 2
    3 → 3
    4 → 5
    On a un delta de 1 entre chaque terme, donc c base est la somme des deux précédents.
    La suite est donc définie par Sn = Fn+Fn-1.
    '''
    res2 = '''
Fn+Fn-1
'''
   
    ex3= '1,2,6,10,15,21,34,...'
    deg3='''
    deltas 1er niveau:
    1 → 1
    2 → 4
    3 → 4
    4 → 5
    5 → 6
    deltas 2ème niveau:
    1 → 3
    2 → 0
    3 → 1
    4 → 1
    On a un delta de 1 entre chaque terme, donc c'est une suite triangulaire.
    Pour trouver la formule, il faut utiliser la formule du triangle de Pascal.
    La suite est donc définie par Sn = (n*(n+1))/2.
    Sinon, vu que deltas =1dasn 2èùe niveau, on considère degré 2: An**2 + Bn + C
    Puis tester avec
    s(1) = 1
    s(2) = 3
    s(3) = 6
    s(4) = 10
    s(5) = 15
    '''
  res3 = '''
    1: An**2 + Bn + C → A + B + C = 1
    2: 4A + 2B + C = 3
    3: 9A + 3B + C = 6
    On en conclut, avec ces 3 équations et 3 inconnues, 
    par les différences aq2 -eq1, aq3 -eq2, etc...
    que A = 1, B = 1 et C = 0.
    La suite est donc definie par Sn = n**2 + n = (n*(n+1))/2.
    '''
'''
  
  