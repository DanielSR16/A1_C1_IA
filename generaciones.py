from traceback import print_tb
from individuo import *
import random
import operator
import statistics
resolucion = 0.001
x = [2,7]
y = [6,8]

RX = x[0] - x[1]
RXnew = abs(RX)
RY = y[0] - y[1]
RYnew = abs(RY)
valoresX = round(RXnew / resolucion + 1)
valoresY = round(RYnew / resolucion + 1)
tam_pob_incial = 7
prob_muta_individuo = 0.5
prob_mut_gen = 0.08
tam_pob_max = 20
num_generaciones = 5

id = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","V","X","Y","Z"]

listaPoblacion = {}
listNombres = []

resuldos_finales =[]
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


print('valores X: ',valoresX)
print('valores Y: ',valoresY)

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

    cruza2(listaPoblacion,listNombres)
        


   
        
    
def cruza2(lista_individuos,lista_Nombre):
    listaCruzas = []
    listaAux = []
    lista_aux_cruzados = {}
    nombres_cruzados = []
    while len(lista_Nombre) > 1: 
        indv1 = random.choice(lista_Nombre)
        listaAux.append(indv1)
        lista_Nombre.remove(indv1)
        indv2 = random.choice(lista_Nombre)
        listaAux.append(indv2)
        lista_Nombre.remove(indv2)
        listaCruzas.append(listaAux)
        listaAux = []
    if(len(lista_Nombre) == 1):
        listaCruzas.append([lista_Nombre[0],lista_Nombre[0]])
    
    for indiv_cruzar in listaCruzas:
        print('--------------------------------------')
        print(indiv_cruzar)
        genotipo_x_1 = []
        genotipo_x_2 = []
        genotipo_y_1 = []
        genotipo_y_2 = []

        change_genotipo_1_x = []
        change_genotipo_1_y = []
        change_genotipo_2_x = []
        change_genotipo_2_y = []
        #llenar listas de genotipos a cruzar
        genotipo_x_1.extend(lista_individuos[indiv_cruzar[0]].genotipo_X)
        genotipo_y_1.extend(lista_individuos[indiv_cruzar[0]].genotipo_Y)
        genotipo_x_2.extend(lista_individuos[indiv_cruzar[1]].genotipo_X)
        genotipo_y_2.extend(lista_individuos[indiv_cruzar[1]].genotipo_Y)
        
        print('X1:',genotipo_x_1)
        print('Y1:',genotipo_y_1)
        print('X2:',genotipo_x_2)
        print('Y2:',genotipo_y_2)
        #eleccion de punto de cruza
        cruza_X = random.randint(1,len(genotipo_x_1)-1)
        cruza_Y = random.randint(1,len(genotipo_y_1)-1)
        #guardar los elementos a intercambiar
        change_genotipo_1_x = genotipo_x_1[cruza_X:len(genotipo_x_1)]
        change_genotipo_1_y = genotipo_y_1[cruza_Y:len(genotipo_y_1)]
        change_genotipo_2_x = genotipo_x_2[cruza_X:len(genotipo_x_2)]
        change_genotipo_2_y = genotipo_y_2[cruza_Y:len(genotipo_y_2)]

        print('cruzas!!!!')
        print(cruza_X)
        print(cruza_Y)
        print('cambios')
        print('X1',change_genotipo_1_x)
        print('Y1',change_genotipo_1_y)
        print('X2',change_genotipo_2_x)
        print('Y2',change_genotipo_2_y)

        #limpar genotipos hasta su puto de cruza

        for limpiar_x in range(0,len(genotipo_x_1)-cruza_X):
            genotipo_x_1.pop()
            genotipo_x_2.pop()

       
        for limpiar_y in range(0,len(genotipo_y_1)-cruza_Y):
            genotipo_y_1.pop()
            genotipo_y_2.pop()

        print('Limpios')
        print('X1:',genotipo_x_1)
        print('Y1:',genotipo_y_1)
        print('X2:',genotipo_x_2)
        print('Y2:',genotipo_y_2)

        #CRUZA DE DATOS
        #X
        genotipo_x_1.extend(change_genotipo_2_x)
        genotipo_x_2.extend(change_genotipo_1_x)

        #Y
        genotipo_y_1.extend(change_genotipo_2_y)
        genotipo_y_2.extend(change_genotipo_1_y)
           
        
        print('CRUZADOS')
        print('X1:',genotipo_x_1)
        print('Y1:',genotipo_y_1)
        print('X2:',genotipo_x_2)
        print('Y2:',genotipo_y_2)
        #añadir nuevos inviduos a la poblacion
        nombre_nuevo_individuo = indiv_cruzar[0] + indiv_cruzar[1]
        nuevo_individuo = Individuo(nombre_nuevo_individuo)
        nuevo_individuo.individuo_temporal(genotipo_x_1,genotipo_y_1)
        lista_aux_cruzados[nombre_nuevo_individuo] = nuevo_individuo
        nombres_cruzados.append(nombre_nuevo_individuo)

        # listaPoblacion[nombre_nuevo_individuo] = nuevo_individuo
        # listNombres.append(nombre_nuevo_individuo)

        nombre_nuevo_individuo2 = indiv_cruzar[1] + indiv_cruzar[0]
        nuevo_individuo2 = Individuo(nombre_nuevo_individuo2)
        nuevo_individuo2.individuo_temporal(genotipo_x_2,genotipo_y_2)
        lista_aux_cruzados[nombre_nuevo_individuo2] = nuevo_individuo2
        nombres_cruzados.append(nombre_nuevo_individuo2)

        # listaPoblacion[nombre_nuevo_individuo2] = nuevo_individuo2
        # listNombres.append(nombre_nuevo_individuo2)
    print('POBLACION XD')
    for indiv in listaPoblacion.values():
        print(indiv.toString())

    # if(len(listaPoblacion) < tam_pob_max):
    #     cruza2(listaPoblacion,listNombres)

    mutacion(lista_aux_cruzados,nombres_cruzados)



def mutacion(listaCruzados_aux,listaNombresAux):
    for i in listaNombresAux:
        contadorProGen_X = 0
        listaProGen_X  = []
        contadorProGen_Y = 0
        listaProGen_Y  = []
        mutacion_individuo = round(random.uniform(0,1),4)
       
   
        if(prob_muta_individuo <= mutacion_individuo):
            # print(f'puede mutar: {i}******************************************************')
            for cruzados_X in range(0,len(listaCruzados_aux[i].genotipo_X)):
                muta_gen_x = round(random.uniform(0,1),4)
                if(muta_gen_x <=prob_mut_gen ):
                    # print(f'muta en x = {muta_gen_x}')
                    listaProGen_X.append(contadorProGen_X-1)
                contadorProGen_X = contadorProGen_X + 1
            
            for cruzados_y in range(0,len(listaCruzados_aux[i].genotipo_Y)):
                muta_gen_y = round(random.uniform(0,1),4)
                if( muta_gen_y<= prob_mut_gen ):
                    # print(f'muta en y = {muta_gen_y}')
                    listaProGen_Y.append(contadorProGen_Y-1)
                contadorProGen_Y = contadorProGen_Y + 1
            # print(listaProGen_X)
            # print(listaProGen_Y)
           
            if(len(listaProGen_X)>0):
                for list_x in listaProGen_X:    
                    valor = listaCruzados_aux[i].genotipo_X[list_x]
                    if(valor == 1):
                        listaCruzados_aux[i].genotipo_X[list_x] = 0
                    elif valor == 0:
                        listaCruzados_aux[i].genotipo_X[list_x] = 1
                    
    

            if(len(listaProGen_Y)>0):
                for list_y in listaProGen_Y:    
                    valor = listaCruzados_aux[i].genotipo_Y[list_y]
                    if(valor == 1):
                        listaCruzados_aux[i].genotipo_Y[list_y] = 0
                    elif valor == 0:
                        listaCruzados_aux[i].genotipo_Y[list_y] = 1
                


       
    for nuevosNombres in  listaNombresAux:
        print(nuevosNombres)
        listaCruzados_aux[nuevosNombres].completarIndividuo(resolucion_deltaX,resolucion_deltaY,x[0],y[0])
        listaPoblacion[nuevosNombres] = listaCruzados_aux[nuevosNombres]
        if listaPoblacion[nuevosNombres].i_X > valoresX or listaPoblacion[nuevosNombres].i_Y > valoresY:
            print('se borro: ',nuevosNombres)
            del listaPoblacion[nuevosNombres]
        else:
            listNombres.append(nuevosNombres)
    
    
    # for nueva in listaPoblacion.values():
    #     print('############  NUEVO   ############')
    #     print(nueva.toString())
    print('POBLACION EN CUENTA: ',len(listaPoblacion))
    print('POBLACION MAXIMIMA: ',tam_pob_max)
    if len(listaPoblacion) < tam_pob_max:
        cruza2(listaPoblacion,listNombres)
    else:
        poda()

def poda():
    print('entre a podar')
      

    aptitudes_generacion = {}
    for r in listaPoblacion.values():
        aptitudes_generacion[r.id] = r.aptitud
        

    aptitudes_sort = sorted(aptitudes_generacion.items(),key=operator.itemgetter(1),reverse=True)

    # for name in enumerate(aptitudes_sort):
    #     print(name[1])
    # print('TOTAL: ',len(aptitudes_sort))
    # print('BORRADO: ', tam_pob_max)
    if(len(aptitudes_sort) == tam_pob_max):
        print('son iguales xd')
        generaciones(aptitudes_sort)
    elif len(aptitudes_sort) > tam_pob_incial:
        for boorar_aptitud in range(0,len(aptitudes_sort)-tam_pob_max):
           aptitudes_sort.pop()
        generaciones(aptitudes_sort)

 
    # print('PODADO !!!!!!')
    # for name in enumerate(aptitudes_sort):
    #     print(name[1])
        
            




def generaciones(aptitudes_sort):
    lista_aux_media = []
    for dato in aptitudes_sort:
        lista_aux_media.append(dato[1])
    media = statistics.mean(lista_aux_media)

 
    resuldos_finales.append([aptitudes_sort[0][1],aptitudes_sort[len(aptitudes_sort)-1][1],media])
    print('a')
    print(resuldos_finales)
    contador_generaciones = 1


    #SE TERMINA MAÑANA XD
    A = 1



crear_poblacion(bits_X=bitsX,bits_Y=bitsY,posicionX=x[0],posicionY=y[0],deltaX=resolucion_deltaX,deltaY=resolucion_deltaY)




 

