import json
import asyncio

from PythonWebSocketsGame.Application.GameLobby.GameLobbies import GameLobbies
from PythonWebSocketsGame.Application.Games.Games import Games

# Requests Models
from PythonWebSocketsGame.Application.Requests.Request import RequestType


# Ws Server Wrappers
from PythonWebSocketsGame.Application.Server.Model.WebSocketClient import WebSocketClient

from PythonWebSocketsGame.Application.Server.WsGameResponseMessages import WsGameResponseMessages

from PythonWebSocketsGame.Application.Server.WsGameRequestMessages import WsGameRequestMessages


class RequestManager:

    messages = WsGameResponseMessages()
    requests = WsGameRequestMessages()
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
        print('on_connection_open')
        self.CONNECTION_POOL[connection] = WebSocketClient(connection)
        await self.push_server_state_to_all_connections()

    async def on_connection_close(self, connection):
        print('on_connection_close')
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

    async def on_join_game_message(self, json_as_dct, connection):
        client = self.CONNECTION_POOL[connection]
        join_game_request = self.requests.unwrap_join_game_request(json_as_dct)

        if join_game_request is not None:

            lobby = self.lobbies.join_lobby(client)

            if lobby is not None:

                active_connections = lobby.active_lobby_connections()
                active_connections.remove(client.connection)

                await self.push_message_to_a_connections(
                    self.messages.make_player_lobby_entry_message(client), active_connections)

                await self.push_message_to_a_connections(
                    self.messages.make_you_have_joined_lobby_message(), client.connection)

            else:

                await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

    async def on_create_game_message(self, json_as_dct, connection):
        print("Started on_create_game_message")

        client = self.CONNECTION_POOL[connection]
        new_game_request = self.requests.unwrap_new_game_request(json_as_dct)

        if new_game_request is not None:

            new_lobby = self.lobbies.create_new_lobby(
                new_game_request.number_of_players, new_game_request.size_of_game, client)

            if new_lobby is not None:

                await self.push_message_to_a_connection(
                    self.messages.make_new_lobby_message(new_lobby), client.connection)
            else:

                await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)
        else:

            await self.push_message_to_a_connection(self.messages.make_action_failure_message(), client.connection)

        print("Ended on_create_game_message")

    async def on_lobby_exit_message(self, json_as_dct, connection):

        client = self.CONNECTION_POOL[connection]
        exit_lobby_request = self.requests.unwrap_exit_lobby_request(json_as_dct)

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

    async def on_game_exit_message(self, json_as_dct, connection):

        client = self.CONNECTION_POOL[connection]
        exit_game_request = self.requests.unwrap_exit_game_request(json_as_dct)

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

    async def on_grid_area_selection_message(self, json_as_dct, connection):

        client = self.CONNECTION_POOL[connection]
        select_area_request = self.requests.unwrap_select_area_request(json_as_dct)

        if select_area_request is not None:

            game = self.games.select_area(client, select_area_request)

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
        print("Started: on_message")
        json_as_dct = json.loads(message)

        try:

            request_type = json_as_dct['request']
            print("Started: on_message: request_type " + request_type)
            request_action = RequestType.from_str(request_type)

            action = self.request_types[request_action]

            await action(json_as_dct, active_connection)
        except NotImplementedError:
            await self.push_message_to_a_connection(
                self.messages.make_action_failure_message(), active_connection)

        print("Ended: on_message")

    async def push_message_to_all_connections(self, message):
        await self.push_message_to_a_connections(message, self.CONNECTION_POOL)

    async def push_server_state_to_all_connections(self):

        number_of_games = self.games.number_of_games()

        number_of_clients = len(self.CONNECTION_POOL)

        await self.push_message_to_all_connections(
            self.messages.make_server_state_message(number_of_clients, number_of_games))

    @staticmethod
    async def push_message_to_a_connection(message, connection):
        print("push_message_to_a_connection: " + message)
        await asyncio.wait([connection.send(message)])

    @staticmethod
    async def push_message_to_a_connections(message, connections):
        print("push_message_to_a_connections: " + message)
        if connections:  # asyncio.wait doesn't accept an empty list
            await asyncio.wait([connection.send(message) for connection in connections])
