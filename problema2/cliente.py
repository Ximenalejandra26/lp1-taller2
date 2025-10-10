#!/usr/bin/env python3
"""
Problema 2: Comunicación bidireccional - Cliente
Objetivo: Crear un cliente TCP que envíe un mensaje al servidor y reciba la misma respuesta
"""

import socket

# Definir la dirección y puerto del servidor
HOST = 'localhost'
PORT = 9002

# Solicitar mensaje al usuario por consola
mensaje = input("Digite tu mensaje: ")

# Crear un socket TCP/IP
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor en la dirección y puerto especificados
cliente.connect((HOST, PORT))

# Mostrar mensaje que se va a enviar
print(f"Mensaje enviado: '{mensaje}'")

#Codificar el mensaje a bytes y enviarlo al servidor
# sendall() asegura que todos los datos sean enviados
cliente.sendall(mensaje . encode())

# Recibir datos del servidor (hasta 1024 bytes)
respuesta = cliente.recv(1024)

# Decodificar e imprimir los datos recibidos
print("Respuesta del 'Echo': '{respuesta}'" )

#Cerrar la conexión con el servidor
cliente.close()
