class Asiento:
    """
    Representa un asiento en una sala de cine.

    Atributos:
        - numero (int): Número del asiento.
        - fila (str): Fila del asiento (ej: 'A', 'B').
        - reservado (bool): Indica si el asiento está reservado.
        - precio_base (float): Precio base del asiento.
    """

    def __init__(self, numero, fila):
        self.numero = numero
        self.fila = fila
        self.reservado = False
        self.precio_base = 10

class SalaCine:
    """
    Administra una lista de asientos y las operaciones sobre ellos.

    Atributos:
        - asientos (list): Lista de objetos Asiento que representan los asientos de la sala.
    """

    def __init__(self):
        self.asientos = []

    def agregar_asiento(self, asiento):
        """
        Agrega un asiento a la sala.

        Args:
            asiento (Asiento): Objeto Asiento a agregar.

        Raises:
            ValueError: Si el asiento ya existe en la sala.
        """
        if asiento not in self.asientos:
            self.asientos.append(asiento)
        else:
            raise ValueError("El asiento ya existe")
        
    def mostrar_asientos(self):
        """
        Muestra todos los asientos y su estado.
        """
        for asiento in self.asientos:
            print(f"Asiento {asiento.numero}, Fila {asiento.fila}, Reservado: {asiento.reservado}")

    def reservar_asiento(self, numero, fila, edad, dia):
        """
        Reserva un asiento y calcula el precio final.

        Busca el asiento por número y fila.
        Si el asiento está disponible, lo reserva y calcula el precio
        aplicando los descuentos correspondientes por día y edad.

        Args:
            numero (int): Número del asiento.
            fila (str): Fila del asiento.
            edad (int): Edad del espectador.
            dia (str): Día de la semana.

        Raises:
            ValueError: Si el asiento no existe o ya está reservado.
        """
        asiento = self._buscar_asiento(numero, fila)
        if asiento:
            if not asiento.reservado:
                precio = self._calcular_precio(asiento, edad, dia)
                asiento.reservado = True
                print(f"Asiento reservado. Precio: ${precio:.2f}")
            else:
                raise ValueError("El asiento ya está reservado")
        else:
            raise ValueError("Asiento no encontrado")

    def cancelar_reserva(self, numero, fila):
        """
        Cancela la reserva de un asiento.

        Args:
            numero (int): Número del asiento.
            fila (str): Fila del asiento.

        Raises:
            ValueError: Si el asiento no existe o no está reservado.
        """
        asiento = self._buscar_asiento(numero, fila)
        if asiento and asiento.reservado:
            asiento.reservado = False
            print("Reserva cancelada.")
        else:
            raise ValueError("No se puede cancelar la reserva.")

    def _buscar_asiento(self, numero, fila):
        """
        Busca un asiento por número y fila en la lista de asientos.

        Args:
            numero (int): Número del asiento.
            fila (str): Fila del asiento.

        Returns:
            Asiento: El objeto Asiento si se encuentra, None en caso contrario.
        """
        for asiento in self.asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        return None

    def _calcular_precio(self, asiento, edad, dia):
        """
        Calcula el precio final de un asiento aplicando descuentos.

        Args:
            asiento (Asiento): Objeto Asiento.
            edad (int): Edad del espectador.
            dia (str): Día de la semana.

        Returns:
            float: Precio final del asiento.
        """
        precio = asiento.precio_base
        # Aquí puedes implementar la lógica de descuentos según edad y día
        if edad < 18:
            precio *= 0.8  # Descuento del 20% para menores de 18 años
        if dia.lower() == "miercoles":
            precio *= 0.9  # Descuento del 10% los miércoles
        return precio

def main():
    sala = SalaCine()
    for numero in range(1, 11):
        for fila in range(ord('A'), ord('Z') + 1):
            sala.agregar_asiento(Asiento(numero, chr(fila)))

    numero_asistentes = int(input("Ingrese el número de asistentes: "))
    edades = []
    for i in range(numero_asistentes):
        edad = int(input(f"Ingrese la edad del asistente {i + 1}: "))
        edades.append(edad)
    dia = input("Ingrese el día de la semana: ")

    for i in range(numero_asistentes):
        numero_asiento = int(input(f"Ingrese el número del asiento para el asistente {i + 1}: "))
        fila_asiento = input(f"Ingrese la fila del asiento para el asistente {i + 1}: ").upper()
        sala.reservar_asiento(numero_asiento, fila_asiento, edades[i], dia)

    sala.mostrar_asientos()

if __name__ == '__main__':
    main()