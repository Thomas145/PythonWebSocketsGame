import json
import asyncio

from PythonWebSocketsGame.Application.GameLobby.GameLobbies import GameLobbies
from PythonWebSocketsGame.Application.Games.Games import Games

# Requests Models
from PythonWebSocketsGame.Application.Requests.Request import RequestType
from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest


# Ws Server Wrappers
from PythonWebSocketsGame.Application.Server.Model.WebSocketClient import WebSocketClient

from PythonWebSocketsGame.Application.Model.Game import Game

from PythonWebSocketsGame.Application.Server.WsGameMessages import WsGameMessages
from PythonWebSocketsGame.Application.Server.WsGameNotification import WsGameNotification


class RequestManager:

    notification = WsGameNotification()
    messages = WsGameMessages()
    lobbies = GameLobbies()
    games = Games()

    CONNECTION_POOL = dict()

    def __init__(self):
        self.request_types = {
            RequestType.new_game: (self.new_game_event_request, self.new_game_event_response)
        }

    def new_game_event_request(self, message, connection):
        new_game_request = json.loads(message, cls=NewGameRequest)
        game = self.add_to_game_pool(Game(new_game_request.size_of_game, new_game_request.number_of_players))
        game.link_client_to_game(self.CONNECTION_POOL[connection])
        return game

    async def on_connection_open(self, connection):
        self.CONNECTION_POOL[connection] = WebSocketClient(connection)
        await self.push_server_state_to_all_connections()
        await self.push_message_to_a_connection(self.make_client_detail_message(connection), connection)

    async def on_connection_close(self, connection):
        client = self.CONNECTION_POOL[connection]
        game = self.games.player_exits_game(client)
        lobby = self.lobbies.leave_lobby(client)
        del self.CONNECTION_POOL[connection]

        if game is not None:

            if game.is_game_over():

                await self.push_message_to_a_connections(
                    self.messages.make_game_over_message(), game.get_active_connections())

            else:

                await self.push_message_to_a_connections(
                    self.messages.make_player_exit_message(client), game.get_active_connections())

        if lobby is not None and not lobby.is_lobby_empty():

            await self.push_message_to_a_connections(
                self.messages.make_player_lobby_exit_message(client), lobby.active_lobby_connections())

        await self.push_server_state_to_all_connections()

    async def on_join_game_message(self,connection):
        client = self.CONNECTION_POOL[connection]
        lobby = self.lobbies.join_lobby(client)

        if lobby is not None:

            active_connections = lobby.active_lobby_connections()
            active_connections.remove(client.connection)

            await self.push_message_to_a_connections(
                self.messages.make_player_lobby_entry_message(client), active_connections)

            await self.push_message_to_a_connections(
                self.messages.make_you_have_joined_lobby_message(client), client.connection)

    async def on_create_game_message(self,connection):
        client = self.CONNECTION_POOL[connection]
        new_lobby = self.lobbies.create_new_lobby(client)

        if new_lobby is not None:
            await self.push_message_to_a_connection(self.messages.make_new_lobby_message(new_lobby), client.connection)
        else:
            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_lobby_exit_message(self, connection):

        client = self.CONNECTION_POOL[connection]
        lobby = self.lobbies.leave_lobby(client)

        if lobby is not None:

            active_connections = lobby.active_lobby_connections()

            await self.push_message_to_a_connections(
                self.messages.make_player_lobby_exit_message(client), active_connections)

            await self.push_message_to_a_connection(
                self.messages.make_you_have_exited_lobby_message(), client.connection)

        else:
            await self.push_message_to_a_connection(
                self.messages.make_action_failure_message(), client.connection)

    async def on_game_exit_message(self, connection):
        client = self.CONNECTION_POOL[connection]
        game = self.games.player_exits_game(client)

        if game is not None:

            if game.is_game_over():

                await self.push_message_to_a_connections(
                    self.messages.make_game_over_message(), game.get_active_connections())

            else:
                await self.push_message_to_a_connections(
                    self.messages.make_player_exit_message(client), game.get_active_connections())

            await self.push_message_to_a_connection(self.messages.make_you_have_exited_game_message(), client.connection)

        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_grid_area_selection_message(self, connection):
        client = self.CONNECTION_POOL[connection]
        game = self.games.select_area(client)

        if game is not None:

            await self.push_message_to_a_connection(
                self.messages.make_you_have_selected_area_game_message(), client.connection)

            await self.push_message_to_a_connections(
                self.messages.make_game_state_message(game), game.get_active_connections())

        else:

            await self.push_message_to_a_connection(
                self.messages.make_action_failure_message(), client.connection)

    async def on_message(self, message, active_connection):
        print("on_message " + message)
        data = json.loads(message)
        request_action = RequestType(data['request'])
        action = self.request_types[request_action]

        request_function = action[0]
        response_function = action[1]
        request_result = request_function(message, active_connection)
        await response_function(request_result, active_connection)

    def number_of_connections(self):
        return len(self.CONNECTION_POOL)

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

    async def push_message_to_all_connections(self, message):
        self.push_message_to_a_connections(message, self.CONNECTION_POOL)

    async def new_game_event_response(self, new_game, active_connection):
        _json = self.messges.make_new_game_response(new_game)
        await self.push_message_to_a_connection(_json, active_connection)
        await self.push_server_state_to_all_connections()

    async def push_server_state_to_all_connections(self):
        await self.push_message_to_all_connections(self.make_server_state_message())

    @staticmethod
    async def push_message_to_a_connection(message, connection):
        await asyncio.wait([connection.send(message)])

    @staticmethod
    async def push_message_to_a_connections(message, connections):
        if connections:  # asyncio.wait doesn't accept an empty list
            await asyncio.wait([connection.send(message) for connection in connections])
