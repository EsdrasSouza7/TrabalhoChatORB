from omniORB import CORBA
import ChatApp

orb = CORBA.ORB_init([], CORBA.ORB_ID)
ior = input("Entre com o IOR: ")

obj = orb.string_to_object(ior)
chat = obj._narrow(ChatApp.Chat)

if chat is None:
    raise Exception("Object reference is not a Chat")

while True:
    #remover o input para que o client fique sempre preocurando novas mensagens.
    #clear e um /algumacoisa para quebrar linha toda vez que buscar mensagens novas??
    message = input("Type a message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    if message.lower() == "calculadora":
        expressao = input("Digite uma expressão (ou 'sair' para encerrar): ")
        received_resposta = chat.calculadora(expressao)
        print(f"Resposa recebida do servidor: {received_resposta}")
    chat.sendMessage(message)

    received_message = chat.receiveMessage()
    print(f"Received message from server: {received_message}")

orb.destroy()
