
import json

# Response Models
from PythonWebSocketsGame.Application.Responses.Models.ServerStateModelResponse import ServerStateModelResponse
from PythonWebSocketsGame.Application.Responses.Models.ClientDetailsModelResponse import ClientDetailsModelResponse


# Ws Response Wrappers
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsNewGameResponse import WsNewGameResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsServerStateResponse import WsServerStateResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsClientResponse import WsClientResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerVictoryResponse import WsPlayerVictoryResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsYourTurnResponse import WsYourTurnResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerEntryResponse import WsPlayerEntryResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsGamePlayerTurnResponse \
    import WsGamePlayerTurnResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerExitResponse import WsPlayerExitResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsNewGameResponse import WsNewGameResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsGameDrawResponse import WsGameDrawResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsClientResponse import WsClientResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsActionFailureResponse \
    import WsActionFailureResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerEnterLobbyResponse \
    import WsPlayerEnterLobbyResponse

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsPlayerExitLobbyResponse \
    import WsPlayerExitLobbyResponse


class WsGameMessages:

    @staticmethod
    def make_new_lobby_message(lobby):
        pass

    @staticmethod
    def make_action_failure_message():
        ws_action_failure_response = WsActionFailureResponse()

        return ws_action_failure_response

    @staticmethod
    def make_game_over_message():
        pass

    @staticmethod
    def make_you_have_joined_lobby_message(client):
        pass

    @staticmethod
    def make_you_have_exited_lobby_message():
        pass

    @staticmethod
    def make_you_have_exited_game_message():
        pass

    @staticmethod
    def make_you_have_selected_area_game_message():
        pass

    @staticmethod
    def make_game_state_message(game):
        pass

    @staticmethod
    def make_player_turn_message(client):
        ws_game_player_turn_response = WsGamePlayerTurnResponse()
        _json = json.dumps(ws_game_player_turn_response, default=WsNewGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_your_turn_message():
        ws_new_game_response = WsNewGameResponse()
        _json = json.dumps(ws_new_game_response, default=WsNewGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_client_detail_message(client):

        client_details_model_response = ClientDetailsModelResponse()
        client_details_model_response.player_name = client.get_client_name()
        client_details_model_response.id = client.get_id_string()
        client_details_model_response.connection_time = \
            client_details_model_response.format_time(client.connection_time)

        ws_client_response = WsClientResponse()
        ws_client_response.client_details = client_details_model_response

        _json = json.dumps(ws_client_response, default=WsClientResponse.encode_complex)

        return _json

    @staticmethod
    def make_server_state_message(number_of_connections, number_of_games):
        server_state = ServerStateModelResponse()
        server_state.number_of_active_players = number_of_connections()
        server_state.number_of_active_games = number_of_games()

        ws_server_state = WsServerStateResponse()
        ws_server_state.server_state = server_state

        _json = json.dumps(ws_server_state, default=WsServerStateResponse.encode_complex)

        return _json

    @staticmethod
    def make_new_game_response():
        ws_new_game_response = WsNewGameResponse()
        _json = json.dumps(ws_new_game_response, default=WsNewGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_game_draw_message():
        ws_game_draw_response = WsGameDrawResponse()
        _json = json.dumps(ws_game_draw_response, default=WsGameDrawResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_exit_message(client):
        ws_player_exit_response = WsPlayerExitResponse()
        _json = json.dumps(ws_player_exit_response, default=WsPlayerExitResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_entry_message(client):
        ws_player_entry_response = WsPlayerEntryResponse()

        _json = json.dumps(ws_player_entry_response, default=WsPlayerEntryResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_victory_message(client):
        ws_player_victory_response = WsPlayerVictoryResponse()

        _json = json.dumps(ws_player_victory_response, default=WsPlayerVictoryResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_lobby_exit_message(client):
        ws_player_exit_lobby_response = WsPlayerExitLobbyResponse()

        _json = json.dumps(ws_player_exit_lobby_response, default=WsPlayerExitLobbyResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_lobby_entry_message(client):
        ws_player_enter_lobby_response = WsPlayerEnterLobbyResponse()

        _json = json.dumps(ws_player_enter_lobby_response, default=WsPlayerEnterLobbyResponse.encode_complex)

        return _json
