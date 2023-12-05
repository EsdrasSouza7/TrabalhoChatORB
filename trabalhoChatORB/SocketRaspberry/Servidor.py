# server.py
import socket

# Configurações do servidor
host = '0.0.0.0'  # Escuta em todas as interfaces
port = 12345       # Número da porta

# Inicializa o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Servidor escutando em {host}:{port}")

# Aceita conexões dos clientes
while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexão recebida de {addr}")

    # Envia uma mensagem de boas-vindas para o cliente
    message = "Bem-vindo ao chat! Digite 'sair' para encerrar a conexão."
    client_socket.send(message.encode())

    # Loop para receber e enviar mensagens
    while True:
        # Recebe a mensagem do cliente
        client_message = client_socket.recv(1024).decode()

        # Se o cliente digitar 'sair', encerra a conexão
        if client_message.lower() == 'sair':
            break

        print(f"Cliente ({addr}): {client_message}")

        # Envia uma mensagem de volta para o cliente
        server_message = input("Digite sua mensagem: ")
        client_socket.send(server_message.encode())

    # Fecha a conexão com o cliente
    print(f"Conexão encerrada com {addr}")
    client_socket.close()
