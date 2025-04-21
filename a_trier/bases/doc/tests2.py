import unittest, os, time


def average(lst):
    return sum(lst) / len(lst)


def main():
    os.environ["TZ"] = "UTC"
    # time.timeset()
    unittest.main()


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
        self.assertGreaterEqual(average([10, 15, 5]), average([2, 3, 7]))
        self.assertFalse(average([10, 15, 5])>10)


# if __name__ == "__main__":
#     unittest.main()

# unittest.main()  # Calling from the command line invokes all tests

print(average(['5', 7, 10]))
main()
