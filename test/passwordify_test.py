import unittest
from passwordify import passwordify


class TestPasswordify(unittest.TestCase):
    def test_base(self):
        self.assertEqual(passwordify("AeopFabe"), "AeopFabe")

    def test_space(self):
        self.assertEqual(passwordify("Aeop Fabe"), "Aeop-Fabe")

    def test_s(self):
        self.assertEqual(passwordify("AesopsFabes"), "Ae$op$Fabe$")

    def test_l(self):
        self.assertEqual(passwordify("AesopSFables"), "Ae$op$Fab1e$")

    def test_multiple(self):
        self.assertEqual(passwordify("Aesops Fables"), "Ae$op$-Fab1e$")

    def test_zero(self):
        self.assertEqual(passwordify("zero"), "zero")

    def test_one(self):
        self.assertEqual(passwordify("one"), "one")

    def test_two(self):
        self.assertEqual(passwordify("two"), "2")

    def test_three(self):
        self.assertEqual(passwordify("three"), "3")

    def test_four(self):
        self.assertEqual(passwordify("four"), "four")

    def test_five(self):
        self.assertEqual(passwordify("five"), "five")

    def test_eight(self):
        self.assertEqual(passwordify("eight"), "eight")

    def test_nine(self):
        self.assertEqual(passwordify("nine"), "nine")

    def test_ten(self):
        self.assertEqual(passwordify("ten"), "10")

    def test_example(self):
        self.assertEqual(passwordify("sleeping in a tent"), "$1eeping-in-a-10t")

    def test_mixed(self):
        self.assertEqual(passwordify("one three sleep four"), "one-3-$1eep-four")

    def test_all(self):
        self.assertEqual(passwordify("atwood tent parsley threepeat cabin"), "a2od-10t-par$1ey-3peat-cabin")

if __name__ == '__main__':
    unittest.main()
