
def ajoute_au_panier(article, chariot=None):
    if chariot is None:
        chariot=[]
    chariot.append(article)
    return chariot

print('1: ', ajoute_au_panier("Chaussures"))
print('2: ', ajoute_au_panier("Chaussettes"))
cart = ajoute_au_panier("Pantalon")
print('3: ', ajoute_au_panier("T-Shirt", cart))

    