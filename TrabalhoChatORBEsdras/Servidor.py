from omniORB import CORBA, PortableServer
import ChatApp
import sys

class ChatServer(ChatApp.Chat):
    def __init__(self):
        self.messages = []

    def sendMessage(self, message):
        print(f"Received message: {message}")
        self.messages.append(message)

    def receiveMessage(self):
        if self.messages:
            return self.messages.pop(0)
        else:
            return "No messages"

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

chat_server = ChatServer()
chat_server_ref = chat_server._this()

poa_manager = poa._get_the_POAManager()
poa_manager.activate()

print(f"Server running. Object reference: {chat_server_ref}")

orb.run()
