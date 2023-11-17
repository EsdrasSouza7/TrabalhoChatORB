import sys
from omniORB import CORBA

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
ior = input("Enter the Chat Server's object reference: ")
obj = orb.string_to_object(ior)
chat = obj._narrow(ChatApp.Chat)

if chat is None:
    raise Exception("Object reference is not a Chat")

username = input("Enter your username: ")
chat.joinChat(username)

while True:
    print("1. Send a message")
    print("2. List users")
    print("3. Leave chat")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        message = input("Enter your message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        chat.sendMessage(username, message)

        received_message = chat.receiveMessage()
        print("Received:", received_message)

    elif choice == '2':
        users = chat.listUsers()
        print("Users online:", users)

    elif choice == '3':
        chat.leaveChat(username)
        break

orb.destroy()

