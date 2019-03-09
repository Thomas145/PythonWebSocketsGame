from .Styles import NoStyle


class GridArea:

    def __init__(self, position_marker):
        self.style = NoStyle()
        self.position = position_marker

    def reset(self):
        self.style = NoStyle()

    def current_state(self):
        print(self.style.display(), end="", flush=True)

    def grid_area_style(self):
        return self.style

    def grid_area_position(self):
        return self.position

    def open(self):
        return not self.style.selected()

    def selected(self, player):
        if self.style.selected() is False:
            if player is not None:
                if player.chosen_style() is not None:
                    self.style = player.chosen_style()
                    return True

        return False
