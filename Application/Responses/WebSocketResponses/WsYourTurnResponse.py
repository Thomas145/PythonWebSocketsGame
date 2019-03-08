
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponseType


class WsYourTurnResponse(WsResponse):

    def __init__(self):
        super().__init__('your_turn')

    @staticmethod
    def type_name():
        return WsResponseType.ws_your_turn.value

    @staticmethod
    def encode_complex(complex_object):

        if isinstance(complex_object, WsYourTurnResponse):

            return {
                complex_object.response_action_type(): complex_object.type_name(),
            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
