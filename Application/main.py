from PythonWebSocketsGame.Application.Model.Game import Game


def main():
    print("Start")

    game = Game(
        min(10, max(3, int(input("Please select a game size name...(Min 3) (Max 10) ")))),
        min(4, max(2, int(input("Please select the number of players...(Min 2) (Max 4) ")))),
    )

    for player in game.get_players():
        player.set_player_name(input("Enter Player " + str(player.get_player_number()) + " name... "))

    while True:

        try:
            game.show_board_state()
            game.who_turn_is_it()
            _space = input("Select a grid space....")

            row_space = int(_space[:1])
            column_space = int(_space[1:2])
            game.active_player_mark_space(row_space, column_space)

            if game.is_game_over():
                break

        except ValueError:
            print("Invalid grid reference entered")

    game.show_board_state()
    game.who_won()

    print("End")


if __name__ == '__main__':
    main()
