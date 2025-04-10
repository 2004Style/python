import socket
import threading


def receive_messages(client_socket):
    """
    Recibir mensajes del servidor y mostrarlos.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                # Limpiar la línea actual del input y mostrar el mensaje recibido
                print("\r" + " " * (len(input_prompt) + len(current_input)), end="")
                print("\r" + message)
                print(
                    input_prompt + current_input, end="", flush=True
                )  # Volver a mostrar el prompt
            else:
                break
        except:
            print("\nConexión cerrada.")
            client_socket.close()
            break


def send_messages(client_socket):
    """
    Enviar mensajes al servidor.
    """
    global current_input
    while True:
        current_input = input(input_prompt)
        client_socket.send(current_input.encode("utf-8"))
        current_input = ""  # Limpiar la entrada después de enviar el mensaje


def start_client():
    """
    Conectar al servidor y empezar a enviar/recibir mensajes.
    """
    # server_ip = "192.168.179.23"
    server_ip = "192.168.10.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Enviar el nombre del cliente al servidor
    global client_name, input_prompt, current_input
    client_name = input("ingrese su nombre: ")
    input_prompt = "Tu: "
    current_input = ""

    client_socket.send(client_name.encode("utf-8"))

    # Iniciar hilos para enviar y recibir mensajes simultáneamente
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()


if __name__ == "__main__":
    start_client()
