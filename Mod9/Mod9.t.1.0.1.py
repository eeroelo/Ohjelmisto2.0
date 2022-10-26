class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto1 = Auto('ABC-123', 142, 0, 0)
print(f"Auton rekisteritunnus on {auto1.rekisteritunnus}, huippunopeus {auto1.huippunopeus}km/h,",
      f"tämänhetkinen nopeus {auto1.tämänhetkinen_nopeus}km/h ja kuljettu matka {auto1.kuljettu_matka} kilometriä")