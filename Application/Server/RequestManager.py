import json
import asyncio

from PythonWebSocketsGame.Application.GameLobby.GameLobbies import GameLobbies
from PythonWebSocketsGame.Application.Games.Games import Games

# Requests Models
from PythonWebSocketsGame.Application.Requests.Request import RequestType

# Ws Server Requests
from PythonWebSocketsGame.Application.Requests.Models.ExitGameRequest import ExitGameRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitLobbyRequest import ExitLobbyRequest
from PythonWebSocketsGame.Application.Requests.Models.JoinGameRequest import JoinGameRequest
from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest
from PythonWebSocketsGame.Application.Requests.Models.SelectGridAreaMessage import SelectGridAreaMessage


# Ws Server Wrappers
from PythonWebSocketsGame.Application.Server.Model.WebSocketClient import WebSocketClient
from PythonWebSocketsGame.Application.Server.WsGameMessages import WsGameMessages


class RequestManager:

    messages = WsGameMessages()
    lobbies = GameLobbies()
    games = Games()

    CONNECTION_POOL = dict()

    def __init__(self):
        self.request_types = {
            RequestType.new_game: self.on_create_game_message,
            RequestType.exit_lobby: self.on_lobby_exit_message,
            RequestType.join_game: self.on_join_game_message,
            RequestType.exit_game: self.on_game_exit_message,
            RequestType.select_area: self.on_grid_area_selection_message
        }

    async def on_connection_open(self, connection):
        self.CONNECTION_POOL[connection] = WebSocketClient(connection)
        await self.push_server_state_to_all_connections()
        await self.push_message_to_a_connection(self.messages.make_client_detail_message(connection), connection)

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

    async def on_join_game_message(self, message, connection):

        client = self.CONNECTION_POOL[connection]
        join_game_request = json.load(message, cls=JoinGameRequest)

        if join_game_request is not None:

            lobby = self.lobbies.join_lobby(client)

            if lobby is not None:

                active_connections = lobby.active_lobby_connections()
                active_connections.remove(client.connection)

                await self.push_message_to_a_connections(
                    self.messages.make_player_lobby_entry_message(client), active_connections)

                await self.push_message_to_a_connections(
                    self.messages.make_you_have_joined_lobby_message(client), client.connection)
        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_create_game_message(self, message, connection):
        client = self.CONNECTION_POOL[connection]
        new_game_request = json.load(message, cls=NewGameRequest)

        if new_game_request is not None:

            new_lobby = self.lobbies.create_new_lobby(
                new_game_request.number_of_players, new_game_request.size_of_game, client)

            if new_lobby is not None:
                await self.push_message_to_a_connection(self.messages.make_new_lobby_message(new_lobby), client.connection)
            else:
                await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_lobby_exit_message(self, message, connection):

        client = self.CONNECTION_POOL[connection]
        exit_lobby_request = json.load(message, cls=ExitLobbyRequest)

        if exit_lobby_request is not None:

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
        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_game_exit_message(self, message, connection):

        client = self.CONNECTION_POOL[connection]
        exit_game_request = json.load(message, cls=ExitGameRequest)

        if exit_game_request is not None:

            game = self.games.player_exits_game(client)

            if game is not None:

                if game.is_game_over():

                    await self.push_message_to_a_connections(
                        self.messages.make_game_over_message(), game.get_active_connections())

                else:

                    await self.push_message_to_a_connections(
                        self.messages.make_player_exit_message(client), game.get_active_connections())

                await self.push_message_to_a_connection(
                    self.messages.make_you_have_exited_game_message(), client.connection)

            else:

                await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)
        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_grid_area_selection_message(self, message, connection):
        client = self.CONNECTION_POOL[connection]
        select_grid_area = json.loads(message, cls=SelectGridAreaMessage)

        if select_grid_area is not None:

            game = self.games.select_area(client, select_grid_area)

            if game is not None:

                await self.push_message_to_a_connection(
                    self.messages.make_you_have_selected_area_game_message(), client.connection)

                active_connections = game.get_active_connections()
                active_player = game.who_turn_is_it()

                await self.push_message_to_a_connections(
                    self.messages.make_game_state_message(game), active_connections)

                await self.push_message_to_a_connection(
                    self.messages.make_your_turn_message(), active_player.client.connection)

                active_connections.remove(active_player.client.connection)

                await self.push_message_to_a_connections(
                    self.messages.make_player_turn_message(active_player), active_connections)

            else:

                await self.push_message_to_a_connection(
                    self.messages.make_action_failure_message(), client.connection)

        else:

            await self.push_message_to_a_connection(
                self.messages.make_action_failure_message(), client.connection)

    async def on_message(self, message, active_connection):
        data = json.loads(message)
        request_action = RequestType(data['request'])
        action = self.request_types[request_action]

        request_function = action[0]
        response_function = action[1]
        request_result = request_function(message, active_connection)
        await response_function(request_result, active_connection)

    async def push_message_to_all_connections(self, message):
        await self.push_message_to_a_connections(message, self.CONNECTION_POOL)

    async def push_server_state_to_all_connections(self):
        await self.push_message_to_all_connections(self.messages.make_server_state_message())

    @staticmethod
    async def push_message_to_a_connection(message, connection):
        await asyncio.wait([connection.send(message)])

    @staticmethod
    async def push_message_to_a_connections(message, connections):
        if connections:  # asyncio.wait doesn't accept an empty list
            await asyncio.wait([connection.send(message) for connection in connections])
