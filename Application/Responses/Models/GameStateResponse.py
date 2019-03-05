
from PythonWebSocketsGame.Application.Responses.Response import Response


class GameStateModelResponse(Response):

    def __init__(self, players, active_player, grid_area):

        self.players = players
        self.player_active = active_player
        self.grid_area = grid_area

    @staticmethod
    def type_name():
        return 'game_state'

    @staticmethod
    def encode_complex(complex_object):

        if isinstance(complex_object, GameStateModelResponse):

            return {

                complex_object.players.type_name():
                    complex_object.players.encode_complex(complex_object.players),

                complex_object.grid_area.type_name():
                    complex_object.grid_area.encode_complex(complex_object.grid_area),

                complex_object.player_active.type_name():
                    complex_object.player_active.encode_complex(complex_object.player_active)

            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
