from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

rycerze = []

for _ in range(4):
    rycerze.append(Rycerz())


for rycerz in rycerze:
    rycerz.maszeruj(2000)

for rycerz in rycerze:
    rycerz.atakuj()

lucznicy = []

for _ in range(3):
    lucznicy.append(Lucznik())


for lucznik in lucznicy:
    lucznik.atakuj()


armia = lucznicy + rycerze

for wojownik in armia:
    wojownik.atakuj()

print(armia)