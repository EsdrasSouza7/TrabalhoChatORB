from omniORB import CORBA
import ChatApp
import sys

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
obj = orb.string_to_object("corbaname::localhost:1050#ChatServer")

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
