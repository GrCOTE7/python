# fichier : main.py
import os
import unittest
import sys
import io

# import test_python_org_search  # Assurez-vous que ce module est dans le même répertoire

# Si on veut avoir des params différents entre CLI et PREVIEW
# if __name__ == "__main__":
#     script_path = os.path.abspath(__file__)
#     if os.getenv("ENV") == "preview":
#         unittest.main(module="test_python_org_search", argv=["ignored"], exit=False)
#     else:
#         unittest.main(module="test_python_org_search")


# class NullIO(io.StringIO):
#     def write(self, txt):
#         pass

if __name__ == "__main__":
    script_path = os.path.abspath(__file__)

    # with NullIO() as null_io:
    #     old_stdout = sys.stdout
    #     sys.stdout = null_io  # Rediriger la sortie standard vers null_io
    #     try:
    #         unittest.main(module="test_python_org_search", argv=["ignored"], exit=False)
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         sys.stdout = old_stdout  # Restaurer la sortie standard

    unittest.main(module="test_python_org_search", argv=["ignored"], exit=False)

# Pour tests in preview
# Param AREPL: Env fil de VSC: c:\Users\utilisateur\env
# contient:
#   ENV=preview
#   WORKDIR=C:\laragon\www\python\bases\guru99
print('-'*70, script_path)
print("ENV: ", os.getenv("ENV"))
print("WORKDIR:", os.getenv("WORKDIR"))
