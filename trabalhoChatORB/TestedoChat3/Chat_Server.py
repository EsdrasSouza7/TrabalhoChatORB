import sys
from omniORB import CORBA, PortableServer
import ChatApp__POA

class ChatServant(ChatApp__POA.Chat):
    def __init__(self):
        self.users = {}
        self.messages = []

    def sendMessage(self, username, message):
        formatted_message = f"{username}: {message}"
        print(formatted_message)
        self.messages.append(formatted_message)

    def receiveMessage(self):
        if self.messages:
            return self.messages.pop(0)
        else:
            return "No messages"

    def joinChat(self, username):
        self.users[username] = self._default_POA().servant_to_reference(self._this())
        print(f"{username} joined the chat.")

    def leaveChat(self, username):
        del self.users[username]
        print(f"{username} left the chat.")

    def listUsers(self):
        return ', '.join(self.users.keys())

    def sendPublicMessage(self, username, message):
        formatted_message = f"{username} (public): {message}"
        print(formatted_message)
        self.messages.append(formatted_message)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chatServant = ChatServant()
chatObject = chatServant._this()

print("Chat Server running...")
print("Object reference:", orb.object_to_string(chatObject))

orb.run()

