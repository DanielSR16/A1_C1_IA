from cmath import sin
from main import *
import random
import math
tablaGeneralY = []
id_Y = []
genotipoY = []
iY = []
fenotipoY = []

id = ["A","B","C","D","E","F","G"]

  

print('valores X: ',valoresX)
print('valores Y: ',valoresY)

print('bits valores x: ',2**num_Bits(valoresX))
print('bits valores y: ',2**num_Bits(valoresY))


resolucion_deltaX = RXnew / 2**num_Bits(valoresX)
resolucion_deltaY = RYnew / 2**num_Bits(valoresY)

print(resolucion_deltaX)
print(resolucion_deltaY)

# formula = valorX**2 * sin 
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
    for a  in range(0,tam_pob_incial):
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

   
    
    for j in range(0,tam_pob_incial):
        fenotipo = x[0] + iX[j] * resolucion_deltaX
        fenotipoRedondeado = round(fenotipo,4)
        fenotipoX.append(fenotipoRedondeado)
    tablaGeneralX.append(fenotipoX)
    print(tablaGeneralX)  

def creacionTabla(tam_pob_incial,valores_tabla,resolucion_delta):
  
    tablaGeneral = []
    id_tabla = []
    genotipo_tabla = []
    i_tabla = []
    fenotipo_tabla = []
    contadorID_tabla = 0 
    listaAux_tabla = []
    contadorBits_tabla = ''



    #Nombre al individuo
    for i in range(0,tam_pob_incial):
     
        id_tabla.append(id[contadorID_tabla])
    
        contadorID_tabla = contadorID_tabla + 1
    
    
    tablaGeneral.append(id_tabla)
   

    #Generar Genotipo y generar i
    for a  in range(0,tam_pob_incial):
        for j in range(0, num_Bits(valores_tabla)):
            randomBits = random.choices((1,0))
            contadorBits_tabla = contadorBits_tabla + str(randomBits[0])  
            listaAux_tabla.append(randomBits[0])
        
        genotipo_tabla.append(listaAux_tabla)
        i_tabla.append(binario_to_Decimal(int(contadorBits_tabla)))
        contadorBits_tabla = ''
        listaAux_tabla = []
    
    
    tablaGeneral.append(genotipo_tabla)
    tablaGeneral.append(i_tabla)

   
    
    for j in range(0,tam_pob_incial):
        #checar
        fenotipo = x[0] + i_tabla[j] * resolucion_delta
        fenotipoRedondeado = round(fenotipo,4)
        fenotipo_tabla.append(fenotipoRedondeado)
    tablaGeneral.append(fenotipo_tabla)
   
    return tablaGeneral

tabla_X = creacionTabla(tam_pob_incial= tam_pob_incial,valores_tabla=valoresX,resolucion_delta=resolucion_deltaX)
tabla_Y = creacionTabla(tam_pob_incial= tam_pob_incial,valores_tabla=valoresY,resolucion_delta=resolucion_deltaY)

print(tabla_X)
print(tabla_Y)


