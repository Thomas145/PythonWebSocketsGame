
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
    ws_new_lobby = 'ws_new_lobby',

    ws_game_start = 'ws_game_start',
    ws_game_draw = 'ws_game_draw',
    ws_game_over = 'ws_game_over',
    ws_game_state = 'ws_game_state',

    ws_server_state = 'ws_server_state',

    ws_player_exit_game = 'ws_player_exit_game ',
    ws_player_entry_game = 'ws_player_entry_game ',

    ws_player_entry_lobby = 'ws_player_entry_lobby',
    ws_player_exit_lobby = 'ws_player_exit_lobby',

    ws_player_victory = 'ws_player_victory',
    ws_player_turn = 'ws_player_turn',

    ws_selected_area = 'ws_selected_area',

    ws_your_turn = 'ws_your_turn',

    ws_you_selected_area = 'ws_you_selected_area',
    ws_you_join_lobby = 'ws_you_join_lobby',
    ws_you_join_game = 'ws_you_join_game',
    ws_you_exit_lobby = 'ws_you_exit_lobby',
    ws_you_exit_game = 'ws_you_exit_game',

    ws_action_failure = 'ws_action_failure'


