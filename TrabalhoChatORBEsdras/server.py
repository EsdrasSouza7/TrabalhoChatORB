from omniORB import CORBA, PortableServer
import ChatApp, ChatApp__POA

class ChatServer(ChatApp__POA.Chat):
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

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chat_server = ChatServer()
obj = chat_server._this()

print(f"Server running. Object reference: {orb.object_to_string(obj)}")


orb.run()

