import pickle
from pickle import *

class Vehiculo:

    def caract(self):
        self.color = "rojo"
        self.puertas = 5
        self.modelo = "deportivo"
        print('Puertas:',self.puertas,
              '\nColor:',self.color,
              '\nModelo:', self.modelo)

    def __init__(self, self.color, self.puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas

Coche = Vehiculo()
caract = Coche.caract()

print(caract)

archivo = open('archivo2.txt','w')

pickle.dump(caract,archivo)

new = load(archivo)
print(new)
archivo.close()