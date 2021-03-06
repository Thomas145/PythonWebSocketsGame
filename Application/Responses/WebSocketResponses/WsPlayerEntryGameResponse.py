

from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponseType


class WsPlayerEntryGameResponse(WsResponse):

    def __init__(self, player_model_response):
        super().__init__('player_entry')
        self.player = player_model_response

    @staticmethod
    def type_name():
        return WsResponseType.ws_player_entry_game.value

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, WsPlayerEntryGameResponse):

            return {

                complex_object.response_action_type(): complex_object.type_name(),

                complex_object.player.type_name():
                    complex_object.player.encode_complex(complex_object.player)

            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


