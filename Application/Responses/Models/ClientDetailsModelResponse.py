
from PythonWebSocketsGame.Application.Responses.Response import Response


class ClientDetailsModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.id = None
        self.player_name = None
        self.connection_time = None

    @staticmethod
    def type_name():
        return 'client_details'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, ClientDetailsModelResponse):
            return complex_object.__dict__
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
