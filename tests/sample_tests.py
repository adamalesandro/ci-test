import unittest

from sgnl.sample import multiply


class TestFunctions(unittest.TestCase):

    def test_multiply_check(self):
        self.assertEqual(multiply(3, 3), 9)

    def test_precision(self):
        self.assertEqual(multiply(2, .22), .44)

    def test_none(self):
        with self.assertRaises(ValueError):
            multiply(2, None)


if __name__ == "__main__":
    unittest.main(exit=False)
