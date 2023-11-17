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
#tentar tirar o pop para ver se aparece no outro cliente
    def calculadora(self):
        # Solicitação de entrada do usuário
        expressao = input("Digite uma expressão (ou 'sair' para encerrar): ")

        try:
            # Avalia a expressão e imprime o resultado
            resultado = eval(expressao)
        except Exception as e:
            # Se houver um erro, imprime uma mensagem de erro
            resultado = "Erro ao calcular a expressão:", e
        return resultado



orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

chat_server = ChatServer()
obj = chat_server._this()

print(f"Server running. Object reference: {orb.object_to_string(obj)}")


orb.run()

