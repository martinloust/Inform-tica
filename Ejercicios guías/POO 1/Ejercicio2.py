# Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if (self.energia - 10 + kms) > 0:
        self.energia -= 10 + kms
    else: 
        print("tiene que reponer energía")
