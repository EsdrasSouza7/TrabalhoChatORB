import socket
import threading

def handle_client(client_socket, addr):
    print(f"Conexão aceita de {addr[0]}:{addr[1]}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"({addr[0]}:{addr[1]}) diz: {message}")

    print(f"Conexão de {addr[0]}:{addr[1]} encerrada")
    client_socket.close()

def main():
    host = '0.0.0.0'  # Aceita conexões de qualquer endereço IP
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Servidor ouvindo em {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    main()

