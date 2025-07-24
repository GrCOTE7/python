import unittest

import div.tests.Calc as Calc
import div.tests.WebsitesSanityChecks as WebsitesSanityChecks

def run_tests():
    simpleCalc = unittest.defaultTestLoader.loadTestsFromModule(Calc)
    webAccess = unittest.defaultTestLoader.loadTestsFromModule(WebsitesSanityChecks)

    tests = [
        simpleCalc,
        # webAccess,
    ]

    combined_suite = unittest.TestSuite(tests)

    runner = unittest.TextTestRunner()

    # print("Je vais tester les accès à 2 sites...\n")
    runner.run(combined_suite)
