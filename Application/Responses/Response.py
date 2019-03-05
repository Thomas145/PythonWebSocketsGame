
from abc import abstractmethod


class Response:

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def type_name():
        pass

    @staticmethod
    @abstractmethod
    def encode_complex(complex_object):
        pass

    @staticmethod
    def format_time(time):
        return time.strftime('%Y-%m-%d %H:%M:%S')
