
from PythonWebSocketsGame.Application.Responses.Response import Response


class LobbyModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.players = None
        self.awaiting_players = None

    @staticmethod
    def type_name():
        return 'lobby_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, LobbyModelResponse):

            return {

                complex_object.players.type_name():
                    complex_object.players.encode_complex(complex_object.players),

                complex_object.awaiting_players.type_name():
                    complex_object.awaiting_players.encode_complex(complex_object.awaiting_players),

            }

        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
