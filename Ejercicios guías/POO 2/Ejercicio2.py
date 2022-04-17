# Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.

class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def equilibrio(self, energia):
        if self.energia > 150 and self.energia < 300:
            print("está en equilibrio")
        else:
            print("no está en equilibrio")