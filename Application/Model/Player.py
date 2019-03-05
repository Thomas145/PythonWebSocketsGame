import uuid


class Player:

    def __init__(self, player_number):
        self.selectedStyle = None
        self.player_number = player_number
        self.id = uuid.uuid4()
        self.client = None

    def is_assigned(self):
        return self.client is not None

    def get_player_name(self):
        if self.is_assigned():
            return self.client.player_name
        else:
            return None

    def get_player_number(self):
        return self.player_number

    def style(self, style):
        if self.selectedStyle is None:
            self.selectedStyle = style

    def chosen_style(self):
            return self.selectedStyle

    def display_player(self):
        print(self.name + " assigned " + self.chosen_style().display())

    def same_player(self, player):
        return self.id == player.id
