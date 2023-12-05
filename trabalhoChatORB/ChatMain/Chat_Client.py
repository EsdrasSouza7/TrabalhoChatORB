from os import system
import sys
from omniORB import CORBA
import ChatApp

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
ior = input("Enter the Chat Server's object reference: ")
obj = orb.string_to_object(ior)
chat = obj._narrow(ChatApp.Chat)

if chat is None:
    raise Exception("Object reference is not a Chat")

username = input("Enter your username: ")
chat.joinChat(username)

while True:
    system('clear')
    received_message = chat.receiveMessage()
    print("Chat: \n", received_message, '\n')
    print("1. Send a message")
    print("2. List users")
    print("3. Calculator")
    print("4. Leave chat")
    print("ou Pressione Enter para atualiza o chat")
    
    choice = input("Choose an option (1/2/3/4): ")

    if choice == '1':
        message = input("Enter your message: ")
        chat.sendMessage(username, message)

    elif choice == '2':
        users = chat.listUsers()
        print("Users online:", users)
        input("Pressione Enter Para Sair")

    elif choice == '3':
        expressao = input("Digite uma expressão: ")
        received_resposta = chat.calculadora(expressao)
        print(f"Resposa recebida do servidor: {received_resposta}")
        received_resposta = str(received_resposta)
        mensagem = (expressao + ' = ' + received_resposta)
        chat.sendMessage(username, mensagem)

    elif choice == '4':
        chat.leaveChat(username)
        break

    

orb.destroy()

