s = set()
s.add(1)
print(s)

# s= {}
# s.add(1) → ERR Dict no add() no extend()

s = {}
s.update({1: True})
print(s)

# get(cle, defaut): lit sans erreur si la clé manque.
# keys(): vue des clés.
# values(): vue des valeurs.
# items(): vue des paires clé/valeur.
# Ajout et mise à jour
# update(autre_dict): fusionne ou remplace des clés existantes.
# setdefault(cle, defaut): retourne la valeur si la clé existe, sinon crée avec defaut.
# opérateur | et |= (Python récent): fusion de dictionnaires.
# Suppression
# pop(cle[, defaut]): retire une clé et retourne sa valeur.
# popitem(): retire et retourne la dernière paire ajoutée.
# clear(): vide le dictionnaire.
# Copie et création
# copy(): copie superficielle.
# fromkeys(iterable, valeur): crée un dict avec ces clés et une même valeur.
