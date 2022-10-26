class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka


    def kiihdyta(self, velo_change):
        self.tämänhetkinen_nopeus += velo_change
        ylaraja = self.huippunopeus
        alaraja = 0
        if self.tämänhetkinen_nopeus > ylaraja:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < alaraja:
            self.tämänhetkinen_nopeus = 0


    def tulosta(self):
        print(f"Auton {self.rekisteritunnus} nopeus on nyt {self.tämänhetkinen_nopeus} km/h")



auto1 = Auto('ABC-123', 142, 0, 0)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.tulosta()

auto1.kiihdyta(-200)

auto1.tulosta()

