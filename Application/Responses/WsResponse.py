
from abc import abstractmethod

from PythonWebSocketsGame.Application.Responses.Response import Response


class WsResponse(Response):

    def __init__(self, action):
        super().__init__()
        self.response_action = action

    @staticmethod
    @abstractmethod
    def encode_complex(complex_object):
        pass

    @staticmethod
    def response_action_type():
        return 'response_action'
