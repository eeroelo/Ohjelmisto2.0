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






autolista = []
kerrat = 1
while kerrat < 6:
    rekisteritunnus = 'ABC-' + str(kerrat)
    huippunopeus = random.randint(100, 200)
    auto1 = Auto(rekisteritunnus, huippunopeus, 0, 0)
    autolista.append(auto1)
    kerrat += 1





class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.kilpailun_id = nimi
        self.matka = pituus
        self.osallistujat = autot
        self.osallistujat = autolista
        #for a in range(autot):
            #self.osallistujat.append(Auto)


    def tunti_kuluu(self):
        #Aikaa kuluu yksi tunti käyttää auton "kulje" metodia.



    def tulosta_tilanne(self):
        #Tulostaa autojen rekisterin, nopeuden ja kuljetun matkan.



    def kilpailu_ohi(self):
        print(f'Nimi: {self.kilpailun_id}, matka: {self.matka} ')

k1 = Kilpailu('Suuri romuralli', 8000, autolista)

#k1.kilpailu_ohi()
#k1.tulosta_tilanne()
k1.tunti_kuluu()


