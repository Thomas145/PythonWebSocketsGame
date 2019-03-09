
from abc import abstractmethod
from enum import Enum


class Request:
    def __init__(self, request):
        self.request = request.value[0]

    @abstractmethod
    def decode_dct(self, dct):
        pass

    def request_of_type(self, dct):
        r = 'request' in dct
        s = self.request == dct['request']
        if r and s:
            return True
        return False


class RequestType(Enum):
    new_game = 'new_game',
    exit_lobby = 'exit_lobby',
    join_game = 'join_game',
    exit_game = 'exit_game',
    select_area = 'select_area',
    select_area1 = 1

    @staticmethod
    def from_str(label):

        for r_type in RequestType:

            if label == r_type.name:

                return r_type

        raise NotImplementedError
