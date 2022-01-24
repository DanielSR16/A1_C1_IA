import random
from unicodedata import name
import math
from main import binario_to_Decimal

class Individuo():
    def __init__(self,id):
        self.id = id
        self.genotipo_X = []
        self.genotipo_Y = []
        self.i_X = 0
        self.i_Y = 0
        self.fenotipo_X = 0
        self.fenotipo_Y = 0
        self.aptitud = 0
    
    def genotipoX(self,bits_X):
        bitsString = ''
        for i in range(0,bits_X):
            randomBits = random.choices((1,0))
            self.genotipo_X.append(randomBits[0])
            bitsString = bitsString + str(randomBits[0])
        self.i_X = binario_to_Decimal(int(bitsString))

    def genotipoY(self,bits_Y):
        bitsString = ''
        for i in range(0,bits_Y):
            randomBits = random.choices((1,0))
            self.genotipo_Y.append(randomBits[0])
            bitsString = bitsString + str(randomBits[0])
        self.i_Y = binario_to_Decimal(int(bitsString))

    def fenotipoX(self,posicion,delta):
        self.fenotipo_X = posicion + self.i_X * delta

    def fenotipoY(self,posicion,delta):
        self.fenotipo_Y = posicion + self.i_Y * delta
    
    def formula(self):
        self.aptitud = self.fenotipo_X**2 * math.sin(self.fenotipo_Y) - 2 * self.fenotipo_Y**2 * math.cos(self.fenotipo_X)
       
    def binario_to_Decimal(binario):
        decimal = 0
        i = 0
        while (binario>0):
            digito  = binario%10
            binario = int(binario//10)
            decimal = decimal+digito*(2**i)
            i = i+1
        # SALIDA
        return decimal

    def crearIndividuo(self,bits_X,bits_Y,posicionX,deltaX,posicionY,deltaY):
        self.genotipoX(bits_X)
        self.genotipoY(bits_Y)
        self.fenotipoX(posicion=posicionX,delta=deltaX)
        self.fenotipoY(posicion=posicionY,delta=deltaY)
        self.formula()
    

    def toString(self):
        return f'id: {self.id}\n' + f'Genotipo X: {self.genotipo_X}\n' + f'Genotipo Y: {self.genotipo_Y}\n' + f'i_X: {self.i_X}\n'+ f'i_Y: {self.i_Y}\n'+f'Fenotipo_X: {self.fenotipo_X}\n'+ f'Fenotipo_Y: {self.fenotipo_Y}\n' +f'aptiud: {self.aptitud}'
  




#CREAR INDIVIDUOS
#    - i tiene que ser menor o igual a los valores del inviduos
#Cruza
#Mutacion
#poda
