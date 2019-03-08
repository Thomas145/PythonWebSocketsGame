
from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class SelectGridAreaMessage(Request):

    def __init__(self, *args, **kwargs):
        Request.__init__(self, *args, **kwargs)

        self.grid_column = None
        self.grid_row = None

    @staticmethod
    def object_hook(dct):

        if 'request' in dct and RequestType.select_area.value == dct['request']:

            select_grid_area_message = SelectGridAreaMessage()
            select_grid_area_message.grid_column_position = int(dct['grid_column'])
            select_grid_area_message.grid_row_position = int(dct['grid_row'])

            return select_grid_area_message

        return dct
