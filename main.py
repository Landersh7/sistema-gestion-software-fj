from modelos import ServicioDesarrollo, ServicioAuditoria, ServicioConsultoria
from cliente_reserva import Cliente, Reserva
from excepciones import ErrorClienteExistente, SaldoInsuficiente, ServicioNoValido
from registros import inicializar_registros

# activamos el sistema de logs apenas arranca el programa
logger = inicializar_registros()

def simular_diez_operaciones():
    # esta función hace exactamente las 10 pruebas que pide la rúbrica (buenas y malas)
    print("\narrancando la simulación automática de las 10 operaciones")
    clientes = []
    reservas = []
    
    # lista con las 10 operaciones que combinan aciertos y errores a propósito
    operaciones = [
        ("1", "carlos pérez", "12345"), # 1. registro normal y válido
        ("1", "ana gómez", "67890"),   # 2. segundo registro válido
        ("1", "carlos pérez", "12345"), # 3. intento repetido (debe dar error de cliente existente)
        ("2", "12345", "1", 2000.0),   # 4. reserva de desarrollo con descuento
        ("2", "67890", "2", 400.0),    # 5. reserva con plata insuficiente (debe dar error)
        ("2", "67890", "2", 1000.0),   # 6. reserva de auditoría correcta
        ("2", "99999", "3", 1000.0),   # 7. cliente que no existe (debe dar error)
        ("2", "12345", "9", 1500.0),   # 8. servicio que no existe (debe dar error)
        ("1", "", "abc"),              # 9. datos mal escritos de cliente (debe dar error)
        ("2", "67890", "3", 600.0)     # 10. reserva de consultoría correcta
    ]
    
    # recorremos una por una las operaciones para ir probando el código
    for i, op in enumerate(operaciones, start=1):
        print(f"\n[prueba {i}] procesando: {op}")
        try:
            # si el primer valor es 1, intentamos registrar un cliente nuevo
            if op[0] == "1":
                nombre = op[1]
                cedula = op[2]
                
                # revisamos si la cédula ya está guardada para lanzar el error personalizado
                for c in clientes:
                    if c.cedula == cedula:
                        raise ErrorClienteExistente("este cliente ya está registrado en el sistema")
                
                nuevo_cliente = Cliente(nombre, cedula)
                clientes.append(nuevo_cliente)
                
                # guardamos la acción en el archivo de texto de logs
                logger.info(f"prueba {i}: cliente registrado con éxito -> {nombre}")
                print("resultado: cliente guardado bien")
                
            # si el primer valor es 2, intentamos hacer una reserva
            elif op[0] == "2":
                cedula = op[1]
                tipo = op[2]
                presupuesto = op[3]
                
                # buscamos al cliente en nuestra lista usando la cédula
                cliente_encontrado = next((c for c in clientes if c.cedula == cedula), None)
                if not cliente_encontrado:
                    raise ValueError("el cliente no se encuentra registrado en el sistema")
                
                # miramos qué servicio eligió el usuario y calculamos su precio
                if tipo == "1":
                    serv = ServicioDesarrollo("desarrollo web", 1500.0)
                    costo = serv.calcular_costo(descuento=100.0) # aquí usamos el parámetro opcional
                elif tipo == "2":
                    serv = ServicioAuditoria("auditoría de código", 800.0)
                    costo = serv.calcular_costo()
                elif tipo == "3":
                    serv = ServicioConsultoria("consultoría técnica", 500.0)
                    costo = serv.calcular_costo()
                else:
                    raise ServicioNoValido("el servicio elegido no existe")
                
                # comprobamos si el presupuesto del cliente alcanza para pagar
                if presupuesto < costo:
                    raise SaldoInsuficiente("el presupuesto no alcanza para cubrir el servicio")
                
                # creamos la reserva y la procesamos
                nueva_reserva = Reserva(cliente_encontrado, serv, duracion=2)
                nueva_reserva.procesamiento()
                reservas.append(nueva_reserva)
                
                # guardamos el éxito en los logs
                logger.info(f"prueba {i}: reserva creada con éxito para {cliente_encontrado.nombre}")
                print(f"resultado: reserva creada por un valor de {costo}")
                
        # atrapamos los errores controlados para que el programa no se caiga
        except (ErrorClienteExistente, SaldoInsuficiente, ServicioNoValido, ValueError, RuntimeError) as e:
            logger.error(f"error controlado en la prueba {i}: {e}")
            print(f"alerta atrapada: {e}")
        except Exception as e:
            logger.critical(f"error inesperado en la prueba {i}: {e}")
            print(f"error grave no esperado: {e}")
        else:
            # esto se ejecuta solo si todo salió bien sin ningún error
            print("estado: esta prueba pasó sin problemas")
        finally:
            # esto se ejecuta siempre al final de cada vuelta, pase lo que pase
            print("estado: fin de esta iteración")
            
    print(f"\nsimulación terminada. total clientes guardados: {len(clientes)}, total reservas hechas: {len(reservas)}")


def main():
    # menú principal para interactuar con la consola de manera sencilla
    while True:
        print("\nsistema de gestión software fj")
        print("1. ejecutar simulación automática de las 10 operaciones")
        print("2. salir")
        
        opcion = input("elige una opción: ")
        
        try:
            if opcion == "1":
                simular_diez_operaciones()
            elif opcion == "2":
                print("saliendo del programa, hasta luego.")
                break
            else:
                print("opción inválida, intenta de nuevo.")
        except Exception as e:
            print(f"ocurrió un error en el menú: {e}")


if __name__ == "__main__":
    main()