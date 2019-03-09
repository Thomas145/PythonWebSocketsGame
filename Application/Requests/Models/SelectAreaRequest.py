
from PythonWebSocketsGame.Application.Requests.Request import Request
from PythonWebSocketsGame.Application.Requests.Request import RequestType


class SelectAreaRequest(Request):

    def __init__(self):
        Request.__init__(self, RequestType.select_area)

        self.grid_column = None
        self.grid_row = None

    def decode_dct(self, dct):

        if self.request_of_type(dct):

            select_area_request = SelectAreaRequest()
            select_area_request.grid_column = int(dct['grid_column'])
            select_area_request.grid_row = int(dct['grid_row'])

            return select_area_request

        raise TypeError(f"'{self.__class__.__name__}' could not be decoded")
