

from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class ExitLobbyRequest(Request):

    def __init__(self):
        Request.__init__(self, RequestType.exit_lobby)

    def decode_dct(self, dct):

        if self.request_of_type(dct):

            exit_lobby_request = ExitLobbyRequest()

            return exit_lobby_request

        raise TypeError(f"'{self.__class__.__name__}' could not be decoded")
