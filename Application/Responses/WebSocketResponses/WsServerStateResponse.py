
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponseType


class WsServerStateResponse(WsResponse):

    def __init__(self):
        super().__init__('server_state')
        self.server_state = None

    @staticmethod
    def type_name():
        return WsResponseType.ws_server_state.value

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, WsServerStateResponse):

            return {

                complex_object.response_action_type(): complex_object.type_name(),

                complex_object.server_state.type_name():
                    complex_object.server_state.encode_complex(complex_object.server_state)
            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
