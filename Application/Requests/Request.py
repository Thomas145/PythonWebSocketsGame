
import json

from abc import abstractmethod
from enum import Enum


class Request(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    @staticmethod
    @abstractmethod
    def object_hook(dct):
        pass


class RequestType(Enum):
    new_game = 'new_game',
    exit_lobby = 'exit_lobby',
    join_game = 'join_game',
    exit_game = 'exit_game',
    select_area = 'select_area',
