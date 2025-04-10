import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print("\r" + " " * (len(input_prompt) + len(current_input)), end="")
                print("\r" + message)
                print(
                    input_prompt + current_input, end="", flush=True
                )
            else:
                break
        except:
            print("\nConexión cerrada.")
            client_socket.close()
            break


def send_messages(client_socket):
    global current_input
    while True:
        current_input = input(input_prompt)
        client_socket.send(current_input.encode("utf-8"))
        current_input = ""


def start_client():
    server_ip = "192.168.10.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

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