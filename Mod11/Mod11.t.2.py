import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka_h, tot_aika):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka_h = kuljettu_matka_h
        self.tot_aika = tot_aika



    def kiihdyta(self, velo_change):
        self.tämänhetkinen_nopeus += velo_change
        ylaraja = self.huippunopeus
        alaraja = 0
        if self.tämänhetkinen_nopeus > ylaraja:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < alaraja:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, matka_h):
        self.tot_aika += matka_h
        matka_h = matka_h * self.tämänhetkinen_nopeus
        self.kuljettu_matka_h += matka_h

#-----------------------------------------------------------------------------------

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka_h, tot_aika, tankki):
            Auto.__init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka_h, tot_aika)
            self.tankki = tankki

    def kulje(self, tot_aika):
        self.tämänhetkinen_nopeus = random.randint(50, 165)
        self.tot_aika += tot_aika
        self.tankki -= tot_aika * self.tämänhetkinen_nopeus//100 * 6.4
        if self.tankki < 0:
            self.tankki = 0


    def auton_tiedot(self):
        print(f'Auton {self.rekisteritunnus} huippunopeus on {self.huippunopeus}km/h ja tankin vetoisuus {self.tankki}'
              f' litraa.')

    def tulosta_tiedot(self):
        print(f'Auton {self.rekisteritunnus} huippunopeus on {self.huippunopeus}km/h. Auto kulkee {self.tot_aika}h'
              f' nopeudella {self.tämänhetkinen_nopeus}km/h jonka jälkeen tankissa on noin {self.tankki //1} litraa')


# -----------------------------------------------------------------------------------

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka_h, tot_aika, akku):
        Auto.__init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka_h, tot_aika)
        self.lataus = akku

    def kulje(self, tot_aika):
        self.tämänhetkinen_nopeus = random.randint(50, 180)
        self.tot_aika += tot_aika
        self.lataus -= tot_aika * (1.70 * self.tämänhetkinen_nopeus//100)
        if self.lataus < 0:
            self.lataus = 0

    def auton_tiedot(self):
        print(f'Auton {self.rekisteritunnus} huippunopeus on {self.huippunopeus}km/h ja akun maksimilataus on '
              f'{self.lataus}kWh')



    def tulosta_tiedot(self):
        print(f'Auton {self.rekisteritunnus} huippunopeus on {self.huippunopeus}km/h. Auto kulkee {self.tot_aika}h'
              f' nopeudella {self.tämänhetkinen_nopeus}km/h jonka jälkeen akun lataus on {self.lataus}kWh')



tesla = Sahkoauto('ABC-15', 180, 0, 0, 0, 52.5)
tesla.auton_tiedot()
#tesla.kulje(int(input('Kuinka monta tuntia auto ajaa: ')))
tesla.kulje(3)
tesla.tulosta_tiedot()


#toyota = Polttomoottoriauto('ACD-123', 165, 0, 0, 0, 32.3)
#toyota.auton_tiedot()
#toyota.kulje(3)
#toyota.tulosta_tiedot()

