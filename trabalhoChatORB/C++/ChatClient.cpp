#include "Chat.hh"
#include <iostream>

int main(int argc, char** argv) {
    try {
        CORBA::ORB_var orb = CORBA::ORB_init(argc, argv);

        CORBA::Object_var obj = orb->string_to_object("corbaname::localhost:1050#ChatServer");
        Chat::ChatServer_var chatServerRef = Chat::ChatServer::_narrow(obj);

        if (CORBA::is_nil(chatServerRef)) {
            std::cerr << "Error: Nil reference." << std::endl;
            return 1;
        }

        chatServerRef->sendMessage("User1", "Hello, Server!");

        char* response = chatServerRef->receiveMessage();
        std::cout << "Server response: " << response << std::endl;

        CORBA::string_free(response);
        orb->destroy();
    } catch (const CORBA::Exception& e) {
        std::cerr << "Exception: " << e << std::endl;
    }

    return 0;
}

