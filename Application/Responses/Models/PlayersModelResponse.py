

from PythonWebSocketsGame.Application.Responses.Response import Response
from PythonWebSocketsGame.Application.Responses.Models.PlayerModelResponse import PlayerModelResponse


class PlayersModelResponse(Response):

    def __init__(self):
        self.players = []

    @staticmethod
    def type_name():
        return 'players'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, PlayersModelResponse):

            return [player.encode_complex(player) for player in complex_object.players]

        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
