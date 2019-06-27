from wojownik import Wojownik


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__(10)

    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self.doswiadczenie += 0.4


