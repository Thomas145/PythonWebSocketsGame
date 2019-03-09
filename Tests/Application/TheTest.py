
import unittest
from inspect import getmembers, isfunction

from PythonWebSocketsGame.Application.Server.Model.WebSocketClient import WebSocketClient

from PythonWebSocketsGame.Application.GameLobby.GameLobby import GameLobby

from PythonWebSocketsGame.Application.Games.Game import Game


class TheTest(unittest.TestCase):

    def test_init(self):
        self.assertTrue(True)

    @staticmethod
    def print_functions(member):
        functions_list = [o for o in getmembers(member) if isfunction(o[1])]
        for f in functions_list:
            print(f[0])

    def not_implemented(self):
        self.assertTrue(False, 'Not Implemented')

    @staticmethod
    def mock_ws_client():
        client = WebSocketClient(object())
        return client

    @staticmethod
    def mock_game_lobby(num_o_players, size_o_game, client):
        lobby = GameLobby(num_o_players, size_o_game, client)
        return lobby

    def mock_ws_game(self):
        lobby = self.mock_game_lobby(2, 3, self.mock_ws_client())
        while not lobby.is_lobby_full():
            lobby.join_game_lobby(self.mock_ws_client())

        game = Game(lobby)
        return game


if __name__ == '__main__':
    unittest.main()
