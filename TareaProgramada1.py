#Elaborado por: Erick Alvarado, Ian Murillo y Nima Samadian
#Fecha de Elaboración 2/11/2020
#Fecha de última modificación:
#Versión de Python 3.8.1
#Importación de librerias
import re
import pickle
import random
import os
#Definición de funciones:
#Programa principal
def agregarAnimales():
    lista1 = []
    conf=0
    try:
        c=open("AP.txt","r")
        for linea in c.readlines():
            lista1+= [linea]
        c.close
        print("Desea cargar datos de un archivo binario previo")
        conf=int(input("1.Si\n2.No\n"))
        if conf==1:
            ubicacion=input("Indique el nombre del archivo: ")
            #Terminar
            #ubicacion = "AP.txt"
            initial_dir = 'C:\\'

            path = ''
            for root, _, files in os.walk(initial_dir):
                if ubicacion in files:
                   path = os.path.join(root, ubicacion)
                   break
            #lista = []
            f = open (ubicacion,"r")
            lista = f.readlines()
            f.close()
            print(path)
            print (lista)
            return ""
        elif conf==2:
            pass
        else:
            print("Opción no valida")
            return agregarAnimales()
    except:
        pass
    lista1 = []
    lista2 = []
    try:
        cantidadA = int(input("Ingrese la cantidad de animales que desea en su zoologico: "))
    except:
        print("Cantidad no válida")
        return agregarAnimales()
    a = open("EjemploDeArchivoTP1.txt",encoding="utf8")
    for linea in a.readlines():
        lista1+= [linea]
    a.close
    x=lista1.pop()
    x+="\n"
    lista1+= [x]
    if cantidadA>len(lista1) or cantidadA<0:
        print("Cantidad no válida")
        return agregarAnimales()
    while cantidadA>0:
        animal=random.choice(lista1)
        if animal in lista2:
            pass
        else:
            lista2.append(animal)
            cantidadA-=1
    print(lista1)
    print(lista2)
    b = open("AP.txt","w")
    for dato in lista2:
        b.write(dato)
    b.close
    return ""
def apartarAnimales():
    lista1 = []
    lista2 = []
    try:
        cantidadA = int(input("Ingrese la cantidad de animales que puede conservar en su zoologico: "))
    except:
        print("Cantidad no válida")
        return apartarAnimales()
    a = open("AP.txt","r")
    for linea in a.readlines():
        lista1+= [linea]
    a.close
    #l = len(lista1)
    #n = l-cantidadA
    while cantidadA>0:
        animal=random.choice(lista1)
        if animal in lista2:
            pass
        else:
            lista2.append(animal)
            cantidadA-=1
    print(lista1)
    print(lista2)
    b = open("AP.txt","w")
    for dato in lista2:
        b.write(dato)
    b.close
    return ""

#agregarAnimales()    
#apartarAnimales()
