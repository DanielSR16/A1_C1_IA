from main import *
import random

tablaGeneralY = []
id_Y = []
genotipoY = []
iY = []
fenotipoY = []

id = ["A","B","C","D","E","F","G"]
def creacionTabla():
  

    print('valores X: ',valoresX)
    print('valores Y: ',valoresY)

    print('bits valores x: ',2**num_Bits(valoresX))
    print('bits valores y: ',2**num_Bits(valoresY))

    
    resolucion_deltaX = RXnew / 2**num_Bits(valoresX)
    resolucion_deltaY = RYnew / 2**num_Bits(valoresY)

    print(resolucion_deltaX)
    print(resolucion_deltaY)


def creacionTablaX():
    tablaGeneralX = []
    id_X = []
    genotipoX = []
    iX = []
    fenotipoX = []
    contadorID = 0 
    listaAux = []
    contadorBits = ''

    #Nombre al individuo
    for i in range(0,tam_pob_incial):
     
        id_X.append(id[contadorID])
    
        contadorID = contadorID + 1
    
    
    tablaGeneralX.append(id_X)
   

    #Generar Genotipo y generar i
    for x  in range(0,tam_pob_incial):
        for j in range(0, num_Bits(valoresX)):
            randomBits = random.choices((1,0))
            contadorBits = contadorBits + str(randomBits[0])  
            listaAux.append(randomBits[0])
        
        genotipoX.append(listaAux)
        iX.append(binario_to_Decimal(int(contadorBits)))
        contadorBits = ''
        listaAux = []
    
    
    tablaGeneralX.append(genotipoX)
    tablaGeneralX.append(iX)

    print(tablaGeneralX)
    
    
     


creacionTablaX()



