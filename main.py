from gc7.tools.file import get_data, get_caller_depth

# import gc

# gc.file_depth.file_depth()

adherents = get_data()  # Liste de dictionnaires

# Calcul de la largeur maximale pour chaque colonne
largeurs_colonnes = {
    cle: max(len(str(cle)), max(len(str(adherent[cle])) for adherent in adherents))
    for cle in adherents[0]
}

# En-tête de la table
ligne_en_tete = " | ".join(
    f"{cle:{largeurs_colonnes[cle]}}" for cle in adherents[0].keys()
)
print(ligne_en_tete)
print("-" * len(ligne_en_tete))

# Données de la table
for adherent in adherents:
    # ligne_donnees = " | ".join(
    #     f"{str(valeur):{largeurs_colonnes[cle]}}" for cle, valeur in adherent.items()
    # )
    ligne_donnees = " | ".join(
        (
            f"{str(valeur):>{largeurs_colonnes[cle]}}"
            if cle == "age"
            else f"{str(valeur):{largeurs_colonnes[cle]}}"
        )
        for cle, valeur in adherent.items()
    )
    print(ligne_donnees)
