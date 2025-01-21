class Asiento:
    """
    Representa un asiento en una sala de cine.

    Atributos:
        - numero (int): Número del asiento.
        - fila (str): Fila del asiento.
        - reservado (bool): Estado de la reserva (True o False).
        - precio (float): Precio del asiento (varía según el día y la edad del espectador).
    """

    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 10.0  # Precio base

    # Getters y setters
    @property
    def numero(self):
        return self.__numero

    @property
    def fila(self):
        return self.__fila

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self, valor):
        if isinstance(valor, bool):
            self.__reservado = valor
        else:
            raise TypeError("El valor de 'reservado' debe ser booleano")

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self.__precio = valor
        else:
            raise ValueError("El precio debe ser positivo")

class SalaCine:
    """
    Administra una lista de asientos y permite las siguientes operaciones:
    - Agregar un asiento
    - Reservar asiento
    - Cancelar reserva
    - Mostrar asientos
    - Buscar asiento
    """

    def __init__(self):
        self.__asientos = []

    def inicializar_sala(self, filas=26, asientos_por_fila=10):
        """
        Inicializa la sala con un número determinado de filas y asientos por fila.

        Args:
            filas (int): Número de filas en la sala.
            asientos_por_fila (int): Número de asientos por fila.
        """
        self.__asientos = []
        for numero in range(1, asientos_por_fila + 1):
            for fila in range(ord('A'), ord('A') + filas):
                self.agregar_asiento(Asiento(numero, chr(fila)))

    def agregar_asiento(self, asiento):
        """
        Agrega un asiento a la sala.

        Args:
            asiento (Asiento): Objeto Asiento a agregar.

        Raises:
            ValueError: Si el asiento ya existe en la sala.
        """
        if not self._buscar_asiento(asiento.numero, asiento.fila):
            self.__asientos.append(asiento)
        else:
            raise ValueError("El asiento ya existe")

    def reservar_asiento(self, numero, fila, edad, dia):
        """
        Reserva un asiento y asigna el precio correspondiente.

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
                precio = self._calcular_precio(edad, dia)
                asiento.precio = precio
                asiento.reservado = True
                print(f"Asiento {asiento.numero}, Fila {asiento.fila} reservado. Precio: ${precio:.2f}")
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
            asiento.precio = 10.0  # Restablece el precio base
            print("Reserva cancelada.")
        else:
            raise ValueError("No se puede cancelar la reserva.")

    def mostrar_asientos(self):
        """
        Muestra todos los asientos, indicando si están reservados y su precio.
        """
        filas = sorted(set(asiento.fila for asiento in self.__asientos))
        for fila in filas:
            asientos_fila = sorted([asiento for asiento in self.__asientos if asiento.fila == fila], key=lambda x: x.numero)
            for asiento in asientos_fila:
                estado = "Reservado" if asiento.reservado else "Disponible"
                print(f"Asiento {asiento.numero}, Fila {asiento.fila}, Estado: {estado}, Precio: ${asiento.precio:.2f}")

    def _buscar_asiento(self, numero, fila):
        """
        Busca un asiento por número y fila en la lista de asientos.

        Args:
            numero (int): Número del asiento.
            fila (str): Fila del asiento.

        Returns:
            Asiento: El objeto Asiento si se encuentra, None en caso contrario.
        """
        for asiento in self.__asientos:
            if asiento.numero == numero and asiento.fila == fila:
                return asiento
        return None

    def _calcular_precio(self, edad, dia):
        """
        Calcula el precio final de un asiento aplicando descuentos.

        Args:
            edad (int): Edad del espectador.
            dia (str): Día de la semana.

        Returns:
            float: Precio final del asiento.
        """
        precio_base = 10.0
        if dia.lower() == "miércoles":
            precio_base *= 0.8  # Descuento del 20% los miércoles
        if edad > 65:
            precio_base *= 0.7  # Descuento del 30% para mayores de 65 años
        return precio_base

def main():
    sala = SalaCine()
    
    while True:
        print("\nMenú:")
        print("1. Inicializar sala")
        print("2. Hacer reserva")
        print("3. Cancelar reserva")
        print("4. Mostrar estado de la sala")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            filas = int(input("Ingrese el número de filas: "))
            asientos_por_fila = int(input("Ingrese el número de asientos por fila: "))
            sala.inicializar_sala(filas, asientos_por_fila)
            print("Sala inicializada.")
        
        elif opcion == '2':
            num_reservas = int(input("Ingrese el número de reservas a realizar: "))
            for _ in range(num_reservas):
                while True:
                    try:
                        edad = int(input("Ingrese la edad del espectador: "))
                        dia = input("Ingrese el día de la semana: ")
                        numero_asiento = int(input("Ingrese el número del asiento: "))
                        fila_asiento = input("Ingrese la fila del asiento: ").upper()
                        sala.reservar_asiento(numero_asiento, fila_asiento, edad, dia)
                        break  # Sale del bucle si la reserva es exitosa
                    except ValueError as e:
                        print(e)
                        print("Por favor, intente nuevamente con un asiento diferente.")
        
        elif opcion == '3':
            num_cancelaciones = int(input("Ingrese el número de reservas a cancelar: "))
            for _ in range(num_cancelaciones):
                try:
                    numero_asiento = int(input("Ingrese el número del asiento a cancelar: "))
                    fila_asiento = input("Ingrese la fila del asiento a cancelar: ").upper()
                    sala.cancelar_reserva(numero_asiento, fila_asiento)
                except ValueError as e:
                    print(e)
        
        elif opcion == '4':
            sala.mostrar_asientos()
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == '__main__':
    main()