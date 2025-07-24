import unittest

import time


class Calc(unittest.TestCase):

    def test_simpleCalc(self):
        self.assertEqual(2+3, 5)

if __name__ == "__main__":

    unittest.main()
