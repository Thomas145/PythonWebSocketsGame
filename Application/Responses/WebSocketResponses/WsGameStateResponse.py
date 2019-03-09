

from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponseType


class WsGameStateResponse(WsResponse):

    def __init__(self, players, grid):
        super().__init__('game_state')
        self.players = players
        self.grid = grid

    @staticmethod
    def type_name():
        return WsResponseType.ws_game_state.value

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, WsGameStateResponse):

            return {

                complex_object.response_action_type():
                    complex_object.type_name(),

                complex_object.players.type_name():
                    complex_object.players.encode_complex(complex_object.players),

                complex_object.grid.type_name():
                    complex_object.grid.encode_complex(complex_object.grid)

            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


