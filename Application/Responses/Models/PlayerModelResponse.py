

from PythonWebSocketsGame.Application.Responses.Response import Response


class PlayerModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.player_name = None

    def from_player(self, player):
        self.player_name = player.get_player_name()
        return self


    @staticmethod
    def type_name():
        return 'player_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, PlayerModelResponse):
            return complex_object.__dict__
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
