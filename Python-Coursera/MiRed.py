
# -*- coding: utf-8 -*-
#Hola, ahora que ya sabemos construir una interacciÃ³n bÃ¡sica con nuestro programa
#de red social, vamos a agregar nuevas funcionalidades.
#
#Vamos a partir con el mismo programa de la etapa anterior, que permite dos cosas:
#1. Obtener datos del usuario
#2. Consultar y mostrar UN mensaje de estado del usuario
#
#Una caracterÃ­stica de los programas con mÃºltiples funcionalidades es que ofrecen un menÃº de acciones
#al usuario. Los menÃº de opciones permiten que el usuario escoja que acciÃ³n realizar y podemos
#implementarlos usando un ciclo while que funcionen mientras el usuario no escoja una acciÃ³n de salida.
#Cada vez que el usuario escoja una acciÃ³n podemos usar una serie de 'if/elif/else' para ejecutar
#distintas secciones de cÃ³digo de acuerdo a lo que el usuario ha solicitado.

#Para empezar vamos a permitir que el usuario publique todos los mensajes que considere desee hasta
#que decida salir voluntariamente del programa.

############################################################
# Bienvenida

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

# CÃ¡lculo de edad
agno = int(input("Para preparar tu perfil, dime en que aÃ±o naciste. "))
edad = 2017-agno-1
print()

# CÃ¡lculo de estatura
estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "aÃ±os")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informaciÃ³n. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    #Solicitamos opciÃ³n al usuario
    escribir_mensaje = str(input("Â¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
    
    continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. Â¡Hasta pronto!")

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acciÃ³n de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mÃ¡s acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafÃ­os:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opciÃ³n al usuario.
#
#2. Modifica este menÃº para que le permita el usuario realizar mÃ¡s de una acciÃ³n.
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.a
