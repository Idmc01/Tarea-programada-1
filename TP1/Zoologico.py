#Elaborado por: Erick Alvarado, Ian Murillo y Nima Samadian
#Fecha de Elaboración 6/11/2020
#Fecha de última modificación:9/11/2020
#Versión de Python 3.8.1
#Importación de librerias
from TareaProgramada1 import*
def nombreZoo():
    """
    Funcionalidad:Pedir nombre de zoológico
    Entradas:Nombre de zoológico
    Salidas:Nombre de zoológico
    """
    print("Crear nombre de zoológico")
    nombre=input("Introduzzca el nombre de su zoológico: ")
    print(nombre)
    return menu(nombre)
def opcion1(nuevaCarpeta,nombre):
    """
    Funcionalidad:Llamar a agergarAnimales
    Entradas:
    Salidas:
    """
    print("Agregar animales")
    nuevaCarpeta=agregarAnimales(nuevaCarpeta)
    return menuAux(nuevaCarpeta,nombre)
def opcion2(nuevaCarpeta,nombre):
    """
    Funcionalidad:Llamar a obtenerInformacion
    Entradas:
    Salidas:
    """
    print("Obtener información de un animal")
    obtenerInformacion(nuevaCarpeta)
    return menuAux(nuevaCarpeta,nombre)
def opcion3(nuevaCarpeta,nombre):
    """
    Funcionalidad:Llamar a anotaciones
    Entradas:
    Salidas:
    """
    print("Registrar anotaciones")
    anotaciones(nuevaCarpeta,nombre)
    return menuAux(nuevaCarpeta,nombre)
def opcion4(nuevaCarpeta,nombre):
    """
    Funcionalidad:Llamar a apartarAnimales
    Entradas:
    Salidas:
    """
    print("Apartar animales de mi zoológico")
    apartarAnimales(nuevaCarpeta)
    return menuAux(nuevaCarpeta,nombre)
def opcion5(nuevaCarpeta,nombre):
    """
    Funcionalidad:Llamar a salvaguardando
    Entradas:
    Salidas:
    """
    print("Salvaguardando estable mi zoológico")
    salvaguardando(nuevaCarpeta,nombre)
    return menuAux(nuevaCarpeta,nombre)
def opcion6(nuevaCarpeta,nombre):
    """
    Funcionalidad:Llamar a exportandoBD
    Entradas:
    Salidas:
    """
    print("Exportando la base de datos ")
    exportandoBD()
    return menuAux(nuevaCarpeta,nombre)
def opcion7():
    """
    Funcionalidad:Llamar a salir
    Entradas:
    Salidas:
    """
    print("Salir del sistema de Información")
    salir()
    return ""
def menu(nombre):
    """
    Funcionalidad:Mostrar menu al usuario
    Entradas:Opcion del menu
    Salidas:Funcione elegida
    """
    nuevaCarpeta=""
    print("""
*---------------------------------------------------------*
|    1. Agregar animales                                  |
|    2. Obtener información de un animal                  |
|    3. Registrar anotaciones                             |
|    4. Apartar animales de mi zoológico                  |
|    5. Salvaguardando estable mi zoológico               |
|    6. Exportando la base de datos                       |
|    7. Salir del sistema de Información                  |
*---------------------------------------------------------*
""")
    try:
            opcion = int(input("inserte una opcion: "))
            if opcion >=1 and opcion<=7:
                if opcion == 1:
                    opcion1(nuevaCarpeta,nombre)
                elif opcion == 2:
                    opcion2(nuevaCarpeta,nombre)
                elif opcion == 3:
                    opcion3(nuevaCarpeta,nombre)
                elif opcion == 4:
                    opcion4(nuevaCarpeta,nombre)
                elif opcion == 5:
                    opcion5(nuevaCarpeta,nombre)
                elif opcion == 6:
                    opcion6(nuevaCarpeta,nombre)
                elif opcion == 7:
                    opcion7()
            else:
                print("ingrese una opción válida")
                return menuAux(nuevaCarpeta,nombre)
    except:
        print("Ingrese una opción valida")
        return menuAux(nuevaCarpeta,nombre)
def menuAux(nuevaCarpeta,nombre):
    """
    Funcionalidad:Mostrar menu al usuario
    Entradas:Opcion del menu
    Salidas:Funcione elegida
    """
    print("""
*---------------------------------------------------------*
|    1. Agregar animales                                  |
|    2. Obtener información de un animal                  |
|    3. Registrar anotaciones                             |
|    4. Apartar animales de mi zoológico                  |
|    5. Salvaguardando estable mi zoológico               |
|    6. Exportando la base de datos                       |
|    7. Salir del sistema de Información                  |
*---------------------------------------------------------*
""")
    try:
            opcion = int(input("inserte una opcion: "))
            if opcion >=1 and opcion<=7:
                if opcion == 1:
                    opcion1(nuevaCarpeta,nombre)
                elif opcion == 2:
                    opcion2(nuevaCarpeta,nombre)
                elif opcion == 3:
                    opcion3(nuevaCarpeta,nombre)
                elif opcion == 4:
                    opcion4(nuevaCarpeta,nombre)
                elif opcion == 5:
                    opcion5(nuevaCarpeta,nombre)
                elif opcion == 6:
                    opcion6(nuevaCarpeta,nombre)
                elif opcion == 7:
                    opcion7()
            else:
                print("ingrese una opción válida")
                return menuAux(nuevaCarpeta,nombre)
    except:
        print("Ingrese una opción valida")
        return menuAux(nuevaCarpeta,nombre)
nombreZoo()
