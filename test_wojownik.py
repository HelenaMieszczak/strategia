import unittest
from wojownik import Wojownik, WojownikBlad


class WojownikTestCase(unittest.TestCase):
    def test_warrior_with_correct_life(self):
        w = Wojownik(30)
        self.assertEqual(w.zycie, 30)

    def test_wojownik_with_incorrect_life(self):
        self.assertRaises(ValueError)
        WojownikBlad(-10)

    def test_repr(self):
        w = Wojownik(10)
        expected = '''HP =  10 EXP =  0'''
        received = w.__repr__()

        self.assertEqual(expected, received)

    def test_marsz(self):
        w = Wojownik(30)
        w.maszeruj(1000)
        self.assertEqual(200.0, w.doswiadczenie)

if __name__ == '__main__':
    unittest.main()
