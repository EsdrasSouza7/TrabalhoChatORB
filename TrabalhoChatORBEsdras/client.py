from omniORB import CORBA
import ChatApp

orb = CORBA.ORB_init([], CORBA.ORB_ID)
ior = input("Entre com o IOR: ")

obj = orb.string_to_object(ior)
chat = obj._narrow(ChatApp.Chat)

if chat is None:
    raise Exception("Object reference is not a Chat")

while True:
    message = input("Type a message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    chat.sendMessage(message)

    received_message = chat.receiveMessage()
    print(f"Received message from server: {received_message}")

orb.destroy()
