

from PythonWebSocketsGame.Application.Responses.Response import Response


class GridColumnModelResponse(Response):

    def __init__(self):
        self.columns = []

    @staticmethod
    def type_name():
        return 'grid_area_state'

    @staticmethod
    def encode_complex(complex_object):
        if isinstance(complex_object, GridColumnModelResponse):

            return [grid_model.encode_complex(grid_model) for grid_model in complex_object.columns]

        else:
            type_name = complex_object.__class__.__name__
            raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
