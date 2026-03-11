import random
from re import S
import sys
from pathlib import Path
from types import LambdaType

import cv2  # pip install opencv-python numpy
import numpy as np

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *

if __name__ == "__main__":
    cls()

    def case():
        cls()

        def contoursAvecCv2():
            # Charger l'image
            image = cv2.imread("visage.png", cv2.IMREAD_GRAYSCALE)

            filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

            # Appliquer la convolution
            image_filtered = cv2.filter2D(image, -1, filter)

            # **Combiner l’image originale avec l’image filtrée**
            image_finale = cv2.addWeighted(image, 0.7, image_filtered, 0.3, 0)
            # Ajuster les coefficients selon le rendu

            # Afficher l’image filtrée
            cv2.imshow("Image originale avec contours", image_finale)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imwrite("visage_coutours.png", image_finale)

        def calculDuContourAvecFiltreLaplacienEtNumpy():
            # Charger l'image
            # image = cv2.imread("visage.png", cv2.IMREAD_GRAYSCALE)

            # Exemple de matrice image en niveaux de gris
            image = np.array(
                [
                    [191, 191, 191, 191, 191],
                    [191, 191, 191, 191, 191],
                    [191, 191, 64, 191, 191],
                    [191, 191, 64, 191, 191],
                    [191, 191, 191, 191, 191],
                ]
            )

            # Filtre Laplacien
            filtre = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

            # Coordonnées du pixel cible (exemple : (2,2))
            x, y = 2, 2

            # Extraire la région 3x3 autour du pixel cible
            voisinage = image[x - 1 : x + 2, y - 1 : y + 2]

            # Appliquer la convolution manuellement
            nouvelle_valeur = np.sum(voisinage * filtre)

            # Limiter la valeur entre 0 et 255
            nouvelle_valeur = max(0, min(255, nouvelle_valeur))

            print(f"Nouvelle luminosité du pixel ({x},{y}) : {nouvelle_valeur}")

        def calculManuelDuContourAvecFiltre(image):

            # Filtre Laplacien en liste
            filtre = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

            # Fonction pour appliquer la convolution sans NumPy
            def appliquer_filtre(image, filtre):
                hauteur, largeur = len(image), len(image[0])  # 18

                image_centrée_avec_bords = [
                    [191] * (largeur + 2) for _ in range(hauteur + 2)
                ]

                # dessiner(image_centrée_avec_bords)

                image_filtrée = [[255] * (largeur + 2) for _ in range(hauteur + 2)]

                for i in range(len(image)):
                    for j in range(len(image[i])):
                        image_centrée_avec_bords[i + 1][j + 1] = image[i][j]

                for i in range(-1, hauteur + 1):  # Ignorer les bords
                    for j in range(-1, largeur + 1):
                        pixel = 0
                        for fi in range(3):
                            for fj in range(3):
                                pixel += (
                                    image_centrée_avec_bords[i + fi - 1][j + fj - 1]
                                    * filtre[fi][fj]
                                )
                        # image_filtrée[i][j] = pixel
                        image_filtrée[i][j] = max(
                            0, min(255, pixel)
                        )  # Clipper entre 0 et 255

                dessiner(image)
                dessiner(image_centrée_avec_bords)
                dessiner(image_filtrée)
                return image_filtrée

            # Appliquer le filtre
            image_filtrée = appliquer_filtre(image, filtre)

            # Afficher le résultat
            # for ligne in image_filtrée:
            #     print(ligne)
            # dessiner(image_filtrée)
            # for ligne in image:
            #     print("".join(f"{str(val):^7}" for val in ligne))

            # for ligne in image_filtrée:
            #     print("".join(f"{val:^5}" for val in ligne))

        def image_get():
            return [
                [191, 191, 191, 191, 191],
                [191, 64, 191, 191, 191],
                [191, 64, 191, 191, 191],
                [191, 64, 191, 191, 191],
                [191, 64, 191, 191, 191],
                [191, 64, 64, 64, 191],
                [191, 191, 191, 191, 191],
            ]

        def image_read(image_path, convertFormat=True):

            from PIL import Image

            # Ouvrir l'image et convertir en niveaux de gris
            img = Image.open(image_path).convert("L")  # "L" = niveaux de gris
            largeur, hauteur = img.size  # 252 x 252
            bloc_size = 1

            if convertFormat:
                # Taille originale et taille cible
                largeur_finale, hauteur_finale = 18, 18

                # Facteur de réduction (taille d'un bloc)
                bloc_size = largeur // largeur_finale  # 252 / 17 = 14 pixels
                largeur = largeur_finale
                hauteur = hauteur_finale

            # Extraire les pixels et calculer les moyennes
            pixels = np.array(img)  # Convertir l'image en tableau NumPy
            image_matrice = []

            for y in range(hauteur):
                ligne = []
                for x in range(largeur):
                    # Déterminer la région correspondante
                    x_start = x * bloc_size
                    y_start = y * bloc_size

                    # Prendre 5 pixels centraux dans cette région pour la moyenne
                    region = pixels[
                        y_start : y_start + bloc_size, x_start : x_start + bloc_size
                    ]
                    centre_pixels = region[
                        bloc_size // 2 - 2 : bloc_size // 2 + 3,
                        bloc_size // 2 - 2 : bloc_size // 2 + 3,
                    ]  # Sélection de 5 pixels centraux

                    moyenne_pixel = int(np.mean(centre_pixels))  # Calculer la moyenne
                    ligne.append(moyenne_pixel)

                image_matrice.append(ligne)

            return image_matrice

        def dessiner(image):
            """Convertion d'une matrice de pixels en car.s ASCII"""

            # Définir les niveaux en fonction de la luminosité
            niveaux = [
                ("\033[0;30m  \033[0m", 50),  # Noir profond
                ("\033[0;37m░░\033[0m", 100),  # Gris foncé
                ("\033[0;37m▒▒\033[0m", 150),  # Gris moyen
                ("\033[0;37m▓▓\033[0m", 200),  # Gris clair
                ("\033[0;97m██\033[0m", 255),  # Blanc
            ]

            for ligne in image:
                print(
                    "".join(
                        next(car for car, seuil in niveaux if val <= seuil)
                        for val in ligne
                    )
                )

        # contoursAvecCv2()
        # calculDuContourAvecFiltreLaplacienEtNumpy()
        # calculManuelDuContourAvecFiltre()
        image = image_get()
        image = image_read("visage.png")
        calculManuelDuContourAvecFiltre(image)

        # dessiner(image)
        # ls()

    case()

    exit()
