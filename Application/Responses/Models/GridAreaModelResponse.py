
from PythonWebSocketsGame.Application.Responses.Response import Response


class GridAreaModelResponse(Response):

    def __init__(self):
        super().__init__()
        self.style = None
        self.grid_reference = None

    @staticmethod
    def type_name():
        return 'grid_area_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, GridAreaModelResponse):
            return complex_object.__dict__
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
