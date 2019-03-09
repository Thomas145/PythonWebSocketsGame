
import json

# Response Models
from PythonWebSocketsGame.Application.Responses.Models.ServerStateModelResponse import ServerStateModelResponse

from PythonWebSocketsGame.Application.Responses.Models.PlayerModelResponse import PlayerModelResponse

from PythonWebSocketsGame.Application.Responses.Models.PlayersModelResponse import PlayersModelResponse

from PythonWebSocketsGame.Application.Responses.Models.LobbyModelResponse import LobbyModelResponse

from PythonWebSocketsGame.Application.Responses.Models.AwaitingPlayersModelResponse import AwaitingPlayersModelResponse

from PythonWebSocketsGame.Application.Responses.Models.GridModelResponse import GridModelResponse

from PythonWebSocketsGame.Application.Responses.Models.GridRowsModelResponse import GridRowsModelResponse

from PythonWebSocketsGame.Application.Responses.Models.GridAreaModelResponse import GridAreaModelResponse

# Ws Response Wrappers

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsServerStateResponse import WsServerStateResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerVictoryResponse \
    import WsPlayerVictoryResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsYourTurnResponse import WsYourTurnResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerEntryGameResponse \
    import WsPlayerEntryGameResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsGamePlayerTurnResponse \
    import WsGamePlayerTurnResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerExitGameResponse \
    import WsPlayerExitGameResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsGameDrawResponse import WsGameDrawResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsActionFailureResponse \
    import WsActionFailureResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerEnterLobbyResponse \
    import WsPlayerEnterLobbyResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerExitLobbyResponse \
    import WsPlayerExitLobbyResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsGameOverResponse \
    import WsGameOverResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsNewLobbyResponse \
    import WsNewLobbyResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsYouHaveJoinedLobbyResponse \
    import WsYouHaveJoinedLobbyResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsYouHaveExitedLobbyResponse \
    import WsYouHaveExitedLobbyResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsYouHaveExitedGameResponse \
    import WsYouHaveExitedGameResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsYouHaveSelectedAreaResponse \
    import WsYouHaveSelectedAreaResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsGameStateResponse \
    import WsGameStateResponse


class WsGameResponseMessages:

    @staticmethod
    def make_player_model_response(client):
        player_model_response = PlayerModelResponse()
        player_model_response.player_name = client.get_client_name()
        return player_model_response

    def make_players_model_response(self, clients):
        players_model_response = PlayersModelResponse()

        for key, client in clients.items():
            players_model_response.players.append(self.make_player_model_response(client))

        return players_model_response

    def make_game_players_model_response(self, players):
        players_model_response = PlayersModelResponse()

        for player in players:
            players_model_response.players.append(self.make_player_model_response(player.client))

        return players_model_response

    @staticmethod
    def make_game_grid_area_model_response(row_position, column_position, grid_area):

        grid_area_model_response = GridAreaModelResponse()
        grid_area_model_response.content = grid_area.grid_area_style().display()
        grid_area_model_response.selected = grid_area.grid_area_style().selected()
        grid_area_model_response.grid_row = row_position
        grid_area_model_response.grid_column = column_position

        return grid_area_model_response

    def make_game_grid_row_model_response(self, row_position, row):
        columns = []

        for column_position, grid_area in enumerate(row.column):
            grid_area_model_response = self.make_game_grid_area_model_response(row_position, column_position, grid_area)
            columns.append(grid_area_model_response)

        return GridRowsModelResponse(columns)

    def make_game_grid_model_response(self, grid):
        rows = []

        for row_position, row in enumerate(grid.row):
            grid_row_model_response = self.make_game_grid_row_model_response(row_position, row)
            rows.append(grid_row_model_response)

        return GridModelResponse(rows)

    @staticmethod
    def make_awaiting_players_model_response(awaiting):
        awaiting_players_model_response = AwaitingPlayersModelResponse()
        awaiting_players_model_response.awaiting_players = awaiting
        return awaiting_players_model_response

    def make_lobby_model_response(self, lobby):

        players_model_response = self.make_players_model_response(lobby.clients_in_lobby)
        awaiting_model_response = self.make_awaiting_players_model_response(lobby.awaiting_number_of_players())

        lobby_model_response = LobbyModelResponse()
        lobby_model_response.players = players_model_response
        lobby_model_response.awaiting_players = awaiting_model_response

        return lobby_model_response

    def make_new_lobby_message(self, lobby):
        lobby_response = self.make_lobby_model_response(lobby)
        ws_new_lobby_response = WsNewLobbyResponse(lobby_response)
        _json = json.dumps(ws_new_lobby_response, default=WsNewLobbyResponse.encode_complex)
        return _json

    @staticmethod
    def make_action_failure_message():
        ws_action_failure_response = WsActionFailureResponse()
        _json = json.dumps(ws_action_failure_response, default=WsActionFailureResponse.encode_complex)
        return _json

    @staticmethod
    def make_game_over_message():
        ws_game_over_response = WsGameOverResponse()
        _json = json.dumps(ws_game_over_response, default=WsGameOverResponse.encode_complex)
        return _json

    @staticmethod
    def make_you_have_joined_lobby_message():
        ws_you_have_joined_lobby_response = WsYouHaveJoinedLobbyResponse()
        _json = json.dumps(ws_you_have_joined_lobby_response, default=WsYouHaveJoinedLobbyResponse.encode_complex)
        return _json

    @staticmethod
    def make_you_have_exited_lobby_message():
        ws_you_have_exited_lobby_response = WsYouHaveExitedLobbyResponse()
        _json = json.dumps(ws_you_have_exited_lobby_response, default=WsYouHaveExitedLobbyResponse.encode_complex)
        return _json

    @staticmethod
    def make_you_have_exited_game_message():
        ws_you_have_exited_game_response = WsYouHaveExitedGameResponse()
        _json = json.dumps(ws_you_have_exited_game_response, default=WsYouHaveExitedGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_you_have_selected_area_game_message():
        ws_you_have_selected_area_response = WsYouHaveSelectedAreaResponse()
        _json = json.dumps(ws_you_have_selected_area_response, default=WsYouHaveSelectedAreaResponse.encode_complex)
        return _json

    def make_game_state_message(self, game):
        players_response = self.make_game_players_model_response(game.players)

        grid_response = self.make_game_grid_model_response(game.grid)
        ws_game_state_response = WsGameStateResponse(players_response, grid_response)
        _json = json.dumps(ws_game_state_response, default=WsGameStateResponse.encode_complex)
        return _json

    def make_player_turn_message(self, client):
        player_response = self.make_player_model_response(client)
        ws_game_player_turn_response = WsGamePlayerTurnResponse(player_response)
        _json = json.dumps(ws_game_player_turn_response, default=WsGamePlayerTurnResponse.encode_complex)

        return _json

    @staticmethod
    def make_your_turn_message():
        ws_your_turn_response = WsYourTurnResponse()
        _json = json.dumps(ws_your_turn_response, default=WsYourTurnResponse.encode_complex)
        return _json

    @staticmethod
    def make_server_state_message(number_of_connections, number_of_games):
        server_state = ServerStateModelResponse()
        server_state.number_of_active_players = number_of_connections
        server_state.number_of_active_games = number_of_games

        ws_server_state = WsServerStateResponse()
        ws_server_state.server_state = server_state

        _json = json.dumps(ws_server_state, default=WsServerStateResponse.encode_complex)

        return _json

    @staticmethod
    def make_game_draw_message():
        ws_game_draw_response = WsGameDrawResponse()
        _json = json.dumps(ws_game_draw_response, default=WsGameDrawResponse.encode_complex)
        return _json

    def make_player_exit_message(self, client):
        player_response = self.make_player_model_response(client)
        ws_player_exit_response = WsPlayerExitGameResponse(player_response)
        _json = json.dumps(ws_player_exit_response, default=WsPlayerExitGameResponse.encode_complex)
        return _json

    def make_player_entry_message(self, client):
        player_response = self.make_player_model_response(client)
        ws_player_entry_response = WsPlayerEntryGameResponse(player_response)
        _json = json.dumps(ws_player_entry_response, default=WsPlayerEntryGameResponse.encode_complex)
        return _json

    def make_player_victory_message(self, client):
        player_response = self.make_player_model_response(client)

        ws_player_victory_response = WsPlayerVictoryResponse(player_response)

        _json = json.dumps(ws_player_victory_response, default=WsPlayerVictoryResponse.encode_complex)

        return _json

    def make_player_lobby_exit_message(self, client):
        player_response = self.make_player_model_response(client)
        ws_player_exit_lobby_response = WsPlayerExitLobbyResponse(player_response)
        _json = json.dumps(ws_player_exit_lobby_response, default=WsPlayerExitLobbyResponse.encode_complex)
        return _json

    def make_player_lobby_entry_message(self, client):
        player_response = self.make_player_model_response(client)
        ws_player_enter_lobby_response = WsPlayerEnterLobbyResponse(player_response)
        _json = json.dumps(ws_player_enter_lobby_response, default=WsPlayerEnterLobbyResponse.encode_complex)
        return _json
