class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.exp = 0
        self.level = 1

    def paranna(self, exp_muutos):
        self.exp += exp_muutos
        levelmuutos = self.exp//100
        self.level += levelmuutos
        self.exp -= levelmuutos*100

    def tulosta(self):
        print(f"Hahmo: {self.nimi}, Level: {self.level}, exp: {self.exp}")




h1 = Hahmo("Jojo")
h2 = Hahmo("Smoky The Bear")

h1.tulosta()
h2.tulosta()

h1.paranna(80)
h2.paranna(135)
h1.paranna(127)

h1.tulosta()
h2.tulosta()