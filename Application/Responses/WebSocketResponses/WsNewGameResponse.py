
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse


class WsNewGameResponse(WsResponse):

    def __init__(self):
        super().__init__('server_state')
        self.awaiting_players = None
        self.players = None

    @staticmethod
    def type_name():
        return 'ws_new_game'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, WsNewGameResponse):

            return {

                complex_object.awaiting_players.type_name():
                    complex_object.awaiting_players.encode_complex(complex_object.awaiting_players),

                complex_object.players.type_name():
                    complex_object.players.encode_complex(complex_object.players)

            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

