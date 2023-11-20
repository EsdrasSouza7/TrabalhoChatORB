from omniORB import CORBA
import ChatApp__POA
import logging

# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

logging.basicConfig(filename='Conversas.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='a',
                    level=logging.INFO,
                    format=log_format)

# Instancia do objeto getLogger()
logger = logging.getLogger('root')

class ChatServant(ChatApp__POA.Chat):
    def __init__(self):
        self.users = []
        self.messages = []

    def sendMessage(self, username, message):
        formatted_message = f"{username}: {message}"
        print(formatted_message)
        logger.info(f'{formatted_message}')
        self.messages.append(formatted_message)

    def receiveMessage(self):
        if self.messages:
            log = '\n'.join(self.messages)
            return log
        else:
            return "No messages"

    def joinChat(self, username):
        self.users.append(username)
        print(f"{username} Entrou no Chat.")
        logger.info(f"{username} Entrou no Chat.")
        self.messages.append(f"{username} Entrou no Chat.")

    def leaveChat(self, username):
        self.users.remove(username)
        print(f"{username} Saiu do Chat.")
        logger.info(f"{username} Saiu do Chat.")
        self.messages.append(f"{username} Saiu do Chat.")

    def listUsers(self):
        return ', '.join(self.users)

    def calculadora(self, expressao):
        try:
            # Avalia a expressão e imprime o resultado
            resultado = eval(expressao)
        except Exception as e:
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
