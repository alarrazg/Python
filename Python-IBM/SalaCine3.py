class Butaca:
    """
    Representa un Butaca en una sala de cine.

    Atributos:
        - numero (int): Número del Butaca.
        - fila (str): Fila del Butaca (ej: 'A', 'B').
        - reservado (bool): Indica si el Butaca está reservado.
        - precio_base (float): Precio base del Butaca.
    """

    def __init__(self, numero, fila):
        # Inicializa los atributos del Butaca con los valores proporcionados
        self.numero = numero
        self.fila = fila
        self.reservado = False
        self.precio_base = 10

class SalaCine:
    """
    Administra una lista de Butacas y las operaciones sobre ellos.

    Atributos:
        - Butacas (list): Lista de objetos Butaca que representan los Butacas de la sala.
    """

    def __init__(self):
        # Inicializa la lista de Butacas vacía
        self.Butacas = []

    def agregar_Butaca(self, Butaca):
        """
        Agrega un Butaca a la sala.

        Args:
            Butaca (Butaca): Objeto Butaca a agregar.

        Raises:
            ValueError: Si el Butaca ya existe en la sala.
        """
        # Verifica si el Butaca ya está en la lista de Butacas
        if Butaca not in self.Butacas:
            # Si no está, lo agrega a la lista
            self.Butacas.append(Butaca)
        else:
            # Si ya está, lanza un error
            raise ValueError("El Butaca ya existe")
        
    def mostrar_Butacas(self):
        """
        Muestra todos los Butacas y su estado en orden por filas.
        """
        # Obtiene una lista de filas únicas y las ordena
        filas = sorted(set(Butaca.fila for Butaca in self.Butacas))
        # Itera sobre cada fila
        for fila in filas:
            # Filtra los Butacas que pertenecen a la fila actual y los ordena por número
            Butacas_fila = sorted([Butaca for Butaca in self.Butacas if Butaca.fila == fila], key=lambda x: x.numero)
            # Imprime los detalles de cada Butaca en la fila actual
            for Butaca in Butacas_fila:
                print(f"Butaca {Butaca.numero}, Fila {Butaca.fila}, Reservado: {Butaca.reservado}")

    def reservar_Butacas_juntos(self, edades, dia):
        """
        Reserva Butacas juntos y calcula el precio final.

        Args:
            edades (list): Lista de edades de los asistentes.
            dia (str): Día de la semana.

        Raises:
            ValueError: Si no hay suficientes Butacas disponibles juntos.
        """
        # Cantidad de Butacas a reservar
        cantidad = len(edades)
        # Itera sobre cada fila en orden alfabético
        for fila in range(ord('A'), ord('Z') + 1):
            # Filtra los Butacas disponibles en la fila actual
            Butacas_disponibles = [Butaca for Butaca in self.Butacas if Butaca.fila == chr(fila) and not Butaca.reservado]
            # Verifica si hay suficientes Butacas disponibles juntos en la fila actual
            if len(Butacas_disponibles) >= cantidad:
                # Reserva los Butacas necesarios
                for i in range(cantidad):
                    Butaca = Butacas_disponibles[i]
                    # Calcula el precio del Butaca con los descuentos aplicables
                    precio = self._calcular_precio(Butaca, edades[i], dia)
                    Butaca.reservado = True
                    print(f"Butaca {Butaca.numero}, Fila {Butaca.fila} reservado. Precio: ${precio:.2f}")
                return
        # Si no hay suficientes Butacas disponibles juntos, lanza un error
        raise ValueError("No hay suficientes Butacas disponibles juntos")

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un Butaca.

        Args:
            numero (int): Número del Butaca.
            fila (str): Fila del Butaca.

        Raises:
            ValueError: Si el Butaca no existe o no está reservado.
        """
        # Busca el Butaca por número y fila
        Butaca = self._buscar_Butaca(numero, fila)
        # Verifica si el Butaca existe y está reservado
        if Butaca and Butaca.reservado:
            # Cancela la reserva del Butaca
            Butaca.reservado = False
            print("Reserva cancelada.")
        else:
            # Si el Butaca no existe o no está reservado, lanza un error
            raise ValueError("No se puede cancelar la reserva.")

    def _buscar_Butaca(self, numero, fila):
        """
        Busca un Butaca por número y fila en la lista de Butacas.

        Args:
            numero (int): Número del Butaca.
            fila (str): Fila del Butaca.

        Returns:
            Butaca: El objeto Butaca si se encuentra, None en caso contrario.
        """
        # Itera sobre la lista de Butacas
        for Butaca in self.Butacas:
            # Verifica si el Butaca coincide con el número y la fila proporcionados
            if Butaca.numero == numero and Butaca.fila == fila:
                return Butaca
        # Si no se encuentra el Butaca, devuelve None
        return None

    def _calcular_precio(self, Butaca, edad, dia):
        """
        Calcula el precio final de un Butaca aplicando descuentos.

        Args:
            Butaca (Butaca): Objeto Butaca.
            edad (int): Edad del espectador.
            dia (str): Día de la semana.

        Returns:
            float: Precio final del Butaca.
        """
        # Precio base del Butaca
        precio = Butaca.precio_base
        # Aplica un descuento del 20% si la edad es menor de 18 años
        if edad < 18:
            precio *= 0.8
        # Aplica un descuento del 10% si el día es miércoles
        if dia.lower() == "miércoles":
            precio *= 0.9
        return precio

def main():
    # Crea una instancia de SalaCine
    sala = SalaCine()
    # Agrega Butacas a la sala (10 Butacas por cada fila de la A a la Z)
    for numero in range(1, 11):
        for fila in range(ord('A'), ord('Z') + 1):
            sala.agregar_Butaca(Butaca(numero, chr(fila)))

    # Solicita al usuario el número de asistentes
    numero_asistentes = int(input("Ingrese el número de asistentes: "))
    edades = []
    # Solicita la edad de cada asistente
    for i in range(numero_asistentes):
        edad = int(input(f"Ingrese la edad del asistente {i + 1}: "))
        edades.append(edad)
    # Solicita el día de la semana
    dia = input("Ingrese el día de la semana: ")

    # Reserva los Butacas juntos para los asistentes
    sala.reservar_Butacas_juntos(edades, dia)

    # Muestra el estado de todos los Butacas
    # sala.mostrar_Butacas()

if __name__ == '__main__':
    main()