#include "Chat.hh"
#include <iostream>

class ChatServer_i : public POA_Chat::ChatServer {
public:
    void sendMessage(const char* username, const char* message) override {
        std::cout << username << ": " << message << std::endl;
    }

    char* receiveMessage() override {
        return CORBA::string_dup("Server received the message.");
    }
};

int main(int argc, char** argv) {
    try {
        CORBA::ORB_var orb = CORBA::ORB_init(argc, argv);

        PortableServer::POA_var poa = CORBA::RootPOA::_narrow(orb->resolve_initial_references("RootPOA"));

        PortableServer::POAManager_var pman = poa->the_POAManager();
        pman->activate();

        ChatServer_i* chatServer = new ChatServer_i();

        CORBA::Object_var obj = poa->servant_to_reference(chatServer);
        Chat::ChatServer_var chatServerRef = Chat::ChatServer::_narrow(obj);

        CORBA::String_var ior = orb->object_to_string(chatServerRef);
        std::cout << ior << std::endl;

        orb->run();
        delete chatServer;
        orb->destroy();
    } catch (const CORBA::Exception& e) {
        std::cerr << "Exception: " << e << std::endl;
    }

    return 0;
}

