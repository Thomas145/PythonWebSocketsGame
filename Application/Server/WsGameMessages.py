
import json

# Response Models
from PythonWebSocketsGame.Application.Responses.Models.ServerStateModelResponse import ServerStateModelResponse


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

from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsNewGameResponse import WsNewGameResponse

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


class WsGameMessages:

    @staticmethod
    def make_new_lobby_message(lobby):
        ws_new_lobby_response = WsNewLobbyResponse()
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
    def make_you_have_joined_lobby_message(client):
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
        _json = json.dumps(ws_you_have_selected_area_response, default=WsYouHaveExitedGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_game_state_message(game):
        ws_game_state_response = WsGameStateResponse()
        _json = json.dumps(ws_game_state_response, default=WsGameStateResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_turn_message(client):
        ws_game_player_turn_response = WsGamePlayerTurnResponse()
        _json = json.dumps(ws_game_player_turn_response, default=WsNewGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_your_turn_message():
        ws_your_turn_response = WsYourTurnResponse()
        _json = json.dumps(ws_your_turn_response, default=WsYourTurnResponse.encode_complex)
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
        ws_player_exit_response = WsPlayerExitGameResponse()
        _json = json.dumps(ws_player_exit_response, default=WsPlayerExitGameResponse.encode_complex)
        return _json

    @staticmethod
    def make_player_entry_message(client):
        ws_player_entry_response = WsPlayerEntryGameResponse()
        _json = json.dumps(ws_player_entry_response, default=WsPlayerEntryGameResponse.encode_complex)
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
