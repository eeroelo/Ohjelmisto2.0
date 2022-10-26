

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




    def tulosta(self):
        print(f"Auton {self.rekisteritunnus} nopeus on nyt {self.tämänhetkinen_nopeus} km/h ja kuljettu matka "
              f"ajassa {self.tot_aika}h on {self.kuljettu_matka_h} km.")


#(rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka, tot_aika)
auto1 = Auto('ABC-123', 142, 0, 0, 0)

auto1.kiihdyta(60)
auto1.kulje(1.5)
auto1.tulosta()






