from wojownik import Wojownik


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__(10)
        self.strzaly = 15

    def atakuj(self, strzaly):
        strzelanie = True
        while strzelanie:
            print('Łucznik: Wypuściłem strzałę!')
            self.doswiadczenie += 0.4
            self.strzaly = self.strzaly - 1
            return self.doswiadczenie
            if self.strzaly == 0:
                print("Już nie postrzelasz")
                strzelanie = False





