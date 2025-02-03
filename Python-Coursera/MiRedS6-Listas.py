#En el archivo de cada usuario, luego de escribir su estado actual, agregaremos una lista de los mensajes
#que han sido publicados por sus amigos, de manera de formar una lista de mensajes que llamaremos "muro", o 'timeline',
#presente en casi todas las redes sociales.

#En este módulo están todos las funciones que hemos creado hasta ahora
import S6Red as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya había un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)
else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacíamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

# Función para agregar un nuevo amigo
def agregar_amigo():
    nuevo_amigo = input("Ingresa el nombre de tu nuevo amigo o amiga: ")
    amigos.append(nuevo_amigo)
    print(f"{nuevo_amigo} ha sido agregado a tu lista de amigos.")

# Función para mostrar los últimos estados de los amigos
def mostrar_estados_amigos():
    for amigo in amigos:
        if Red.existe_archivo(amigo + ".user"):
            with open(amigo + ".user", "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                estado_amigo = lineas[7].strip()  # Asumiendo que el estado está en la línea 8 (índice 7)
                print(f"Estado de {amigo}: {estado_amigo}")
        else:
            print(f"No se encontró el archivo de {amigo}")

# Menú de opciones
opcion = -1
while opcion != 0:
    print("\nOpciones:")
    print("1. Actualizar estado")
    print("2. Agregar un nuevo amigo")
    print("3. Mostrar los últimos estados de los amigos")
    print("0. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)
    elif opcion == 2:
        agregar_amigo()
    elif opcion == 3:
        mostrar_estados_amigos()
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en", nombre+".user")
        archivo_usuario = open(nombre+".user", "w")
        archivo_usuario.write(nombre + "\n")
        archivo_usuario.write(str(edad) + "\n")
        archivo_usuario.write(str(estatura_m + estatura_cm / 100) + "\n")
        archivo_usuario.write(sexo + "\n")
        archivo_usuario.write(pais + "\n")
        archivo_usuario.write(str(len(amigos)) + "\n")
        for amigo in amigos:
            archivo_usuario.write(amigo + "\n")
        archivo_usuario.write(estado + "\n")
        archivo_usuario.write("\n".join(muro) + "\n")
        archivo_usuario.close()
        print("Archivo", nombre+".user", "guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")

