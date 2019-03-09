
from PythonWebSocketsGame.Tests.Application.TheTest import TheTest

from PythonWebSocketsGame.Application.Server.WsGameResponseMessages import WsGameResponseMessages

from PythonWebSocketsGame.Application.Requests.Request import RequestType

class TestWsGameMessages(TheTest):

    messages = WsGameResponseMessages()

    def test_make_action_failure_message(self):
        print(self.messages.make_action_failure_message())

    def test_make_game_draw_message(self):
        print(self.messages.make_game_draw_message())

    def test_make_game_over_message(self):
        print(self.messages.make_game_over_message())

    def test_make_game_state_message(self):
        game = self.mock_ws_game()
        print(self.messages.make_game_state_message(game))

    def test_make_new_lobby_message(self):
        client = self.mock_ws_client()
        lobby = self.mock_game_lobby(2, 3, client)
        print(self.messages.make_new_lobby_message(lobby))

    def test_make_player_entry_message(self):
        client = self.mock_ws_client()
        print(self.messages.make_player_entry_message(client))

    def test_make_player_exit_message(self):
        client = self.mock_ws_client()
        print(self.messages.make_player_exit_message(client))

    def test_make_player_lobby_entry_message(self):
        client = self.mock_ws_client()
        print(self.messages.make_player_lobby_entry_message(client))

    def test_make_player_lobby_exit_message(self):
        client = self.mock_ws_client()
        print(self.messages.make_player_lobby_exit_message(client))

    def test_make_player_turn_message(self):
        client = self.mock_ws_client()
        print(self.messages.make_player_turn_message(client))

    def test_make_player_victory_message(self):
        client = self.mock_ws_client()
        print(self.messages.make_player_victory_message(client))

    def test_make_server_state_message(self):
        number_of_connection = 5
        number_of_games = 6
        print(self.messages.make_server_state_message(number_of_connection, number_of_games))

    def test_make_you_have_exited_game_message(self):
        print(self.messages.make_you_have_exited_game_message())

    def test_make_you_have_exited_lobby_message(self):
        print(self.messages.make_you_have_exited_lobby_message())

    def test_make_you_have_joined_lobby_message(self):
        print(self.messages.make_you_have_joined_lobby_message())

    def test_make_you_have_selected_area_game_message(self):
        print(self.messages.make_you_have_selected_area_game_message())

    def test_make_your_turn_message(self):
        print(self.messages.make_your_turn_message())
