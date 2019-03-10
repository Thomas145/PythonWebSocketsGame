from PythonWebSocketsGame.Application.Model.Player import Player
from PythonWebSocketsGame.Application.Model.Grid import Grid
from PythonWebSocketsGame.Application.Model.Styles import SelectedStyle

import uuid


class Game:

    def __init__(self, lobby):
        self.id = uuid.uuid4()
        self.players = []
        self.players_pointer = 0
        self.active_player = None
        self.winner = None
        self.grid = Grid(lobby.size_of_game)

        position = 0
        for key, client in lobby.get_clients_in_lobby().items():

            player = Player(position+1)
            self.players.append(player)
            player.style(SelectedStyle(position))
            player.client = client

            # Links the client to the game on creation so on any action the game can be found with ease.
            client.game = self

            if position == 0:
                self.active_player = player
            position += 1

    def unlink_client_from_game(self, client):
        print('Stared unlink_client_from_game')
        for player in self.players:
            if player.client.id == client.id:
                self.players.remove(player)
                print('unlink_client_from_game_removed')
                return player

        return None

    def get_active_connections(self):
        active_connections = set()

        for player in self.get_players():
            if player.is_assigned():
                active_connections.add(player.client.connection)

        return active_connections

    def get_players(self):
        return self.players

    def number_of_players(self):
        return len(self.players)

    def swap_active_player(self):
        self.players_pointer += 1
        if self.players_pointer >= len(self.get_players()):
            self.players_pointer = 0

        self.active_player = self.get_players()[self.players_pointer]

    def has_winner(self):
        return self.winner is not None

    def show_board_state(self):
        self.grid.print_board()

    def is_game_over(self):
        return self.has_winner() or self.grid.no_spaces() or len(self.players) <= 1

    def who_won(self):
        return self.winner

    def who_turn_is_it(self):
        return self.active_player

    def select_area(self, client, grid_position):

        if self.active_player is not None:

            if self.active_player.client.id == client.id:

                return self.active_player_mark_space(grid_position.grid_row, grid_position.grid_column)

        return False

    def active_player_mark_space(self, grid_row, grid_column):

        grid_selection = self.grid.exact_position(grid_row, grid_column)

        if grid_selection is not None:

            if grid_selection[0].selected(self.active_player):

                has_winner = self.grid.winner()

                if not has_winner:
                    self.swap_active_player()
                else:
                    self.winner = self.active_player

            return True

        return False
