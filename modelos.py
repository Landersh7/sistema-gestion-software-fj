from abc import ABC, abstractmethod

class Servicio(ABC):
    # esta es la clase padre abstracta que obliga a las demás a tener la función de calcular costo
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        # las clases hijas deben rellenar esta función obligatoriamente
        pass


class ServicioDesarrollo(Servicio):
    # clase para calcular el costo de desarrollo de software
    def calcular_costo(self, descuento=0.0):
        # aplicamos un incremento del 20 por ciento y le restamos un descuento opcional
        costo_con_impuesto = self.costo_base * 1.20
        return costo_con_impuesto - descuento


class ServicioAuditoria(Servicio):
    # clase para calcular el costo de auditorías de código
    def calcular_costo(self):
        # aplicamos un recargo del 10 por ciento específico para auditorías
        return self.costo_base * 1.10


class ServicioConsultoria(Servicio):
    # clase para calcular el costo de consultorías técnicas
    def calcular_costo(self):
        # aplicamos un recargo pequeño del 5 por ciento
        return self.costo_base * 1.05