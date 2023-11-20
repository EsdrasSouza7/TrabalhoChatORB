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

username = input("Entre com o seu Nome de usuario: ")
chat.joinChat(username)

while True:

    system('clear')
    received_message = chat.receiveMessage()
    print("Chat: \n", received_message)
    print("\n1. Enviar Mensagem")
    print("2. Lista de Usuario")
    print("3. Calculadora")
    print("4. Sair do Chat")
    print("ou presione Enter para fechar o Menu.")
    
    choice = input("Choose an option (1/2/3/4): ")

    if choice == '1':
        message = input("Digite sua Mensagem: ")
        chat.sendMessage(username, message)

    elif choice == '2':
        users = chat.listUsers()
        print("Usuario Online:", users)
        input("Pressione Enter Para Sair")

    elif choice == '3':
        expressao = input("Digite uma expressão: ")
        received_resposta = str(chat.calculadora(expressao))
        #received_resposta = str(received_resposta)
        mensagem = (expressao + ' = ' + received_resposta)
        chat.sendMessage(username, mensagem)

    elif choice == '4':
        chat.leaveChat(username)
        break

    

orb.destroy()
