#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Cliente
Objetivo: Crear un cliente TCP que se conecte a un servidor e intercambie mensajes básicos
"""

import socket

HOST = 'localhost'  # Escuchar en todas las interfaces disponibles
PORT = 9001

# Crear un socket TCP/IP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)

# Conectar el socket al servidor en la dirección y puerto especificados
cliente.connect((HOST, PORT))
# Enviar datos al servidor (convertidos a bytes)
# sendall() asegura que todos los datos sean enviados
cliente.sendall(b"Mundo!")
# Recibir datos del servidor (hasta 1024 bytes)
respuesta = cliente.recv(1024)
# Decodificar e imprimir los datos recibidos
print(f"Respuesta: {respuesta}")
#Cerrar la conexión con el servidor
cliente.close()
