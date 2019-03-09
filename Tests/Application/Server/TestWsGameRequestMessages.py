import json

from PythonWebSocketsGame.Tests.Application.TheTest import TheTest

from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest
from PythonWebSocketsGame.Application.Requests.Models.JoinGameRequest import JoinGameRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitLobbyRequest import ExitLobbyRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitGameRequest import ExitGameRequest
from PythonWebSocketsGame.Application.Requests.Models.SelectAreaRequest import SelectAreaRequest
from PythonWebSocketsGame.Application.Server.WsGameRequestMessages import WsGameRequestMessages


class TestWsGameRequestMessages(TheTest):

    messages = WsGameRequestMessages()

    def test_unwrap_join_game_request(self):
        request_body = JoinGameRequest()

        json_str = json.dumps(request_body.__dict__)
        json_dct = json.loads(json_str)

        self.messages.unwrap_join_game_request(json_dct)

    def test_unwrap_exit_lobby_request(self):
        request_body = ExitLobbyRequest()

        json_str = json.dumps(request_body.__dict__)
        json_dct = json.loads(json_str)

        self.messages.unwrap_exit_lobby_request(json_dct)

    def test_unwrap_exit_game_request(self):
        request_body = ExitGameRequest()

        json_str = json.dumps(request_body.__dict__)
        json_dct = json.loads(json_str)

        self.messages.unwrap_exit_game_request(json_dct)

    def test_unwrap_select_area_request(self):
        request_body = SelectAreaRequest()
        request_body.grid_column = "1"
        request_body.grid_row = "2"

        json_str = json.dumps(request_body.__dict__)
        json_dct = json.loads(json_str)

        self.messages.unwrap_select_area_request(json_dct)

    def test_unwrap_new_game_request(self):

        request_body = NewGameRequest()
        request_body.number_of_players = "3"
        request_body.size_of_game = "2"

        json_str = json.dumps(request_body.__dict__)
        json_dct = json.loads(json_str)

        self.messages.unwrap_new_game_request(json_dct)
