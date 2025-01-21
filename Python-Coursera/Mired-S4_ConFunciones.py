def calcular_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    return estatura_m, estatura_cm

def solicitar_cantidad_amigos():
    while True:
        try:
            return int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos):
    print()
    print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")
    print()

def solicitar_datos_perfil():
    nombre = input("Para empezar, dime cómo te llamas. ")
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = 2017 - agno - 1
    print()
    estatura_m, estatura_cm = calcular_estatura()
    num_amigos = solicitar_cantidad_amigos()
    return nombre, edad, estatura_m, estatura_cm, num_amigos

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de datos del perfil
nombre, edad, estatura_m, estatura_cm, num_amigos = solicitar_datos_perfil()
mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

# Esta opción permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    # Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    # Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@" + nombre_amigo, mensaje)
            print("--------------------------------------------------")

    # Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

    # Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        nombre, edad, estatura_m, estatura_cm, num_amigos = solicitar_datos_perfil()
        mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos)

    # Código para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    # Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print()