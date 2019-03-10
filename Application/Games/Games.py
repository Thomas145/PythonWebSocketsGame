
from PythonWebSocketsGame.Application.Games.Game import Game


class Games:

    def __init__(self):
        self.games = dict()

    def select_area(self, client, grid_position):
        game = self.games[client.client.game.id]

        if game is not None:
            if game.select_area(client, grid_position):
                return game

        return None

    def make_game_from_lobby(self, lobby):
        game = Game(lobby)
        self.games[game.id] = game
        return game

    def check_if_game_over(self, game_id):
        game = self.games[game_id]
        if game is not None:
            return game.is_game_over()
        else:
            return False

    def player_exits_game(self, client):
        print('Started player_exits_game')
        game = None
        if client.game is not None:
            print('player_was_in_game')
            game = self.games.get(client.game.id)
            if game is not None:
                print('player_was_in_game_found')
                game.unlink_client_from_game(client)
        else:
            print("Client was not in game")

        return game

    def is_game_over(self, game):
        print("is_game_over")
        if self.check_if_game_over(game.id):
            print("game_is_over terminating game")
            del self.games[game.id]
            return True
        print("game_is_not_over")
        return False

    def number_of_games(self):
        return len(self.games)
