import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka_h):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka_h = kuljettu_matka_h




    def kiihdyta(self, velo_change):
        self.tämänhetkinen_nopeus += velo_change
        ylaraja = self.huippunopeus
        alaraja = 0
        if self.tämänhetkinen_nopeus > ylaraja:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < alaraja:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, matka_h):
        #self.tot_aika += matka_h
        matka_h = matka_h * self.tämänhetkinen_nopeus
        self.kuljettu_matka_h += matka_h




    def tulosta(self):
        print(f"Auton {self.rekisteritunnus} nopeus on nyt {self.tämänhetkinen_nopeus} km/h ja kuljettu matka "
              f"ajassa {self.tot_aika}h on {self.kuljettu_matka_h} km.")


#(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka, tot_aika)
auto1 = Auto('ABC-123', 142, 0, 0)


autolista = []
kerrat = 1
while kerrat < 11:
    rekisteritunnus = 'ABC-' + str(kerrat)
    huippunopeus = random.randint(100, 200)
    auto1 = Auto(rekisteritunnus, huippunopeus, 0, 0)
    autolista.append(auto1)
    kerrat += 1

stop = False
while not stop:
    for i in autolista:
        muutos = random.randint(-10, 15)
        i.kiihdyta(muutos)

    for i in autolista:
        i.kulje(1)
        if i.kuljettu_matka_h < 10000:
            continue
        print('Voittaja on: ', i.rekisteritunnus)
        stop = True

print('Rekisteritunnus:        Huippunopeus:        Kuljettu matka:')
for i in autolista:
    print(f'{i.rekisteritunnus}                     {i.huippunopeus}km/h                      {i.kuljettu_matka_h}km')
