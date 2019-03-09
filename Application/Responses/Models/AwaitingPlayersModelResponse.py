
from PythonWebSocketsGame.Application.Responses.Response import Response


class AwaitingPlayersModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.awaiting_players = None

    @staticmethod
    def type_name():
        return 'awaiting'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, AwaitingPlayersModelResponse):
            return complex_object.__dict__
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
