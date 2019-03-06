import uuid


class GameLobby:

    def __init__(self, number_of_player_required, size_of_game, client):

        self.lobby_id = uuid.uuid4()
        self.number_of_player_required = number_of_player_required
        self.size_of_game = size_of_game
        self.clients_in_lobby = dict()
        self.join_game_lobby(client)

    def is_lobby_full(self):
        return len(self.clients_in_lobby) == self.number_of_player_required

    def is_lobby_empty(self):
        return len(self.clients_in_lobby) == 0

    def join_game_lobby(self, client):
        if not self.is_lobby_full():
            self.clients_in_lobby[client.id] = client
            return True
        return False

    def leave_game_lobby(self, client):
        del self.clients_in_lobby[client.id]

    def active_lobby_connections(self):
        connections = set()

        for key, value in self.clients_in_lobby:
            connections.add(value.connection)

        return connections


