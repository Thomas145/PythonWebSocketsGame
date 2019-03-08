
from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class NewGameRequest(Request):

    def __init__(self, *args, **kwargs):
        Request.__init__(self, *args, **kwargs)

        self.number_of_players = None
        self.size_of_game = None

    @staticmethod
    def object_hook(dct):

        if 'request' in dct and RequestType.new_game.value == dct['request']:

            new_game_request = NewGameRequest()
            new_game_request.number_of_players = int(dct['number_of_players'])
            new_game_request.size_of_game = int(dct['size_of_game'])

            return new_game_request

        return dct
