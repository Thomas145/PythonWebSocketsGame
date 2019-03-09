
from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class JoinGameRequest(Request):

    def __init__(self,):
        Request.__init__(self, RequestType.join_game)

    def decode_dct(self, dct):

        if self.request_of_type(dct):

            join_game_request = JoinGameRequest()
            return join_game_request

        raise TypeError(f"'{self.__class__.__name__}' could not be decoded")
