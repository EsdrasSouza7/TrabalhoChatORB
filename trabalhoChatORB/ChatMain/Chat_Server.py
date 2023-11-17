#import sys
from omniORB import CORBA, PortableServer
import ChatApp, ChatApp__POA

class ChatServant(ChatApp__POA.Chat):
    def __init__(self):
        self.users = []
        self.messages = []

    def sendMessage(self, username, message):
        formatted_message = f"{username}: {message}"
        print(formatted_message)
        self.messages.append(formatted_message)

    def receiveMessage(self):
        if self.messages:
            log = '\n'.join(self.messages)
            return log
        else:
            return "No messages"

    def joinChat(self, username):
        self.users.append(username)
        print(f"{username} joined the chat.")
        self.messages.append(f"{username} joined the chat.")

    def leaveChat(self, username):
        self.users.remove(username)
        print(f"{username} left the chat.")
        self.messages.append(f"{username} left the chat.")

    def listUsers(self):
        return ', '.join(self.users)

    def calculadora(self, expressao):
        try:
            # Avalia a expressão e imprime o resultado
            resultado = eval(expressao)
        except Exception as e:
            # Se houver um erro, imprime uma mensagem de erro
            return  "Erro ao calcular a expressão:", e
        return resultado

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chatServant = ChatServant()
chatObject = chatServant._this()

print("Chat Server running...")
print("Object reference:", orb.object_to_string(chatObject))

orb.run()

