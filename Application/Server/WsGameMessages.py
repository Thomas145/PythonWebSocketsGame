
import json

# Response Models
from PythonWebSocketsGame.Application.Responses.Models.PlayersModelResponse import PlayersModelResponse
from PythonWebSocketsGame.Application.Responses.Models.AwaitingPlayersModelResponse import AwaitingPlayersModelResponse
from PythonWebSocketsGame.Application.Responses.Models.ServerStateModelResponse import ServerStateModelResponse
from PythonWebSocketsGame.Application.Responses.Models.ClientDetailsModelResponse import ClientDetailsModelResponse


# Ws Response Wrappers
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsNewGameResponse import WsNewGameResponse
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsServerStateResponse import WsServerStateResponse
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsClientResponse import WsClientResponse

class WsGameMessages:




    def make_client_detail_message(self, connection):
        socket_client = self.CONNECTION_POOL[connection]

        client_details_model_response = ClientDetailsModelResponse()
        client_details_model_response.player_name = socket_client.get_client_name()
        client_details_model_response.id = socket_client.get_id_string()
        client_details_model_response.connection_time = \
            client_details_model_response.format_time(socket_client.connection_time)

        ws_client_response = WsClientResponse()
        ws_client_response.client_details = client_details_model_response

        _json = json.dumps(ws_client_response, default=WsClientResponse.encode_complex)

        return _json

    def make_server_state_message(self):
        server_state = ServerStateModelResponse()
        server_state.number_of_active_players = self.number_of_connections()
        server_state.number_of_active_games = self.number_of_games()

        ws_server_state = WsServerStateResponse()
        ws_server_state.server_state = server_state

        _json = json.dumps(ws_server_state, default=WsServerStateResponse.encode_complex)

        return _json


    def make_new_game_response(self):
        ws_new_game_response = WsNewGameResponse()
        _json = json.dumps(ws_new_game_response, default=WsNewGameResponse.encode_complex)
        return _json

    def make_game_draw_message(self):
        ws_game_draw_response = WsGameDrawResponse()
        _json = json.dumps(ws_game_draw_response, default=WsGameDrawResponse.encode_complex)
        return _json

    def make_player_exit_message(self, player):
        ws_player_exit_response = WsPlayerExitResponse()
        _json = json.dumps(ws_player_exit_response, default=WsPlayerExitResponse.encode_complex)
        return _json

    def make_player_entry_message(self, player):
        ws_player_entry_response = WsPlayerEntryResponse()

        _json = json.dumps(ws_player_entry_response, default=WsPlayerEntryResponse.encode_complex)
        return _json

    def make_player_victory_message(self, player):
        ws_player_victory_response = WsPlayerVictoryResponse()

        _json = json.dumps(ws_player_victory_response, default=WsPlayerVictoryResponse.encode_complex)
        return _json



    def make_player_lobby_exit_message(self, client):
        ws_player_exit_lobby_response = WsPlayerExitLobbyResponse()

        _json = json.dumps(ws_player_exit_lobby_response, default=WsPlayerExitLobbyResponse.encode_complex)
        return _json

    def make_player_lobby_entry_message(self, client):
        ws_player_enter_lobby_response = WsPlayerEnterLobbyResponse()

        _json = json.dumps(ws_player_enter_lobby_response, default=WsPlayerEnterLobbyResponse.encode_complex)

        return _json
