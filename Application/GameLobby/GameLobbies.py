
from PythonWebSocketsGame.Application.GameLobby.GameLobby import GameLobby


class GameLobbies:

    def __init__(self):
        self.client_in_lobby_index = dict()
        self.lobbies = dict()

    def place_client_in_lobby_index(self, client, lobby):
        print("Starting place_client_in_lobby_index")
        self.client_in_lobby_index[client.id] = lobby.lobby_id
        print("number_of_clients in lobby " + str(len(self.lobbies)))

    def remove_client_from_lobby_index(self, client):
        print("Started remove_client_from_lobby_index")
        del self.client_in_lobby_index[client.id]
        print("number_of_clients in lobby " + str(len(self.lobbies)))

    def create_new_lobby(self, number_of_player_required, size_of_game, client):
        print("Starting create_new_lobby")
        new_lobby = None
        if not self.is_client_in_lobby(client):
            new_lobby = GameLobby(number_of_player_required, size_of_game, client)
            self.lobbies[new_lobby.lobby_id] = new_lobby
            self.place_client_in_lobby_index(client, new_lobby)
            return new_lobby

        return new_lobby

    def is_client_in_lobby(self, client):
        keys = self.client_in_lobby_index.keys()
        in_lobby = client.id in keys
        return in_lobby

    def join_lobby(self, client):
        if not self.is_client_in_lobby(client):

            for lobby_id, lobby in self.lobbies:

                if lobby.join_game_lobby(client):

                    self.place_client_in_lobby_index(client, lobby)

                    return lobby

        return None

    def leave_lobby(self, client):
        print("Stared leave_lobby")
        lobby = None
        if self.is_client_in_lobby(client):

            print("client_was_in_lobby")
            lobby_key = self.client_in_lobby_index.get(client.id)
            lobby = self.lobbies.get(lobby_key)
            lobby.leave_game_lobby(client)
            self.remove_client_from_lobby_index(client)

            self.terminate_lobby_if_empty(lobby)

        else:
            print("client was not in lobby")
            print("number_of_clients in lobby " + str(len(self.lobbies)))

        return lobby

    def terminate_lobby_if_empty(self, lobby):
        print("Started terminate_lobby_if_empty")
        if lobby.is_lobby_empty():
            print("lobby_was_terminate")
            del self.lobbies[lobby.lobby_id]
        else:
            print("lobby_was_not_terminate")
