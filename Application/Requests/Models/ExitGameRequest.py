

from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class ExitGameRequest(Request):

    def __init__(self, *args, **kwargs):
        Request.__init__(self, *args, **kwargs)

    @staticmethod
    def object_hook(dct):

        if 'request' in dct and RequestType.exit_game.value == dct['request']:
            return ExitGameRequest()

        return dct
