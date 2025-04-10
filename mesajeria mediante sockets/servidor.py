import socket
import threading

# Diccionario para almacenar los clientes conectados con sus nombres
clients = {}


def broadcast(message, current_client):
    """
    Enviar un mensaje a todos los clientes excepto al que lo envió.
    """
    for client, name in clients.items():
        if client != current_client:
            try:
                client.send(message)
            except:
                client.close()
                del clients[client]


def handle_client(client_socket):
    """
    Manejar la comunicación con un cliente.
    """
    try:
        # Recibir el nombre del cliente
        client_name = client_socket.recv(1024).decode("utf-8")
        welcome_message = f"{client_name} se ha unido al chat."
        print(welcome_message)
        broadcast(welcome_message.encode("utf-8"), client_socket)

        # Almacenar el cliente en el diccionario con su nombre
        clients[client_socket] = client_name

        while True:
            # Recibir mensaje del cliente
            message = client_socket.recv(1024)
            if message:
                formatted_message = f"{client_name}: {message.decode('utf-8')}"
                print(formatted_message)
                broadcast(formatted_message.encode("utf-8"), client_socket)
            else:
                break
    except:
        pass
    finally:
        # Remover cliente al desconectarse
        client_socket.close()
        del clients[client_socket]
        disconnect_message = f"{client_name} ha salido del chat."
        print(disconnect_message)
        broadcast(disconnect_message.encode("utf-8"), None)


def start_server():
    """
    Iniciar el servidor y aceptar conexiones entrantes.
    """
    host = "0.0.0.0"  # Escuchar en todas las interfaces
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    #print(f"Servidor escuchando en {host}:{port}")
    print("Servidor ejecutado y preparado para los usuarios")

    while True:
        client_socket, client_address = server_socket.accept()
        #print(f"Conexión aceptada de {client_address}")

        # Iniciar un nuevo hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    start_server()
