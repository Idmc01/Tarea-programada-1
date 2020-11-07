import names
import random
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
    return reactivarAudio(lista)
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
def renombrar():
    es=input("Introduzca nombre del estudiante: ")
    ap=input("Introduzca primer apellido del estudiante: ")
    ap2=input("Introduzca segundo apellido del estudiante: ")
pedirDatos()
