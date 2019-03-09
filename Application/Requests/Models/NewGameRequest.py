
from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class NewGameRequest(Request):

    def __init__(self):
        Request.__init__(self, RequestType.new_game)
        self.number_of_players = None
        self.size_of_game = None

    def decode_dct(self, dct):

        if self.request_of_type(dct):

            new_game_request = NewGameRequest()
            new_game_request.number_of_players = int(dct['number_of_players'])
            new_game_request.size_of_game = int(dct['size_of_game'])

            return new_game_request

        raise TypeError(f"'{self.__class__.__name__}' could not be decoded")
