# Sistema de Gestión - Software FJ

Este es el proyecto desarrollado para la Fase 4, este es un sistema hecho en Python que maneja clientes, servicios y reservas usando Programación Orientada a Objetos (POO), sin necesidad de bases de datos y se organizo de la siguiente manera:

- excepciones.py: Aqui estan los errores que se personalizaron para controlar situaciones del negocio como clientes repetidos o saldos que no alcanzan o cosas asi que pudan pasar para que el codigo no se detenga
- registros.py: Este configura el sistema para guardar un historial de todo lo que va pasando en un archivo de texto 
- cliente_reserva.py: Aqui se guarda la información de los clientes de firma segura y maneja el estado de las reservas para tener una mejor organizacion
- modelos.py: Aqui se encuentra la clase que es la base de los servicios y las clases hijas que calculan los costos aplicando polimorfismo
- main.py: Para finalizar tenemos este codigo que es el programa principal que muestra el menú y ejecuta automáticamente las 10 pruebas porque aqui es donde se condenza todo el codigo

la forma de ejecutarlo o ponerlo a funcionar es la siguiente
1. Primero se abre el terminal en la carpeta donde se tienen todos los archivos
2. Luego se ejecuta el programa principal con este comando:
   ```
   bash
   python main.py
   ```
   En algunos programas solo toca darle f5 que es el atajo y ya funciona
