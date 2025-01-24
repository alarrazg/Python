#Hola.
#Hasta ahora nuestra red social incluye estas caracterÃ­sticas:

#El programa de la semana anterior permitÃ­a:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#4. Modificar el perfil del usuario
#
#Y ademÃ¡s algunas de estas funcionalidades estÃ¡n encapsulados en un mÃ³dulo, de manera
#que tu cÃ³digo principal es cada vez mÃ¡s corto y puedes concentrarte en la funcionalidad principal.

#Vamos por la siguiente evoluciÃ³n de nuestra red social.

#HabrÃ¡s notado que cada vez que ejecutamos nuestro programa de red social, debemos ingresar
#todos los datos del usuario que estÃ¡ utilizando el programa, antes de poder alcanzar
#el menÃº de opciones. Esto es bastante engorroso.

#Sin embargo, ahora sabemos que podemos utilizar memoria secundaria de nuestro computador,
#esto es, espacio del disco, para guardar archivos. Vamos a usar esto para que nuestro
#programa pueda recordar los datos de los usuarios, y evitar tener que escribirlos en cada ocasiÃ³n.

#Y la estrategia que usaremos es la siguiente.
#Cada vez que un usuario nuevo utilice nuestro programa, vamos a guardar un archivo con sus datos.
#El nombre de este archivo serÃ¡ el nombre del usuario, seguido de la extensiÃ³n '.user'.
#En este archivo guardaremos una lÃ­nea por cada variable importante de nuestro usuario.

#De esta manera, la prÃ³xima vez que ejecutemos nuestro programa, lo primero que haremos serÃ¡ preguntar
#el nombre del usuario, y ver si existe un archivo con ese nombre.
#Si existe, entonces lo leemos desde el disco, y evitamos tener que preguntar todos sus datos.
#Si no existe, entonces seguimos comportÃ¡ndonos como antes, lo tratamos como un usuario nuevo, y preguntamos
#sus datos para luego crear un archivo.


#Recordemos que en este mÃ³dulo estÃ¡n todos las funciones adicionales que hemos creado.
import S5Red as Red
#El mÃ³dulo 'os' nos permitirÃ¡ consultar si un archivo existe.
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if os.path.isfile(nombre+".user"):
    #Esto lo hacemos si ya habÃ­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline()
    pais = archivo_usuario.readline()
    num_amigos = int(archivo_usuario.readline())
    estado = archivo_usuario.readline()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)
    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        archivo_usuario = open(nombre+".user","w")
        archivo_usuario.write(nombre+"\n")
        archivo_usuario.write(str(edad)+"\n")
        archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
        archivo_usuario.write(sexo+"\n")
        archivo_usuario.write(pais+"\n")
        archivo_usuario.write(str(num_amigos)+"\n")
        archivo_usuario.write(estado+"\n")
        #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
        archivo_usuario.close()
        print("Archivo",nombre+".user","guardado")



print("Gracias por usar Mi Red. Â¡Hasta pronto!")

#Cuando ejecutes este programa por primera vez, verÃ¡s que se crea un archivo nuevo en tu computador
#cada vez que ingresas con el nombre de un usuario nuevo. Prueba a ingresar
#con un nombre de usuario que ya habÃ­as usado antes.

#Este programa es bastante mÃ¡s completo que los que tenÃ­amos antes, sin embargo aÃºn tiene cosas
#por mejorar. Por ejemplo, Â¿quÃ© ocurre si el archivo estÃ¡ mal escrito, o si le falta alguna lÃ­nea?
#Â¿QuÃ© ocurre si en una ocasiÃ³n ingreso mi nombre con mayÃºsculas, y en otra ocasiÃ³n lo hago con minÃºsculas?
#
#Te invitamos a corregir dos detalles en este programa
#1. Al leer las lÃ­neas del archivo, siempre se leen como Ãºltimos caracteres, algunos caracteres blancos como
#   espacios y el caracter de cambio de lÃ­nea ('\n'). Esto hace que los nombres de archivos creados incluyan
#   estos caracteres adicionales. Puedes utilizar los mÃ©todos de str para eliminar este tipo de caracteres
#   que llamamos "no imprimibles"
#2. Utiliza tu conocimiento de funciones para crear funciones que lean desde un archivo,
#   y retornen el conjunto de datos leÃ­dos, de manera de encapsular el proceso de lectura y escritura,
#   y reducir el tamaÃ±o de tu cÃ³digo.0
