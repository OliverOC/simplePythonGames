from ticTacToeCheck import check_win
from ticTacToeBoardConverter import board_converter


def start_game():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    return game


def make_move(player, row_num, col_num, game_board):
    if player == 1:
        if game_board[row_num-1][col_num-1] == 0:
            game_board[row_num-1][col_num-1] = 1
            return game_board

        else:
            print("error: space already taken. Try again player2.")
            board_converter(game_board)
            error = "error"
            return error

    elif player == 2:
        if game_board[row_num - 1][col_num - 1] == 0:
            game_board[row_num - 1][col_num - 1] = 2
            return game_board

        else:
            print("error: space already taken. Try again player2.")
            board_converter(game_board)
            error = "error"
            return error


if __name__ == "__main__":
    board = start_game()
    winner = check_win(board)
    while winner == "no winner":
        print("player1's turn")
        player1_row_input = input("row:")
        player1_column_input = input("column:")
        player1_move = make_move(1, player1_row_input, player1_column_input, board)
        if player1_move == "error":
            while player1_move == "error":
                player1_row_input = input("row:")
                player1_column_input = input("column:")
                player1_move = make_move(1, player1_row_input, player1_column_input, board)
        # print(player1_move[0])
        # print(player1_move[1])
        # print(player1_move[2])
        board_presented1 = board_converter(player1_move)
        winner = check_win(board)

        if winner == "no winner":
            print("player2's turn")
            player2_row_input = input("row:")
            player2_column_input = input("column:")
            player2_move = make_move(2, player2_row_input, player2_column_input, board)
            if player2_move == "error":
                while player2_move == "error":
                    player2_row_input = input("row:")
                    player2_column_input = input("column:")
                    player2_move = make_move(2, player1_row_input, player1_column_input, board)
            # print(player2_move[0])
            # print(player2_move[1])
            # print(player2_move[2])
            board_presented2 = board_converter(player2_move)
            winner = check_win(board)

        if winner != "no winner":
            print("winner: " + str(winner))

    print("game over")
