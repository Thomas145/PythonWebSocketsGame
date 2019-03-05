

from PythonWebSocketsGame.Application.Responses.Response import Response
from PythonWebSocketsGame.Application.Responses.Models.PlayerModelResponse import PlayerModelResponse


class PlayersModelResponse(Response):

    def __init__(self):
        self.players = []

    def number_of_players(self):
        if self.players is None:
            return 0
        else:
            return len(self.players)

    def from_players(self, players):
        for player in players:
            if player.is_assigned():
                self.players.append(PlayerModelResponse().from_player(player))

    @staticmethod
    def type_name():
        return 'players'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, PlayersModelResponse):
            return [player.__dict__ for player in complex_object.players]
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
