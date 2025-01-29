#Esta versiÃ³n utiliza archivos para almacenar y leer los datos de cada usuario de nuestra red social.

#AdemÃ¡s encapsula el proceso de lectura y escritura de archivos en el mÃ³dulo Red, de manera de hacer
#que el cÃ³digo sea mÃ¡s fÃ¡cil de comprender.

#Recordemos que en este mÃ³dulo estÃ¡n todos las funciones adicionales que hemos creado.
import S5Red2 as Red

Red.mostrar_bienvenida()
nombre = input("Para empezar, dime como te llamas. ")
if Red.existe_usuario(nombre):
    nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado = Red.cargar_usuario(nombre)
else:
    print("No encontramos un usuario con ese nombre, por favor ingresa tus datos.")
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

# En ambos casos, al llegar aquí ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

# Ahora podemos mostrar el menú y consultar las opciones
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

    elif opcion == 5:
        nuevo_nombre = input("Ingresa el nuevo nombre de usuario: ")
        if Red.existe_usuario(nuevo_nombre):
            nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado = Red.cargar_usuario(nuevo_nombre)
            print("Usuario cambiado exitosamente.")
        else:
            print("No se puede cambiar a ese usuario. El archivo no existe.")

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre + ".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
        print("Archivo", nombre + ".user", "guardado")
        break

print("Gracias por usar Mi Red. ¡Hasta pronto!")

# Te proponemos que completes el siguiente ejercicio:
# 1. Ingresa al programa de red social con distintos usuarios. Luego de eso tendrás varios archivos con extensión
#    '.user'. Abre cualquiera de ellos con un editor de texto y edita algún valor.
#    A continuación inicia tu programa y entra con el nombre de uno de usuarios. ¿Se actualizan los datos?
#
# 2. Agrega una nueva opción que se llame "Cambiar de usuario". Con esta opción el programa, sin salirse
#    de la red, el programa solicita un nuevo nombre y, en caso que exista un archivo con el nombre
#    de ese usuario, se cargan sus datos. Si el archivo no existe, basta con indicar que no se puede
#    cambiar a ese usuario.