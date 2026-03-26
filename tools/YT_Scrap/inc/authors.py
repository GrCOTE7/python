import sys
from pymox_kit import *

AUTHORS = {
        
        # 0: "doro2255",
        # 1: "LionelCOTE",
        # 2: "c57-u5s",
        # 3: "CodeAvecJonathan",
        # 4: "DataAvecJB",
        # 5: "MasteringAI-q9g",
        # 6: "CodeGoat-s2y",
        # 7: "tseries",
        
        0: "doro2255",
        1: "LionelCOTE",
        2: "c57-u5s",
        3: "Alphorm",
        4: "tseries",
        5: "coach-exam",
        6: "CodeAvecJonathan",
        7: "Gravenilvectuto",
        8: "hassanbahi",
        9: "donaldprogrammeur",
        10: "DataAvecJB",
        11: "bandedecodeurs",
        12: "MasteringAI-q9g",
        13: "KevinDegila",
        14: "InformatiqueSansComplexe",
        15: "MachineLearnia",
        16: "CodeGoat-s2y",
        17: "2minutesPy",
        18: "JordyBayo",
        19: "Faireaimerlesmathématiques-h4w",
        20: "Indently"
    }

# Pour mise au point du script ❌ toutes en partant du bas saud tseries et alphorn
#  0 AUTHOR = "doro2255"                 #      1 video  -              29 vues -               7 minutes

#  1 AUTHOR= "LionelCOTE"                #     12 videos -           3 955 vues -   1 heure et 27 minutes - Aide pour mise au point car peu de vidéos

#  2 AUTHOR = "c57-u5s"                  #     16 videos -           1 097 vues -   11 heures et 23 minutes
#  3 AUTHOR = "Alphorm"                  #  4 064 videos -      15 577 306 vues -  665 heures et 3 minutes - Au passage, diverses notions liées à l'informatique
#  4 AUTHOR = "tseries"                  # 23 437 videos - 329 019 848 258 vues - 2011 heures et 38 minutes - Compte qui génère le + de gains au Monde avec YT !

# Niveau scolaire
#  5 AUTHOR = "coach-exam"               #    110 videos -         195 664 vues -   12 heures et 54 minutes

# Initiation à Python (Bases)
#  6 AUTHOR = "CodeAvecJonathan"         #     10 videos -       5 386 712 vues -   15 heures et 16 minutes
#  7 AUTHOR = "Gravenilvectuto"          #    174 videos -      26 853 211 vues -   49 heures et 39 minutes
#  8 AUTHOR = "hassanbahi"               #    843 videos -      52 877 137 vues -  191 heures et 13 minutes - Top pour comprendre super bien les bases - Attention: Pas mal de vidéos + anciennes avec le langage C, mais facilement adaptable ou catégoriser 'done' ;-) !... Sinon, c aussi 1 super exo ;-) !

# Python approfondi
#  9 AUTHOR = "donaldprogrammeur"        #    424 videos -       1 143 154 vues -  303 heures et 56 minutes - Des bases à DevOps

# Python - FastAPI
# 10 AUTHOR = "DataAvecJB"               #     16 videos -          49 987 vues -    8 heures et  6 minutes - FastAPI en moins de 10 minutes
# 11 AUTHOR = "bandedecodeurs"           #     50 videos -         742 077 vues -   21 heures et 16 minutes - + généraliste, intro simple et visuelle

# Python pour l'IA
# 12 AUTHOR = "MasteringAI-q9g"          #     29 videos -           3 717 vues -   10 heures et 41 minutes - Exemple pédagogique orienté objet et plus complet (DB, validation, endpoints)
# 13 AUTHOR = "KevinDegila"              #    262 videos -         607 775 vues -   53 heures et 38 minutes
# 14 AUTHOR = "InformatiqueSansComplexe" #    285 videos -       1 809 388 vues -   33 heures et 20 minutes
# 15 AUTHOR = "MachineLearnia"           #     65 videos -      11 500 619 vues -   22 heures et 53 minutes

# 16 AUTHOR = "CodeGoat-s2y"             #     38 videos -          42 150 vues -   24 heures et 23 minutes - En anglais, mais archi complet

def get_author_name(ida=None):
    """_summary_

    Args:
        ida (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    

    if isinstance(ida, int) and ida in AUTHORS:
        return AUTHORS[ida]
    else:
        file = "inc/authors.py"
        sys.exit(
            f"{RED}{ida} n'est pas un index correct{R}... : {RED}AUTHOR n'est pas défini dans {SB}{file}{R}. Arrêt du script.{R}"
        )

def nb_authors():
    return len(AUTHORS)


if __name__ == "__main__":
    URL = get_author_name(0)
    print(f"{GREEN}{URL}{R}\n{GREEN}Nombre d'auteurs disponibles : {nb_authors()}{R}")
