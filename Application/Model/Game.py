from PythonWebSocketsGame.Application.Model.Player import Player
from PythonWebSocketsGame.Application.Model.Grid import Grid
from PythonWebSocketsGame.Application.Model.Styles import SelectedStyle

import uuid
import queue

class Game:

    def __init__(self, game_size, players):
        self.id = uuid.uuid4()
        self.players = []
        self.waiting_on = None
        self.players_pointer = 0
        self.active_player = None
        self.winner = None
        self.assignment_queue = queue.Queue(players)

        for i in range(players):

            player = Player((i+1))

            self.assignment_queue.put(player)
            self.players.append(player)

            player.style(SelectedStyle(i))

            if self.active_player is None:
                self.active_player = player

        self.grid = Grid(game_size)
        self.waiting_on = self.number_of_players()

    def link_client_to_game(self, client):

        if not self.assignment_queue.empty():
            if not client.in_game:
                player_to_assign = self.assignment_queue.get()
                player_to_assign.client = client
                client.game = self

    def unlink_client_from_game(self, client):
        for player in self.players:
            if player.client.id == client.id:
                player.client = None
                client.game = None
                self.players.remove(player)
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
        return self.has_winner() or self.grid.no_spaces()

    def who_won(self):
        return self.winner

    def who_turn_is_it(self):
        return self.active_player

    def active_player_mark_space(self, grid_row, grid_column):

        grid_selection = self.grid.exact_position(grid_row, grid_column)

        if grid_selection is not None:

            if grid_selection[0].selected(self.active_player):

                has_winner = self.grid.winner()

                if not has_winner:
                    self.swap_active_player()
                else:
                    self.winner = self.active_player
