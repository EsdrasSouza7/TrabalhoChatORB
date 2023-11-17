from omniORB import CORBA
import Example, Example__POA

class Greetings_i(Example__POA.Greetings):
    def sayHello(self):
        return "Hello from OmniORBpy!"

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

greetings = Greetings_i()
obj = greetings._this()

print(orb.object_to_string(obj))
print("Server ready...")

orb.run()

