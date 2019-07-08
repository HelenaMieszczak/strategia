import unittest
from wojownik import Wojownik, WojownikBlad
from jednostki.rycerz import Rycerz
from druzyna import Druzyna

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


class TestRycerz(unittest.TestCase):
    def test_atakuj(self):
        r = Rycerz()
        r.atakuj()
        self.assertEqual(0.3, r.doswiadczenie)

    def test_stworzenie_udane(self):
        r = Rycerz()
        self.assertEqual(r.zycie, 60)
        self.assertEqual(r.doswiadczenie, 0)

class TestDruzyna(unittest.TestCase):
    def test_stworzenie(self):
        d = Druzyna()
        self.assertEqual(d.wojownicy, [])

    def test_dodawanie(self):
        d = Druzyna()
        r1 = Rycerz()
        d.dodaj_wojownika(r1)
        self.assertEqual(d.wojownicy, [r1])


if __name__ == '__main__':
    unittest.main()
