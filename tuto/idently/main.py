import flet as ft


def stopPycs():
    """Important if flet run -d -r pour les fichiers créés dans__pycache__/"""
    import sys

    sys.dont_write_bytecode = True


def testsLaunch():
    import div.tests.testsSuite as tests

    stopPycs()
    tests.run_tests()


def autoLogin():
    stopPycs()
    import div.selenium_folder.autoLogin as aL

    aL.autoLogin.login()


def main():

    # Lancement des tests..
    # testsLaunch()
    autoLogin()

    pass


if __name__ == "__main__":

    main()
    print("-" * 100, "FIN", "-" * 14)
