class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = (tilavuus + abs(tilavuus))//2
        self.saldo = (alku_saldo + abs(alku_saldo))//2 if alku_saldo <= tilavuus else tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            ota_kaikki = self.saldo
            self.saldo = 0.0
            return ota_kaikki

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
