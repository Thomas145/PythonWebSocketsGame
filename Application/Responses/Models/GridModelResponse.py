

from PythonWebSocketsGame.Application.Responses.Response import Response


class GridModelResponse(Response):

    def __init__(self):
        self.rows = []

    @staticmethod
    def type_name():
        return 'grid_area_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, GridModelResponse):

            return [grid_area.encode_complex(grid_area) for grid_area in complex_object.rows]

        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
