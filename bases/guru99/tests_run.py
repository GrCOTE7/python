# fichier : main.py
import os
import unittest
import logging
# import test_python_org_search  # Assurez-vous que ce module est dans le même répertoire

# Si on veut avoir des params différents entre CLI et PREVIEW
# if __name__ == "__main__":
#     script_path = os.path.abspath(__file__)
#     if os.getenv("ENV") == "preview":
#         unittest.main(module="test_python_org_search", argv=["ignored"], exit=False)
#     else:
#         unittest.main(module="test_python_org_search")

if __name__ == "__main__":
    script_path = os.path.abspath(__file__)

    # Configurer le niveau de journalisation pour afficher seulement les erreurs
    logging.basicConfig(level=logging.ERROR)
    
    t=unittest.main(module="test_python_org_search", argv=["ignored"], exit=False)

# Pour tests in preview
# Param AREPL: Env fil de VSC: c:\Users\utilisateur\env
# contient:
#   ENV=preview
#   WORKDIR=C:\laragon\www\python\bases\guru99
print (script_path)
print("ENV: ", os.getenv("ENV"))
print("WORKDIR:", os.getenv("WORKDIR"))
