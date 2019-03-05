from .GridColumn import GridColumn


class Grid:

    def __init__(self, grid_size):

        self.row = []
        for i in range(grid_size):
            self.row.append(GridColumn(i, grid_size))

    def exact_position(self, row_index, column_index):
        _row = self.row_position(row_index)
        _column = None
        _result = None

        if _row is not None:
            _column = _row.column_position(column_index)

        if _column is not None:
            _result = (_column, row_index, column_index)

        return _result

    def row_position(self, row_index):
        a = row_index > -1
        b = row_index <= len(self.row) - 1

        if a & b:
            return self.row[row_index]

        return None

    def print_board(self):

        row_sep = ""
        for i in range((len(self.row)*5) + 1):
            row_sep += "-"

        print()
        for row in self.row:

            print(row_sep)
            print("", end="|", flush=True)

            for column in row.get_columns():

                row_column_style = column.grid_area_style()

                if not row_column_style.selected():
                    print(" " + str(row.position) + str(column.position) + " ", end="|", flush=True)
                else:
                    print(" " + row_column_style.display() + "  ", end="|", flush=True)

            print()

        print(row_sep)
        print()

    def right_of(self, row_position, column_position):
        # print("Moving right_of")
        return self.exact_position(row_position, column_position + 1)

    def left_of(self, row_position, column_position):
        # print("Moving left_of")
        return self.exact_position(row_position, column_position - 1)

    def down_of(self, row_position, column_position):
        # print("Moving down_of")
        return self.exact_position(row_position + 1, column_position)

    def above_of(self, row_position, column_position):
        # print("Moving above_of")
        return self.exact_position(row_position - 1, column_position)

    def right_down_of(self, row_position, column_position):
        # print("Moving right_down_of")
        return self.exact_position(row_position + 1, column_position + 1)

    def left_down_of(self, row_position, column_position):
        # print("Moving left_down_of")
        return self.exact_position(row_position + 1, column_position - 1)

    def number_of_matches(self, start_area, movement_func, current_area, row_position, column_position,
                          number_other_matches, number_of_movement):

        win_con = 2
        need_more_matches = number_other_matches < win_con
        more_possible_movements = number_of_movement < win_con
        within_bounds = current_area is not None

        if need_more_matches & more_possible_movements & within_bounds:

            movement_result = movement_func(row_position, column_position)

            if movement_result is not None:

                movement_result_current_area = movement_result[0]
                movement_result_row_position = movement_result[1]
                movement_result_column_position = movement_result[2]

                start_area_style = start_area.grid_area_style()
                new_area_style = movement_result_current_area.grid_area_style()

                if start_area_style.same_style(new_area_style):
                    number_other_matches = self.number_of_matches(
                        start_area,
                        movement_func,
                        movement_result_current_area,
                        movement_result_row_position,
                        movement_result_column_position,
                        number_other_matches + 1,
                        number_of_movement + 1)

        return number_other_matches

    @staticmethod
    def win_condition(number_matches):
        return number_matches == 2

    def winner(self):
        winner: bool = False

        #  For every area i want to check if the same style occurs at least three times
        for index_row, row in enumerate(self.row):

            for index_column in range(row.number_of_columns()):

                start_area = self.exact_position(index_row, index_column)[0]

                if not winner:
                    winner = self.win_condition(self.number_of_matches(start_area, self.left_down_of, start_area,
                                                                       index_row, index_column, 0, 0))

                if not winner:
                    winner = self.win_condition(self.number_of_matches(start_area, self.right_down_of, start_area,
                                                                       index_row, index_column, 0, 0))

                if not winner:
                    winner = self.win_condition(self.number_of_matches(start_area, self.down_of, start_area,
                                                                       index_row, index_column, 0, 0))

                if not winner:
                    winner = self.win_condition(self.number_of_matches(start_area, self.right_of, start_area,
                                                                       index_row, index_column, 0, 0))

        return winner

    def no_spaces(self):
        space_remaining = False

        for col in self.row:
            if not space_remaining:
                space_remaining = col.has_space()

        return not space_remaining

