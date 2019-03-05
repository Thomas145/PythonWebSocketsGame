from .GridArea import GridArea


class GridColumn:

    def __init__(self, position_marker, grid_size):
        self.position = position_marker
        self.column = []

        for i in range(grid_size):
            self.column.append(GridArea(i))

    def get_position(self):
        return self.position

    def column_position(self, column_index):
        a = column_index > -1
        b = column_index <= (self.number_of_columns() - 1)

        if a & b:
            return self.column[column_index]

        return None

    def has_space(self):
        open_space = False
        for column_space in self.column:
            if not open_space:
                open_space = column_space.open()

        return open_space

    def number_of_columns(self):
        return len(self.column)

    def get_columns(self):
        return self.column
