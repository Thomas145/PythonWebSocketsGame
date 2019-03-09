
from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest

from PythonWebSocketsGame.Application.Requests.Models.JoinGameRequest import JoinGameRequest

from PythonWebSocketsGame.Application.Requests.Models.ExitGameRequest import ExitGameRequest

from PythonWebSocketsGame.Application.Requests.Models.ExitLobbyRequest import ExitLobbyRequest

from PythonWebSocketsGame.Application.Requests.Models.SelectAreaRequest import SelectAreaRequest


class WsGameRequestMessages:

    @staticmethod
    def unwrap(json_as_dct, clazz):
        decoded_clazz = clazz.decode_dct(json_as_dct)
        return decoded_clazz

    def unwrap_new_game_request(self, json_as_dct):
        new_game_request = self.unwrap(json_as_dct, NewGameRequest())
        return new_game_request

    def unwrap_join_game_request(self, json_as_dct):
        new_game_request = self.unwrap(json_as_dct, JoinGameRequest())
        return new_game_request

    def unwrap_exit_lobby_request(self, json_as_dct):
        exit_lobby_request = self.unwrap(json_as_dct, ExitLobbyRequest())
        return exit_lobby_request

    def unwrap_exit_game_request(self, json_as_dct):
        exit_game_request = self.unwrap(json_as_dct, ExitGameRequest())
        return exit_game_request

    def unwrap_select_area_request(self, json_as_dct):
        select_area_request = self.unwrap(json_as_dct, SelectAreaRequest())
        return select_area_request
