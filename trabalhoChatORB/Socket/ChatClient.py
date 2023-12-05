import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Servidor diz: {data.decode('utf-8')}")

def main():
    host = '127.0.0.1'  # IP do servidor
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("Você: ")
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()

