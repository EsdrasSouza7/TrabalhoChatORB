from omniORB import CORBA
import Example

orb = CORBA.ORB_init([], CORBA.ORB_ID)
ior = input("Enter IOR of Greetings object: ")

obj = orb.string_to_object(ior)
greetings = obj._narrow(Example.Greetings)

if greetings is None:
    print("Object reference is not a Greetings")
else:
    message = greetings.sayHello()
    print("Message from server:", message)

