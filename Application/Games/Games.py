
from PythonWebSocketsGame.Application.Model.Game import Game


class Games:

    def __init__(self):
        self.games = dict()

    def select_area(self, client, grid_position):
        game = self.games[client.client.game.id]

        if game is not None:
            if game.select_area(client, grid_position):
                return game

        return None

    def make_new_make_from_lobby(self, lobby):
        game = Game(lobby)
        self.games[game.id] = game

    def check_if_game_over(self, game_id):
        game = self.games[game_id]
        if game is not None:
            return game.is_game_over()
        else:
            return False

    def player_exits_game(self, client):
        game = None
        if client.game is not None:
            game = self.games[client.game.id]
            if game is not None:
                game.unlink_client_from_game(client)

        return game

    def number_of_games(self):
        return len(self.games)
