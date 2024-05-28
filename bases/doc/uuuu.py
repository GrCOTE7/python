import os

def get_path_depth():
    """ Get the prefix for path
    """
    # Obtenez le chemin du répertoire courant
    chemin_courant = os.getcwd()

    # Continuez à monter dans l'arborescence des répertoires jusqu'à ce que vous atteigniez le répertoire racine
    # while 'python' != chemin_courant[-6]:
    #     print(chemin_courant)
    #     chemin_courant = os.path.dirname(chemin_courant)

    # return chemin_courant

    # print(trouver_repertoire_racine())

    print(os.getcwd())

    path='c:\laragon\www\python'

    path = os.getcwd()
    arr=[1,2,3]
    res=arr[-1]
    res=arr[-1]

    res=path.split("\\")
    print(res)
    print(len(res))

    res = len(res)-res.index('python')-1

    print('Prof = ',res)

    print( '../'*res+'chemin')


get_path_depth()
