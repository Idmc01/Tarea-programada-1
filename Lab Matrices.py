import names
import random
import re
import time
def pedirDatos():
    cp=int(input("Cantidad de participantes en la reunión: "))
    if cp>100 or cp<0:
        print("Cantida no válida")
        return Zoom()
    cf=int(input("Cantidad de filas de la reunión: "))
    if cf>5 or cf<0:
        print("Cantida no válida")
        return Zoom()
    cpan=int(input("Cantidad de pantallas de la reunión: "))
    if cpan>4 or cpan<0:
        print("Cantida no válida")
        return Zoom()
    print("a) Cantidad de participantes en la reunión:",cp,"\n",
          "b) Cantidad de filas de la reunión:",cf,"\n",
          "c) Cantidad de pantallas de la reunión:",cpan)
    return crearLista(cp,cf,cpan)
def crearLista(cp,cf,cpan):
    lista=[]
    cfc=cf
    x=0
    while cpan!=0:
        lista+=[[]]
        cpan-=1
    while cp!=0:
        for pantalla in lista:
            while cf!=0:
                lista[x]+=[[]]
                cf-=1
            cf=cfc
            x+=1
            cp-=(cf*5)
        x=0
        p=0
        e=5
        for pantalla in lista:
            for fila in lista[x]:
                while e!=0:
                    n=names.get_first_name()
                    a1=names.get_last_name()
                    a2=names.get_last_name()
                    lista[x][p]+=[[n,a1,a2]]
                    e-=1
                p+=1
                e=5
            x+=1
            p=0
    x=0
    for pantalla in lista:
        for fila in lista[x]:
            print(fila)
        print("")
        x+=1
    return brindarDatos(lista)
def brindarDatos(lista):
    audio=[True, False]
    presencia=[1,2,3]
    reacciones=["sn","ap","lv"]
    for pantalla in lista:
        for fila in pantalla:
            for estudiante in fila:
                estudiante.append(random.choice(audio))
                estudiante.append(random.choice(presencia))
                estudiante.append(random.choice(reacciones))
                print(estudiante)
    return salir()
def reactivarAudio(lista):
    es=input("Introduzca nombre del estudiante: ")
    ap=input("Introduzca apellido del estudiante: ")
    p=1
    f=1
    c=1
    for pantalla in lista:
        for fila in pantalla:
            for estudiante in fila:
                if estudiante[0]==es and estudiante[1]==ap:
                    if estudiante[3]==True:
                        print("No se puede activar el audio porque ya está activo")
                    else:
                        estudiante[3]=True
                        print("Página:",p,"Fila:",f,"Columna:",c)
                        print("Su audio está siendo activado")
                    print(estudiante[3])
                c+=1
            f+=1
            c=1
        p+=1
        f=1
    return ""
def renombrar(lista):
    es=input("Introduzca nombre del estudiante: ")
    ap=input("Introduzca primer apellido del estudiante: ")
    ap2=input("Introduzca segundo apellido del estudiante: ")
    p=1
    f=1
    c=1
    for pantalla in lista:
        for fila in pantalla:
            for estudiante in fila:
                if estudiante[0]==es and estudiante[1]==ap and estudiante[2]==ap2:
                    nn = input("Ingrese el nuevo nombre: ")
                    na = input("Ingrese el nuevo primer apellido: ")
                    na2 = input("Ingrese el nuevo segundo apellido: ")
                    estudiante[0] = nn
                    estudiante[1] = na
                    estudiante[2] = na2
                    print("Nombre cambiado exitosamente")
                    print ("Página:",p,"Fila:",f,"Columna:",c)
                    print(estudiante)
                    return ""
                c+=1
            f+=1
            c=1
        p+=1
        f=1
    print ("Nombre no encontrado")
    return renombrar(lista)
def mostrarTodo(lista):
    p=1
    f=1
    c=1
    for pantalla in lista:
        for fila in pantalla:
            for estudiante in fila:
                au=estudiante[3]
                tp=estudiante[4]
                if au==True:
                    au="Activo"
                else:
                    au="Inactivo"
                if tp==1:
                    tp="Foto Visible"
                elif tp==2:
                    tp="Foto no Visible"
                else:
                    tp="Video Activo"
                print("Página:",p,"Fila:",f,"Columna:",c,
                      "Nombre:",estudiante[0],estudiante[1],estudiante[2],
                      "Audio:",au,"Tipo de presencia:",tp)
                c+=1
            f+=1
            c=1
        p+=1
        f=1
    return ""
def participantesVideo(lista):
    p=1
    f=1
    c=1
    for pantalla in lista:
        for fila in pantalla:
            for estudiante in fila:
                if estudiante[4]==3:
                    print("Página:",p,"Fila:",f,"Columna:",c,
                      "Nombre:",estudiante[0],estudiante[1],estudiante[2])
                c+=1
            f+=1
            c=1
        p+=1
        f=1
    return ""
def buscarParticipantes(lista):
    ec=input("Introduzca nombre a buscar: ")
    Ec=ec.capitalize()
    p=1
    f=1
    c=1
    for pantalla in lista:
        for fila in pantalla:
            for estudiante in fila:
                if re.search(ec,estudiante[0])!=None or re.search(ec,estudiante[1])!=None or re.search(ec,estudiante[2])!=None or re.search(Ec,estudiante[0])!=None or re.search(Ec,estudiante[1])!=None or re.search(Ec,estudiante[2])!=None:
                    print("Página:",p,"Fila:",f,"Columna:",c,
                      "Nombre:",estudiante[0],estudiante[1],estudiante[2])
                c+=1
            f+=1
            c=1
        p+=1
        f=1
    return ""
def salir():
    t=5
    print("El anfitrión ha eliminado su participación de esta reunión. Saliendo en")
    while t!=0:
        print(t)
        t-=1
        time.sleep(5)
    return ""
pedirDatos()
