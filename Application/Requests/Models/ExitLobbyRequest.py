

from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class ExitLobbyRequest(Request):

    def __init__(self, *args, **kwargs):
        Request.__init__(self, *args, **kwargs)

    @staticmethod
    def object_hook(dct):

        if 'request' in dct and RequestType.exit_lobby.value == dct['request']:
            return ExitLobbyRequest()

        return dct
