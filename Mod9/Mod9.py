class Ase:
    def __init__(self, nimi, atk):
        self.nimi = nimi
        self.atk = atk

class Tiimi:
    def __init__(self, hahmot):
        hahmot = []

    def tulosta(self):
        print('')
        for h in hahmot:
            h.tulosta()

    def lisää_hahmo(self):


class Hahmo:
    def __init__(self, nimi, ase):
        self.nimi = nimi
        self.exp = 0
        self.level = 1
        self.ase = ase

    def paranna(self, exp_muutos):
        self.exp += exp_muutos
        levelmuutos = self.exp//100
        self.level += levelmuutos
        self.exp -= levelmuutos*100

    def tulosta(self):
        print(f"Hahmo: {self.nimi}, Level: {self.level}, exp: {self.exp}, Ase= {self.ase.nimi}")

    def aseta_ase(self, ase):
        self.ase = ase


t = Tiimi()

h1 = Hahmo("Jojo", 'nyrkit')
h2 = Hahmo("Smoky The Bear", 'nyrkit')

t.hahmot.append(h1)
t.hahmot.append(h2)



a0 = Ase("Nyrkit", 1)
a1 = Ase("Sword", 8)
a2 = Ase("Big Fucking Gun", 999)


h1.paranna(80)
h2.paranna(135)

h1.paranna(127)

h1.aseta_ase(a2)
h2.aseta_ase(a1)

h1.tulosta()
h2.tulosta()


