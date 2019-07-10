class WojownikBlad(Exception):
    def __repr__(self):
        return"Bardzo umarł."


class Wojownik:
    def __init__(self, zycie):
        self.doswiadczenie = 0
        self.zycie = zycie

        if zycie < 0:
            raise WojownikBlad

    def __repr__(self):
        nazwa = self.__class__.__name__
        return f"\n{nazwa}: \nHP =  {self.zycie} \nEXP =  {self.doswiadczenie}"

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print(f"{nazwa}: przeszedłem {dystans} m")
        self.doswiadczenie += dystans * 0.2

