

from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class ExitGameRequest(Request):

    def __init__(self):
        Request.__init__(self, RequestType.exit_game)

    def decode_dct(self, dct):

        if self.request_of_type(dct):

            exit_game_request = ExitGameRequest()

            return exit_game_request

        raise TypeError(f"'{self.__class__.__name__}' could not be decoded")
