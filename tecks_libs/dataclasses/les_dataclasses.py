from dataclasses import dataclass, replace


# @dataclass(frozen=True) # On ne peut pas changer les choses - Tout est 'congelé'
@dataclass(frozen=False) # On peut changer les choses
class Utilisateur:
    nom: str
    email: str

def modifie_utlisateur(user):
    return replace(user, nom="COUCOU")

u = Utilisateur(nom="Alice", email="alice@test.com")

print(u, '\n=> ', modifie_utlisateur(u))
