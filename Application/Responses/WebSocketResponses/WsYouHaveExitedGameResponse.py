
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponseType


class WsYouHaveExitedGameResponse(WsResponse):

    def __init__(self):
        super().__init__('exit_game')

    @staticmethod
    def type_name():
        return WsResponseType.ws_you_exit_game.value

    @staticmethod
    def encode_complex(complex_object):

        if isinstance(complex_object, WsYouHaveExitedGameResponse):

            return {
                complex_object.response_action_type(): complex_object.type_name(),
            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
