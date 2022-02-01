from traceback import print_tb
from individuo import *
from formulario import *
import random
import operator
import statistics
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

vista_entrada = Formulario()
vista_entrada.vista()
print('soy el X1: ',vista_entrada.posicionX_1)

resolucion = float(vista_entrada.resolucion)
x = [float(vista_entrada.posicionX_1),float(vista_entrada.posicionX_2)]
y = [float(vista_entrada.posicionY_1),float(vista_entrada.posicionY_2)]

RX = x[0] - x[1]
RXnew = abs(RX)
RY = y[0] - y[1]
RYnew = abs(RY)
valoresX = round(RXnew / resolucion + 1)
valoresY = round(RYnew / resolucion + 1)

tam_pob_incial = int(vista_entrada.tamaño_poblacion_inicial)
prob_muta_individuo = float(vista_entrada.probabilidad_mutacion_individual)
prob_mut_gen = float(vista_entrada.probabilidad_mutacion_genetica)
tam_pob_max = int(vista_entrada.tamaño_poblacion_maxima)
num_generaciones = int(vista_entrada.generaciones)


id = ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","V","X","Y","Z"]

listaPoblacion = {}
listNombres = []

resuldos_finales =[]
contador_generaciones = 0

total_mejor = []
total_peor = []
total_promedio = []

total_generaciones = []
for i in range(1,num_generaciones+1):
    total_generaciones.append(i)
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

def crear_poblacion(bits_X,bits_Y,posicionX,posicionY,deltaX,deltaY,contador_gen):
    contador = 0
    print('soy delta Y : ',deltaY)

    while contador < tam_pob_incial:
        indiv = Individuo(id[contador])
        indiv.crearIndividuo(bits_X=bits_X,bits_Y=bits_Y,posicionX=posicionX,posicionY=posicionY,deltaX=deltaX,deltaY=deltaY)
        if(indiv.i_X <= valoresX and indiv.i_Y <= valoresY):
            listaPoblacion[id[contador]] = indiv 
            listNombres.append(id[contador])
            contador = contador + 1

    cruza2(listaPoblacion,listNombres,contador_gen)
        


   
        
    
def cruza2(lista_individuos,lista_Nombre,contador_gen):

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
        # print('--------------------------------------')
        # print(indiv_cruzar)
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
        
        # print('X1:',genotipo_x_1)
        # print('Y1:',genotipo_y_1)
        # print('X2:',genotipo_x_2)
        # print('Y2:',genotipo_y_2)
        #eleccion de punto de cruza
        cruza_X = random.randint(1,len(genotipo_x_1)-1)
        cruza_Y = random.randint(1,len(genotipo_y_1)-1)
        #guardar los elementos a intercambiar
        change_genotipo_1_x = genotipo_x_1[cruza_X:len(genotipo_x_1)]
        change_genotipo_1_y = genotipo_y_1[cruza_Y:len(genotipo_y_1)]
        change_genotipo_2_x = genotipo_x_2[cruza_X:len(genotipo_x_2)]
        change_genotipo_2_y = genotipo_y_2[cruza_Y:len(genotipo_y_2)]

        # print('cruzas!!!!')
        # print(cruza_X)
        # print(cruza_Y)
        # print('cambios')
        # print('X1',change_genotipo_1_x)
        # print('Y1',change_genotipo_1_y)
        # print('X2',change_genotipo_2_x)
        # print('Y2',change_genotipo_2_y)

        #limpar genotipos hasta su puto de cruza

        for limpiar_x in range(0,len(genotipo_x_1)-cruza_X):
            genotipo_x_1.pop()
            genotipo_x_2.pop()

       
        for limpiar_y in range(0,len(genotipo_y_1)-cruza_Y):
            genotipo_y_1.pop()
            genotipo_y_2.pop()

        # print('Limpios')
        # print('X1:',genotipo_x_1)
        # print('Y1:',genotipo_y_1)
        # print('X2:',genotipo_x_2)
        # print('Y2:',genotipo_y_2)

        #CRUZA DE DATOS
        #X
        genotipo_x_1.extend(change_genotipo_2_x)
        genotipo_x_2.extend(change_genotipo_1_x)

        #Y
        genotipo_y_1.extend(change_genotipo_2_y)
        genotipo_y_2.extend(change_genotipo_1_y)
           
        
        # print('CRUZADOS')
        # print('X1:',genotipo_x_1)
        # print('Y1:',genotipo_y_1)
        # print('X2:',genotipo_x_2)
        # print('Y2:',genotipo_y_2)
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
    # print('POBLACION XD')
    # for indiv in listaPoblacion.values():
    #     print(indiv.toString())

    # if(len(listaPoblacion) < tam_pob_max):
    #     cruza2(listaPoblacion,listNombres)

    mutacion(lista_aux_cruzados,nombres_cruzados,contador_gen)



def mutacion(listaCruzados_aux,listaNombresAux,contador_gen):
    for i in listaNombresAux:
        contadorProGen_X = 0
        listaProGen_X  = []
        contadorProGen_Y = 0
        listaProGen_Y  = []
        mutacion_individuo = round(random.uniform(0,1),4)
       
   
        if(prob_muta_individuo <= mutacion_individuo):
         
            for cruzados_X in range(0,len(listaCruzados_aux[i].genotipo_X)):
                muta_gen_x = round(random.uniform(0,1),4)
                if(muta_gen_x <=prob_mut_gen ):
               
                    listaProGen_X.append(contadorProGen_X-1)
                contadorProGen_X = contadorProGen_X + 1
            
            for cruzados_y in range(0,len(listaCruzados_aux[i].genotipo_Y)):
                muta_gen_y = round(random.uniform(0,1),4)
                if( muta_gen_y<= prob_mut_gen ):
                
                    listaProGen_Y.append(contadorProGen_Y-1)
                contadorProGen_Y = contadorProGen_Y + 1
      
           
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
        # print(nuevosNombres)
        listaCruzados_aux[nuevosNombres].completarIndividuo(resolucion_deltaX,resolucion_deltaY,x[0],y[0])
        listaPoblacion[nuevosNombres] = listaCruzados_aux[nuevosNombres]
        if listaPoblacion[nuevosNombres].i_X > valoresX or listaPoblacion[nuevosNombres].i_Y > valoresY:
            # print('se borro: ',nuevosNombres)
            del listaPoblacion[nuevosNombres]
        else:
            listNombres.append(nuevosNombres)
    
    
    # for nueva in listaPoblacion.values():
    #     print('############  NUEVO   ############')
    #     print(nueva.toString())
    # print('POBLACION EN CUENTA: ',len(listaPoblacion))
    # print('POBLACION MAXIMIMA: ',tam_pob_max)
    if len(listaPoblacion) < tam_pob_max:
        cruza2(listaPoblacion,listNombres,contador_gen)
    elif len(listaPoblacion) >= tam_pob_max:
        poda(contador_gen)

def poda(contador_gen):
    # for todos in listaPoblacion.values():
    #     print(todos.toString())
    #     print('______________________________________')
      

    aptitudes_generacion = {}
    for r in listaPoblacion.values():
        aptitudes_generacion[r.id] = r.aptitud
        

    aptitudes_sort = sorted(aptitudes_generacion.items(),key=operator.itemgetter(1),reverse=True)
    total_peor.append(aptitudes_sort[len(aptitudes_sort)-1][1])

    # for name in enumerate(aptitudes_sort):
    #     print(name[1])
    # print('TOTAL: ',len(aptitudes_sort))
    # print('BORRADO: ', tam_pob_max)
 
    if(len(aptitudes_sort) == tam_pob_max):
        print('son iguales xd')
        generaciones(aptitudes_sort,contador_gen)
    elif len(aptitudes_sort) > tam_pob_incial:
        for boorar_aptitud in range(0,len(aptitudes_sort)-tam_pob_max):
           aptitudes_sort.pop()
        generaciones(aptitudes_sort,contador_gen)

 
    # print('PODADO !!!!!!')
    # for name in enumerate(aptitudes_sort):
    #     print(name[1])
        
            




def generaciones(aptitudes_sort,contador_gen):

    contador_gen = contador_gen + 1
    print(contador_gen)
    new_poblacion = {}
    new_nombres_poblacion = []

    lista_aux_media = []
    for dato in aptitudes_sort:
        lista_aux_media.append(dato[1])
    media = statistics.mean(lista_aux_media)
    resuldos_finales.append([aptitudes_sort[0][1],media])

    print('datos metidos en new poblation')
    for datos_new in aptitudes_sort:
        new_poblacion[datos_new[0]] = listaPoblacion[datos_new[0]]
    
    listaPoblacion.clear()
    

    for datos_new2 in aptitudes_sort:
        listaPoblacion[datos_new2[0]] = new_poblacion[datos_new2[0]]
        new_nombres_poblacion.append(datos_new2[0])
    #editar
    # x=[1,2,3,4,5,6]
    # y=[2,1,5,6,3,9]

    # plt.scatter(x, y)
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.title("Scatter Plot")
    # plt.show()

    if contador_gen < num_generaciones:
        completarGeneraciones(listaPoblacion,new_nombres_poblacion,contador_gen)
    if contador_gen == num_generaciones:
        
        for resul in resuldos_finales:
            
            total_mejor.append(resul[0])
            total_promedio.append(resul[1])
         
        

def completarGeneraciones(lista_new_plobation,lista_new_Nombres,contador_gen):
    

     cruza2(lista_new_plobation,lista_new_Nombres,contador_gen)

# def metodo ():
    
      
    
def grafica():
   

     #Primera Tabla
  
   
    figure = plt.figure(figsize=(15,10))
    ax = plt.subplot(1,1,1)
    ax.plot( total_generaciones,total_promedio, label='Promedio',marker='.')  # Plot some data on the (implicit) axes.
    ax.plot( total_generaciones,total_peor, label='Peor',marker='.')  # etc.
    ax.plot( total_generaciones,total_mejor,label='Mejor',marker='.')
    ax.set_ylabel('Aptitud')
    ax.set_xlabel('Generaciones')

    blue_line = mlines.Line2D([], [], color='blue', 
                          markersize=15, label='Promedio')
    red = mlines.Line2D([], [], color='orange', 
                          markersize=15, label='Peor')
    yel = mlines.Line2D([], [], color='green', 
                          markersize=15, label='Mejor')
    ax.legend(handles=[yel,blue_line,red])

def tabla():
        # for todos in listaPoblacion.values():
        #     print(todos.toString())
        #     print('______________________________________')

        figure2 = plt.figure(figsize=(15,10))
        ax2 = plt.subplot(1,1,1)
        data = []
        auxList = []
        resta = tam_pob_max - 4 
        contador_impresion = 0 
        for individuo in listaPoblacion.values():
            contador_impresion = contador_impresion + 1
            if contador_impresion >=resta:
                auxList.append(individuo.genotipo_X)
                auxList.append(individuo.genotipo_Y)
                auxList.append(individuo.i_X)
                auxList.append(individuo.i_Y)
                auxList.append(individuo.fenotipo_X)
                auxList.append(individuo.fenotipo_Y)
                auxList.append(individuo.aptitud)
                data.append(auxList)
                auxList = []

        print(data)
        colum_labeles = ['Genotipo X','Genotipo Y','iX','iY','Fenotipo X','Fenotipo Y','Aptitud']
        ax2.axis('tight')
        ax2.axis('off')
        tabla = ax2.table(cellText=data,colLabels=colum_labeles,loc="center")
        tabla.set_fontsize(30)      
 
crear_poblacion(bits_X=bitsX,bits_Y=bitsY,posicionX=x[0],posicionY=y[0],deltaX=resolucion_deltaX,deltaY=resolucion_deltaY,contador_gen=contador_generaciones)
grafica()
tabla()
plt.show()




 

