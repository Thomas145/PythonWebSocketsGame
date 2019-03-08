
from enum import Enum

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


class WsResponseType(Enum):
    ws_client_response = 'ws_client_response',
    ws_new_game = 'ws_new_game',
    ws_game_draw_response = 'ws_game_draw_response',
    ws_player_entry = 'ws_player_entry',
    ws_player_exit = 'ws_player_exit',
    ws_player_victory = 'ws_player_victory',
    ws_server_state = 'ws_server_state',
    ws_your_turn = 'ws_your_turn',
    ws_action_failure = 'ws_action_failure',
    ws_player_entry_lobby = 'ws_player_entry_lobby',
    ws_player_exit_lobby = 'ws_player_exit_lobby'
