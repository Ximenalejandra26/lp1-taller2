#!/usr/bin/env python3
"""
Problema 3: Chat simple con múltiples clientes - Servidor
Objetivo: Crear un servidor de chat que maneje múltiples clientes simultáneamente usando threads
"""

import socket
import threading

#Definir la dirección y puerto del servidor
HOST = 'localhost'
PORT = 9003
# Lista para mantener todos los sockets de clientes conectados
clientes = []

def atender_cliente(cliente,nombre):
    """
    Maneja la comunicación con un cliente específico en un hilo separado.
    
    Args:
        client_socket: Socket del cliente
        client_name: Nombre del cliente
    """ 
    while True:
        try:
            #Recibir datos del cliente (hasta 1024 bytes)
            mensaje = cliente.recv(1024)
            # Si no se reciben datos, el cliente se desconectó
            if not mensaje:
                break
                
            # Formatear el mensaje con el nombre del cliente
            mensaje = f"{nombre}: {mensaje.decode()}"
            
            # Imprimir el mensaje en el servidor
            print(f"{nombre}: {mensaje.decode()}")
                              
            #Retransmitir el mensaje a todos los clientes excepto al remitente
            broadcast(mensaje, cliente)  
            
        except ConnectionResetError:
            # Manejar desconexión inesperada del cliente
            clientes.remove(cliente)
            cliente.close()
            break

def broadcast(mensaje, emisor):

    """
    Envía un mensaje a todos los clientes conectados excepto al remitente.
     
    Args:
        message: Mensaje a enviar (string)
        sender_socket: Socket del cliente que envió el mensaje original
    """
    for cliente in clientes:
        if cliente != emisor:
            # Enviar el mensaje codificado a bytes a cada cliente
            cliente.send(mensaje.encode())

#Crear un socket TCP/IP
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Enlazar el socket a la dirección y puerto especificados
servidor.bind((HOST, PORT))
#Poner el socket en modo escucha
# El parámetro define el número máximo de conexiones en cola
servidor.listen(5)
print("El servidor 'Chat' esta esperando conexiones...")

# Bucle principal para aceptar conexiones entrantes
while True:
    #Aceptar una conexión entrante
    # client: nuevo socket para comunicarse con el cliente
    # addr: dirección y puerto del cliente
    cliente, direccion = servidor.accept()
    print(f"cliente conectado desde la IP {direccion}")
    
    #Recibir el nombre del cliente (hasta 1024 bytes) y decodificarlo
    nombre = cliente.recv(1024).decode()
    #Agregar el socket del cliente a la lista de clientes conectados
    clientes.append(cliente) 
    # Enviar mensaje de confirmación de conexión al cliente
    cliente.send("ya estás conectado!".encode())
    
    # Notificar a todos los clientes que un nuevo usuario se unió al chat
    broadcast(f"{nombre} se ha unido al Chat.", cliente)
    
    #Crear e iniciar un hilo para manejar la comunicación con este cliente
    # target: función que se ejecutará en el hilo
    # args: argumentos que se pasarán a la función
    hilo_cliente = threading.Thread(target=atender_cliente, args=(cliente,nombre))
    hilo_cliente.start()

