
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Julkaisun nimi on {self.nimi}')

#-----------------------------------------------------------------------
class Kirja(Julkaisu):
    def __init__(self, nimi, sivumaara, kirjoittaja):
        Julkaisu.__init__(self, nimi)
        self.sivumaara = sivumaara
        self.kirjoittaja = kirjoittaja

    def tulosta_tiedot(self):
        print(f'Kirjan nimi on {self.nimi}, sivuja kirjassa on {self.sivumaara} ja '
              f'kirjan on kirjoittanut {self.kirjoittaja}.')

#-----------------------------------------------------------------------

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f'Lehden nimi on {self.nimi} ja päätoimittaja {self.paatoimittaja}')


sl1 = Lehti('Aku Ankka', 'Aki Hyyppä')
sl1.tulosta_tiedot()

k1 = Kirja('Hytti no:6', 200, 'Rosa Liksom')
k1.tulosta_tiedot()

#ttt = Julkaisu('Nakkeja suolaliemessa simpukoiden kanssa')
#ttt.tulosta_tiedot()

