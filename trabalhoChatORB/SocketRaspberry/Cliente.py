# client.py
import socket

# Configurações do cliente
host = 'ip_do_raspberry'  # Insira o endereço IP do Raspberry Pi aqui
port = 12345              # Número da porta

# Inicializa o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Recebe a mensagem de boas-vindas do servidor
server_message = client_socket.recv(1024).decode()
print(server_message)

# Loop para enviar e receber mensagens
while True:
    # Envia a mensagem para o servidor
    client_message = input("Digite sua mensagem: ")
    client_socket.send(client_message.encode())

    # Se o cliente digitar 'sair', encerra a conexão
    if client_message.lower() == 'sair':
        break

    # Recebe a mensagem do servidor
    server_message = client_socket.recv(1024).decode()
    print(f"Servidor: {server_message}")

# Fecha a conexão com o servidor
client_socket.close()
