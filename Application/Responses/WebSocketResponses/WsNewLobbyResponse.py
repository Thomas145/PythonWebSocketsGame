
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponseType


class WsNewLobbyResponse(WsResponse):

    def __init__(self):
        super().__init__('server_state')

    @staticmethod
    def type_name():
        return WsResponseType.ws_new_lobby.value

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, WsNewLobbyResponse):

            return {
                complex_object.response_action_type(): complex_object.type_name(),
            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")