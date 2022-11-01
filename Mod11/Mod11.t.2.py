import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, fuel, type):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
        self.tot_aika = 0
        self.fuel = fuel
        self.type = type


# Nopeus arvotaan randomilla, se ei voi ylittää max nopeutta.
    def kulje(self, tot_aika):
        self.tämänhetkinen_nopeus = random.randint(50, 200)
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

    # Kuljettu matka tunteina
        self.tot_aika += tot_aika

    # Auton tyyppi, eli type, määrää miten kulutus lasketaan.
        # Polttomoottori:
        if self.type == 'carbon':
            self.fuel -= tot_aika * self.tämänhetkinen_nopeus // 100 * 6.4

        # Sähkömoottori:
        elif self.type == 'elec':
            self.fuel -= (tot_aika * self.tämänhetkinen_nopeus) // 100 * 7.2

    # Polttoaine ei voi olla alle 0.
        if self.fuel < 0:
            self.fuel = 0

    # Kuljettu matka kilometreinä.
        self.kuljettu_matka = self.tot_aika * self.tämänhetkinen_nopeus



#-----------------------------------------------------------------------------------

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, fuel, type):
            Auto.__init__(self, rekisteritunnus, huippunopeus,fuel, type)

    #Polttomoottoriauton tiedot
    def auton_tiedot(self):
        print(f'Auton {self.rekisteritunnus} huippunopeus on {self.huippunopeus}km/h ja tankin vetoisuus {self.fuel}'
              f' litraa. Auto on tyypiltään polttomoottoriauto.')

    def tulosta_tiedot(self):
        print(f'Auto {self.rekisteritunnus} kulkee {self.tot_aika}h'
              f' nopeudella {self.tämänhetkinen_nopeus}km/h jonka jälkeen tankissa on noin {self.fuel //1} litraa.'
              f' Kuljettu matka kyseisessä ajassa <{self.kuljettu_matka}km>')


# -----------------------------------------------------------------------------------

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, fuel, type):
            Auto.__init__(self, rekisteritunnus, huippunopeus,fuel, type)

    # Sähköauton tiedot
    def auton_tiedot(self):
        print(f'Auton {self.rekisteritunnus} huippunopeus on {self.huippunopeus}km/h ja akun maksimilataus '
              f'{self.fuel}kWh. Auto on tyypiltään sähköauto.')


    def tulosta_tiedot(self):
        print(f'Auto {self.rekisteritunnus} kulkee {self.tot_aika}h nopeudella {self.tämänhetkinen_nopeus}km/h '
              f'jonka jälkeen akun lataus on {self.fuel}kWh. Kuljettu matka kyseisessä ajassa <{self.kuljettu_matka}km>')


# -----------------------------------------------------------------------------------



print('----------------------------------------------------------------')

toyota = Polttomoottoriauto('ACD-123', 165, 32.3, 'carbon')
toyota.auton_tiedot()
toyota.kulje(3)
toyota.tulosta_tiedot()
print('----------------------------------------------------------------')
tesla = Sahkoauto('ABC-15', 180, 52.5, 'elec')
tesla.auton_tiedot()
#tesla.kulje(int(input('Kuinka monta tuntia auto ajaa: ')))
tesla.kulje(3)
tesla.tulosta_tiedot()

