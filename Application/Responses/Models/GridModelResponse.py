

from PythonWebSocketsGame.Application.Responses.Response import Response


class GridModelResponse(Response):

    def __init__(self, rows):
        self.rows = rows

    @staticmethod
    def type_name():
        return 'grid'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, GridModelResponse):
            return [row.encode_complex(row) for row in complex_object.rows]
        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
