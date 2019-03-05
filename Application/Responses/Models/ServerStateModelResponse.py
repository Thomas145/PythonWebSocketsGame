
from PythonWebSocketsGame.Application.Responses.Response import Response


class ServerStateModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.number_of_active_players = None
        self.number_of_active_games = None

    @staticmethod
    def type_name():
        return 'server_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, ServerStateModelResponse):
            return complex_object.__dict__
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
