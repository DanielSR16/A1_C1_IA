from individuo import *
import random
resolucion = 0.001
x = [2,7]
y = [6,8]

RX = x[0] - x[1]
RXnew = abs(RX)
RY = y[0] - y[1]
RYnew = abs(RY)
valoresX = round(RXnew / resolucion + 1)
valoresY = round(RYnew / resolucion + 1)
tam_pob_incial = 4
prob_muta_individual = 0.1
prob_mut_gen = 0.05
tam_pob_max = 10
id = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","V","X","Y","Z"]
listaPoblacion = {}
listNombres = []

# Bits de valores
def num_Bits(valor):
    aux=0
    i=1
    bits=0
    while aux <= valor:
        aux=pow(2, i)
        bits=i
        i=i+1
    return bits


# print('valores X: ',valoresX)
# print('valores Y: ',valoresY)

# print('bits valores x: ',2**num_Bits(valoresX))
# print('bits valores y: ',2**num_Bits(valoresY))
bitsX = num_Bits(valoresX)

bitsY = num_Bits(valoresY)

resolucion_deltaX = round(RXnew / 2**num_Bits(valoresX),5)
resolucion_deltaY = round(RYnew / 2**num_Bits(valoresY),5)

# print(resolucion_deltaX)
# print(resolucion_deltaY)

def crear_poblacion(bits_X,bits_Y,posicionX,posicionY,deltaX,deltaY):
    contador = 0
    print('soy delta Y : ',deltaY)

    while contador < tam_pob_incial:
        indiv = Individuo(id[contador])
        indiv.crearIndividuo(bits_X=bits_X,bits_Y=bits_Y,posicionX=posicionX,posicionY=posicionY,deltaX=deltaX,deltaY=deltaY)
        if(indiv.i_X <= valoresX and indiv.i_Y <= valoresY):
            listaPoblacion[id[contador]] = indiv 
            listNombres.append(id[contador])
            contador = contador + 1

    
        

crear_poblacion(bits_X=bitsX,bits_Y=bitsY,posicionX=x[0],posicionY=y[0],deltaX=resolucion_deltaX,deltaY=resolucion_deltaY)

def cruza():
       
    listaRandom = []
    listaRandom.extend(listNombres)
    
    listaAux = []
    listaCruzas = []
    while len(listaRandom) > 1: 
        indv1 = random.choice(listaRandom)
        listaAux.append(indv1)
        listaRandom.remove(indv1)
        indv2 = random.choice(listaRandom)
        listaAux.append(indv2)
        listaRandom.remove(indv2)
        listaCruzas.append(listaAux)
        listaAux = []
    print(listaCruzas)
    print(listaRandom)
   

    for valoresCruzados in listaCruzas:
        genotipo_x_1 = []
        genotipo_y_1 = []
        genotipo_x_2 = []
        genotipo_y_2 = []

        genotipo_x_1 = listaPoblacion[valoresCruzados[0]].genotipo_X
        genotipo_y_1 = listaPoblacion[valoresCruzados[0]].genotipo_Y
        genotipo_x_2 = listaPoblacion[valoresCruzados[1]].genotipo_X
        genotipo_y_2 = listaPoblacion[valoresCruzados[1]].genotipo_Y

        
        

        #cruza X
        cruza_X = random.randint(1,len(genotipo_x_1)-1)
        print(valoresCruzados)
        print('cruza x')
        print(cruza_X)
        print(genotipo_x_1)
        print(genotipo_x_2)
        print('intercambiar X1')
        print(genotipo_x_1[cruza_X:len(genotipo_x_1)])
        print('intercambiar X2')
        print(genotipo_x_2[cruza_X:len(genotipo_x_2)])

        cruzar_datos_x1 = genotipo_x_1[cruza_X:len(genotipo_x_1)]
        cruzar_datos_x2 = genotipo_x_2[cruza_X:len(genotipo_x_2)]

        for x in range(0,len(genotipo_x_1)-cruza_X):
            genotipo_x_1.pop()
            genotipo_x_2.pop()
        
        print('borrado')
        print(genotipo_x_1)
        print(genotipo_x_2)
        genotipo_x_1.extend(cruzar_datos_x2)
        genotipo_x_2.extend(cruzar_datos_x1)
        print('nuevos')
        print(genotipo_x_1)
        print(genotipo_x_2)
        # print(genotipo_x_2)
       
        print('####################################################################')
        #Cruzas Y

        cruza_Y = random.randint(1,len(genotipo_y_1)-1)
        print('cruza Y')
        print(cruza_Y)
        print(genotipo_y_1)
        print(genotipo_y_2)
        print('intercambiar Y1')
        print(genotipo_y_1[cruza_Y:len(genotipo_y_1)])
        print('intercambiar Y2')
        print(genotipo_y_2[cruza_Y:len(genotipo_y_2)])
        
        
        cruzar_datos_y1 = genotipo_y_1[cruza_Y:len(genotipo_y_1)]
        cruzar_datos_y2 = genotipo_y_2[cruza_Y:len(genotipo_y_2)]

        for x in range(0,len(genotipo_y_1)-cruza_Y):
            genotipo_y_1.pop()
            genotipo_y_2.pop()

        print('borrado')
        print(genotipo_y_1)
        print(genotipo_y_2)
        genotipo_y_1.extend(cruzar_datos_y2)
        genotipo_y_2.extend(cruzar_datos_y1)
        print('nuevos')
        print(genotipo_y_1)
        print(genotipo_y_2)

        print("____________________________________________________________________")
   

        

        
        
    for i in listNombres:    
        print(listaPoblacion[i].toString())
   


cruza()
 

