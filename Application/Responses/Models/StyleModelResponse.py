

from PythonWebSocketsGame.Application.Responses.Response import Response


class StyleModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.display = None
        self.available = False

    @staticmethod
    def type_name():
        return 'style_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, StyleModelResponse):
            return complex_object.__dict__
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
