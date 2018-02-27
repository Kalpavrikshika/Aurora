import unittest

from arithmetics import Arithmetics
app = Arithmetics()
class ArithmeticsTest(unittest.TestCase):

    def test_addition(self):
        add = app.addition(3,7)
        self.assertEqual(10,add)

if __name__ == '__main__':
    unittest.main()