#Elaborado por: Erick Alvarado, Ian Murillo y Nima Samadian
#Fecha de Elaboración 2/11/2020
#Fecha de última modificación:
#Versión de Python 3.8.1
#Importación de librerias
import re
import pickle
import random
import os
import wikipedia as wiki
import xml.etree.ElementTree as ET
#Definición de funciones:
#Programa principal
def agregarAnimales():
    """
    Funcionalidad:Agregar animales al archivo
    Entradas:Cantidad de animales que se quiere en el zoológico
    Salidas:La lista de todos los animales del zoológico
    """
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
    print(lista2)
    b = open("AP.txt","w")
    for dato in lista2:
        b.write(dato)
    b.close
    return ""
def obtenerInformacion():
    """
    Funcionalidad:Obtener la información del animal elegido
    Entradas:Nombre del animal que se quiere buscar
    Salidas:Título,nombre,url de wikipedia,resumen e imagen del animal
    """
    lista1=[]
    c=open("AP.txt","r")
    for linea in c.readlines():
        lista1+= [linea]
    c.close
    p=1
    for animal in lista1:
        print (p,"-",animal)
        p+=1
    op=int(input("Seleccione el animal a buscar: "))
    l=len(lista1)
    if op<=l and op>0:
        wiki.set_lang("es")
        anima=lista1[op-1]
        inf=wiki.page(anima)
        titulo=inf.title
        url=inf.url
        info=wiki.summary(anima)
        info=re.sub('\[\d+\]', '', info)
        ima=inf.images
        lista2=[]
        for link in ima:
            la=len(link)
            if link[la-3]=="j" or link[la-3]=="J":
                lista2.append(link)
        print(anima,titulo,"\n",url,"\n",info,"\n",lista2[0])
    return ""

def apartarAnimales():
    """
    Funcionalidad:Modificar la cantidad de animales del zoológico segun indique el usuario
    Entrada:Cantidad nueva de animales
    Salida:Lista de animales según cantidad específicada
    """
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
    while cantidadA>0:
        animal=random.choice(lista1)
        if animal in lista2:
            pass
        else:
            lista2.append(animal)
            cantidadA-=1
    print(lista2)
    b = open("AP.txt","w")
    for dato in lista2:
        b.write(dato)
    b.close
    return ""
def anotaciones():
    """
    Funcionalidad:Insertar y guardar anotaciones para un animal
    Entrada:El animal al que se le quieren hacer las anotaciones
    Salida:Anotaciones del animal
    """
    lista1=[]
    lista2=[]
    c=open("AP.txt","r")
    for linea in c.readlines():
        lista1+= [linea]
    c.close
    p=1
    for animal in lista1:
        print (p,"-",animal)
        p+=1
    op=int(input("Seleccione el animal a buscar: "))
    l=len(lista1)
    if op<=l and op>0:
        anima=lista1[op-1]
        at=input("Anotaciones: ")
        try:
            b=open("Anotaciones","rb")
            lista2=pickle.load(b)
            b.close
            for lista in lista2:
                if lista[0]==anima:
                    lista.append(at)
                    a=open("Anotaciones","wb")
                    pickle.dump(lista2,a)
                    a.close
                    for objeto in lista2:
                        print("")
                        for dato in objeto:
                            print(dato)
                    return ""
        except:
            pass
        lista2+=[[anima,at]]
        a=open("Anotaciones","wb")
        pickle.dump(lista2,a)
        a.close
        print("")
        for objeto in lista2:
            print("")
            for dato in objeto:
                print(dato)
    return ""
def salvaguardando():
    """
    Funcionalidad:Agerga el animal a la matriz con todos sus datos menos la imagen
    Entrada:
    Salida:
    """
    lista1=[]
    lista2=[]
    a=open("Anotaciones","rb")
    anotaciones=pickle.load(a)
    a.close
    b=open("AP.txt","r")
    for linea in b.readlines():
        lista1+= [linea]
    b.close
    print("Buscando información...")
    for anima in lista1:
        wiki.set_lang("es")
        inf=wiki.page(anima)
        titulo=inf.title
        url=inf.url
        info=wiki.summary(anima)
        info=re.sub('\[\d+\]', '', info)
        lista2+=[[anima,titulo,url,info]]
    print("Información guardada")
    for anima in lista2:
        for dato in anotaciones:
            if dato[0]==anima[0]:
                l=len(dato)
                p=1
                while p<l:
                    anima.append(dato[p])
                    p+=1
    c=open("Salvaguardado","wb")
    pickle.dump(lista2,c)
    c.close
    for anima in lista2:
        for dato in anima:
            print(dato)
        print("")
    return ""
def exportandoBD():
    """
    Funcionalidad:Genera un archivo de tipo .xml que almacene la lista completa de animales 
    Entrada:
    Salida:
    """
    a=open("Salvaguardado","rb")
    lista=pickle.load(a)
    a.close
    p=4
    root = ET.Element("Zoo")
    for anima in lista:
        l=len(anima)
        doc = ET.SubElement(root, "Datos")
        ET.SubElement(doc, "Nombre", Animal=anima[0]).text = anima[1]
        ET.SubElement(doc, "Informacion", Animal=anima[2]).text = anima[3]
        while p<l:
            ET.SubElement(doc, "Anotaciones", Animal=anima[p]).text = ""
            p+=1
        p=4
    tree = ET.ElementTree(root)
    na=input("Ingrese el nombre con el que desea guardar el archivo: ")
    tree.write(na+".xml")
    return ""
def salir():
    """
    Funcionalidad:Salir del programa 
    Entrada:
    Salida:Frase
    """
    print("Los animales nacen como son, lo aceptan y eso es todo. Viven con mayor paz que las personas")
    return ""
#agregarAnimales()
#obtenerInformacion()
#apartarAnimales()
#anotaciones()
#salvaguardando()
#exportandoBD()
#salir()
