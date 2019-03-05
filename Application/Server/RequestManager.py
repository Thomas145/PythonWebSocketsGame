import json
import asyncio


# Requests Models
from PythonWebSocketsGame.Application.Requests.Request import RequestType
from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest


# Response Models
from PythonWebSocketsGame.Application.Responses.Models.PlayersModelResponse import PlayersModelResponse
from PythonWebSocketsGame.Application.Responses.Models.AwaitingPlayersModelResponse import AwaitingPlayersModelResponse
from PythonWebSocketsGame.Application.Responses.Models.ServerStateModelResponse import ServerStateModelResponse
from PythonWebSocketsGame.Application.Responses.Models.ClientDetailsModelResponse import ClientDetailsModelResponse


# Ws Response Wrappers
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsNewGameResponse import WsNewGameResponse
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsServerStateResponse import WsServerStateResponse
from PythonWebSocketsGame.Application.Responses.WebSocketResponses.WsClientResponse import WsClientResponse


# Ws Server Wrappers
from PythonWebSocketsGame.Application.Server.Model.WebSocketClient import WebSocketClient

from PythonWebSocketsGame.Application.Model.Game import Game


class RequestManager:

    GAME_POOL = dict()
    PLAYER_POOL = dict()
    CONNECTION_POOL = dict()

    def __init__(self):
        self.request_types = {

            RequestType.new_game: (self.new_game_event_request, self.new_game_event_response)

        }

    def add_to_game_pool(self,game):
        self.GAME_POOL[game.id] = game
        return game

    def remove_from_game_pool(self, game_id):
        game = self.GAME_POOL[game_id]
        del self.GAME_POOL[game.id]
        return game

    def new_game_event_request(self, message, connection):
        new_game_request = json.loads(message, cls=NewGameRequest)
        game = self.add_to_game_pool(Game(new_game_request.size_of_game, new_game_request.number_of_players))
        game.link_client_to_game(self.CONNECTION_POOL[connection])

        return game

    def number_of_games(self):
        return len(self.GAME_POOL)

    def number_of_connections(self):
        return len(self.CONNECTION_POOL)

    def make_client_detail(self, connection):
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

    def make_server_state(self):
        server_state = ServerStateModelResponse()
        server_state.number_of_active_players = self.number_of_connections()
        server_state.number_of_active_games = self.number_of_games()

        ws_server_state = WsServerStateResponse()
        ws_server_state.server_state = server_state

        _json = json.dumps(ws_server_state, default=WsServerStateResponse.encode_complex)

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

    def remove_client_from_game(self, client):
        if client.in_game():
            game = self.GAME_POOL[client.game.id]
            player_exit = game.unlink_client_from_game(client)
            self.notifiy_game_of_player_exit(game, player_exit)

    def check_game_if_over(self, game):
        if game.is_game_over():
            if game.has_winner():
                self.notify_game_of_player_victory(game, game.who_won())
            else:
                self.notify_game_of_player_drawn(game)

            del self.GAME_POOL[game.id]

    async def notify_game_of_player_drawn(self, game):
        message = self.make_game_draw_message()
        game_connections = game.get_active_connections()
        await self.push_message_to_a_connections(message, game_connections)

    async def notify_game_of_player_exit(self, game, player):
        message = self.make_player_exit_message(player)
        game_connections = game.get_active_connections()
        await self.push_message_to_a_connections(message, game_connections)

    async def notify_game_of_player_entry(self, game, player):
        message = self.make_player_entry_message(player)
        game_connections = game.get_active_connections()
        await self.push_message_to_a_connections(message, game_connections)

    async def notify_game_of_player_victory(self, game, player):
        message = self.make_player_victory_message(player)
        game_connections = game.get_active_connections()
        await self.push_message_to_a_connections(message, game_connections)
        del self.GAME_POOL[game.id]

    async def notify_game_of_player_turn(self, game, player):
        game_connections = game.get_active_connections()
        game_connections.remove(player.client.connection)

        player_turn_message = self.make_player_turn_message(player)
        game_player_turn_message = self.make_game_player_turn_message(player)

        await self.push_message_to_a_connections(game_player_turn_message, game_connections)
        await self.push_message_to_a_connection(player_turn_message, player.client.connection)

    async def on_message(self, message, active_connection):
        print("on_message " + message)
        data = json.loads(message)
        request_action = RequestType(data['request'])
        action = self.request_types[request_action]

        request_function = action[0]
        response_function = action[1]
        request_result = request_function(message, active_connection)
        await response_function(request_result, active_connection)

    async def add_to_connection_pool(self, connection):
        self.CONNECTION_POOL[connection] = WebSocketClient(connection)
        await self.push_server_state_to_all_connections()
        await self.push_message_to_a_connection(self.make_client_detail(connection), connection)

    async def remove_from_connection_pool(self, connection):
        client = self.CONNECTION_POOL[connection]
        del self.CONNECTION_POOL[connection]
        self.remove_client_from_game(client)
        await self.push_server_state_to_all_connections()

    async def push_server_state_to_all_connections(self):
        await self.push_message_to_all_connections(self.make_server_state())

    @staticmethod
    async def push_message_to_a_connection(message, connection):
        await asyncio.wait([connection.send(message)])

    @staticmethod
    async def push_message_to_a_connections(message, connections):
        if connections:  # asyncio.wait doesn't accept an empty list
            await asyncio.wait([connection.send(message) for connection in connections])

    async def push_message_to_all_connections(self, message):
        self.push_message_to_a_connections(message, self.CONNECTION_POOL)

    async def new_game_event_response(self, new_game, active_connection):

        players_model_response = PlayersModelResponse()
        players_model_response.from_players(new_game.get_players())

        awaiting_players_model_response = AwaitingPlayersModelResponse()
        awaiting_players_model_response.waiting_on(
            new_game.number_of_players(), players_model_response.number_of_players()
        )

        response_body = WsNewGameResponse()
        response_body.players = players_model_response
        response_body.awaiting_players = awaiting_players_model_response

        _json = json.dumps(response_body, default=response_body.encode_complex)

        await self.push_message_to_a_connection(_json, active_connection)
        await self.push_server_state_to_all_connections()
