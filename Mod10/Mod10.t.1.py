class Hissi:
    def __init__(self, nimi, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros
        self.hissi_nimi = nimi


    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alinkerros or kohdekerros > self.ylinkerros:
            print(f'Hississä ei ole kerrosta {kohdekerros}.')
            return


        while self.kerros < kohdekerros:
            self.kerros_ylos()

        while self.kerros > kohdekerros:
            self.kerros_alas()

        if self.kerros == kohdekerros:
            print(f'"Pling" hissi on kerroksessa: {kohdekerros} varo sulkeutuvia ovia.')

        return


    def kerros_alas(self):
        print(f'Hissi on kerroksessa: {self.kerros}')
        self.kerros -= 1
        return


    def kerros_ylos(self):
        print(f'Hissi on kerroksessa: {self.kerros}')
        self.kerros += 1
        return

h1 = Hissi('nimi', 1, 9)

h1.siirry_kerrokseen(5)
h1.siirry_kerrokseen(4)