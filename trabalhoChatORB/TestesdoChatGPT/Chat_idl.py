# Python stubs generated by omniidl from Chat.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "ChatApp"
#
__name__ = "ChatApp"
_0_ChatApp = omniORB.openModule("ChatApp", r"Chat.idl")
_0_ChatApp__POA = omniORB.openModule("ChatApp__POA", r"Chat.idl")


# interface Chat
_0_ChatApp._d_Chat = (omniORB.tcInternal.tv_objref, "IDL:ChatApp/Chat:1.0", "Chat")
omniORB.typeMapping["IDL:ChatApp/Chat:1.0"] = _0_ChatApp._d_Chat
_0_ChatApp.Chat = omniORB.newEmptyClass()
class Chat :
    _NP_RepositoryId = _0_ChatApp._d_Chat[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_ChatApp.Chat = Chat
_0_ChatApp._tc_Chat = omniORB.tcInternal.createTypeCode(_0_ChatApp._d_Chat)
omniORB.registerType(Chat._NP_RepositoryId, _0_ChatApp._d_Chat, _0_ChatApp._tc_Chat)

# Chat operations and attributes
Chat._d_sendMessage = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)
Chat._d_receiveMessage = ((), ((omniORB.tcInternal.tv_string,0), ), None)
Chat._d_joinChat = (((omniORB.tcInternal.tv_string,0), ), (), None)
Chat._d_leaveChat = (((omniORB.tcInternal.tv_string,0), ), (), None)
Chat._d_listUsers = ((), ((omniORB.tcInternal.tv_string,0), ), None)

# Chat object reference
class _objref_Chat (CORBA.Object):
    _NP_RepositoryId = Chat._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def sendMessage(self, *args):
        return self._obj.invoke("sendMessage", _0_ChatApp.Chat._d_sendMessage, args)

    def receiveMessage(self, *args):
        return self._obj.invoke("receiveMessage", _0_ChatApp.Chat._d_receiveMessage, args)

    def joinChat(self, *args):
        return self._obj.invoke("joinChat", _0_ChatApp.Chat._d_joinChat, args)

    def leaveChat(self, *args):
        return self._obj.invoke("leaveChat", _0_ChatApp.Chat._d_leaveChat, args)

    def listUsers(self, *args):
        return self._obj.invoke("listUsers", _0_ChatApp.Chat._d_listUsers, args)

omniORB.registerObjref(Chat._NP_RepositoryId, _objref_Chat)
_0_ChatApp._objref_Chat = _objref_Chat
del Chat, _objref_Chat

# Chat skeleton
__name__ = "ChatApp__POA"
class Chat (PortableServer.Servant):
    _NP_RepositoryId = _0_ChatApp.Chat._NP_RepositoryId


    _omni_op_d = {"sendMessage": _0_ChatApp.Chat._d_sendMessage, "receiveMessage": _0_ChatApp.Chat._d_receiveMessage, "joinChat": _0_ChatApp.Chat._d_joinChat, "leaveChat": _0_ChatApp.Chat._d_leaveChat, "listUsers": _0_ChatApp.Chat._d_listUsers}

Chat._omni_skeleton = Chat
_0_ChatApp__POA.Chat = Chat
omniORB.registerSkeleton(Chat._NP_RepositoryId, Chat)
del Chat
__name__ = "ChatApp"

#
# End of module "ChatApp"
#
__name__ = "Chat_idl"

_exported_modules = ( "ChatApp", )

# The end.
