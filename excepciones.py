# aca definimos nuestros propios errores personalizados para el programa
# los usamos para controlar situaciones especiales del negocio de software fj

class ErrorClienteExistente(Exception):
    # este error salta cuando tratamos de registrar un cliente con una cédula que ya está en la lista
    pass


class SaldoInsuficiente(Exception):
    # este error salta cuando el cliente no tiene suficiente presupuesto para pagar el servicio
    pass


class ServicioNoValido(Exception):
    # este error salta si el usuario elige una opción de servicio que no aparece en el menú
    pass


class ErrorReserva(Exception):
    # este error sirve como base general por si algo falla al momento de procesar las reservas
    pass