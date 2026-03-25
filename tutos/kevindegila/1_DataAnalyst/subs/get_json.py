import numpy as np
import pandas as pd
import math, os
from tabulate import tabulate
import urllib.request

print("-" * 111)


def get_movies():
    dossier = "datasets"
    fichier = os.path.join(dossier, "movie.csv")

    url = "https://raw.githubusercontent.com/kevindegila/data-analyst/main/datasets/movie.csv"

    # Créer le dossier si nécessaire
    os.makedirs(dossier, exist_ok=True)

    # Télécharger le fichier seulement s'il n'existe pas
    if not os.path.exists(fichier):
        urllib.request.urlretrieve(url, fichier)

    # Lecture robuste du CSV
    try:
        return pd.read_csv(fichier, sep=",")
    except pd.errors.ParserError:
        # movie = pd.read_csv(fichier, sep=",", engine="python", on_bad_lines="skip")
        movie = pd.read_csv(fichier, sep=",", engine="python", on_bad_lines="ignore")
        print("Avertissement: certaines lignes mal formées ont été ignorées.")
        

if __name__ == "__main__":
    movie = get_movies()
    print(movie.iloc[2, 3])
    
    # CLI dans google Colab
    # !mkdir datasets
    # !wget https://raw.githubusercontent.com/kevindegila/data-analyst/main/datasets/movie.csv -O datasets/movie.csv
