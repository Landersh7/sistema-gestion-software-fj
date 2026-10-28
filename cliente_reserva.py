class Cliente:
    # esta clase guarda los datos básicos de cada cliente que usa el sistema
    def __init__(self, nombre, cedula):
        # validamos que el nombre no esté vacio y que la cédula sea solo de números
        if not nombre or not isinstance(nombre, str):
            raise ValueError("el nombre del cliente no puede estar vacío")
        
        if not cedula or not str(cedula).isdigit():
            raise ValueError("la cédula del cliente debe tener solo números")
        
        # guardamos los datos de forma privada para proteger la información
        self.__nombre = nombre
        self.__cedula = str(cedula)

    @property
    def nombre(self):
        # esto nos permite ver el nombre desde afuera de manera segura
        return self.__nombre

    @property
    def cedula(self):
        # esto nos permite ver la cédula desde afuera de manera segura
        return self.__cedula


class Reserva:
    # esta clase junta al cliente con el servicio que contrató y maneja su estado
    def __init__(self, cliente, servicio, duracion=1):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente" # arranca pendiente por defecto

    def confirmar(self):
        # cambiamos el estado a confirmada si todo sale bien
        self.estado = "Confirmada"
        print(f"reserva confirmada para el cliente {self.cliente.nombre}")

    def cancelar(self):
        # cambiamos el estado a cancelada si pasa algún problema
        self.estado = "Cancelada"
        print(f"reserva cancelada por problemas para el cliente {self.cliente.nombre}")

    def procesamiento(self):
        # aquí intentamos procesar la reserva y si algo falla la cancelamos usando try y except
        try:
            if self.duracion <= 0:
                raise ValueError("la duración debe ser mayor a cero")
            self.confirmar()
        except Exception as e:
            self.cancelar()
            # conectamos el error original con uno nuevo para cumplir con la rúbrica
            raise RuntimeError("falló el procesamiento de la reserva") from e