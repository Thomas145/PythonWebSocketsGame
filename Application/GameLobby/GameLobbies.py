
from PythonWebSocketsGame.Application.GameLobby.GameLobby import GameLobby


class GameLobbies:

    def __init__(self):
        self.client_in_lobby_index = dict()
        self.lobbies = dict()

    def place_client_in_lobby_index(self, client, lobby):
        self.client_in_lobby_index[client.id] = lobby.lobby_id

    def remove_client_from_lobby_index(self, client):
        del self.client_in_lobby_index[client.id]

    def create_new_lobby(self, client):
        new_lobby = None
        if self.is_client_in_lobby(client):
            new_lobby = GameLobby(client)
            self.lobbies[new_lobby.lobby_id] = new_lobby
            self.place_client_in_lobby_index(client, new_lobby)
            return new_lobby

        return new_lobby

    def is_client_in_lobby(self, client):
        return self.client_in_lobby_index[client.id] is None

    def join_lobby(self, client):
        if not self.is_client_in_lobby(client):

            for lobby_id, lobby in self.lobbies:

                if lobby.join_game_lobby(client):

                    self.place_client_in_lobby_index(client, lobby)

                    return lobby

        return None

    def leave_lobby(self, client):
        lobby = None
        if self.is_client_in_lobby(client):
            lobby = self.lobbies[self.is_client_in_lobby[client.id]]
            lobby.leave_game_lobby(client)
            self.remove_client_from_lobby_index(client)
            self.terminate_lobby_if_empty(lobby)
        return lobby

    def terminate_lobby_if_empty(self, lobby):
        if lobby.is_lobby_empty():
            del self.lobbies[lobby.id]
