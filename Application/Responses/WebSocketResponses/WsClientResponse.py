
from PythonWebSocketsGame.Application.Responses.WsResponse import WsResponse


class WsClientResponse(WsResponse):

    def __init__(self):
        super().__init__('client_details')
        self.client_details = None

    @staticmethod
    def type_name():
        return 'ws_client_details'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, WsClientResponse):

            return {

                complex_object.response_action_type(): complex_object.type_name(),

                complex_object.client_details.type_name():
                    complex_object.client_details.encode_complex(complex_object.client_details)
            }

        else:

            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

