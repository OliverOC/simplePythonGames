def board_converter(board_marked):
    dashes = " ---"
    pipes_empty = "|   "
    pipes_x = "| X "
    pipes_o = "| O "
    board_look = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(len(board_look)):
        for ii in range(len(board_marked)):
            if board_marked[i][ii] == 0:
                board_look[i][ii] = pipes_empty
            elif board_marked[i][ii] == 1:
                board_look[i][ii] = pipes_o
            elif board_marked[i][ii] == 2:
                board_look[i][ii] = pipes_x
            else:
                pass

    print(dashes * 3)
    print(board_look[0][0] + str(board_look[0][1]) + str(board_look[0][2]) + pipes_empty)
    print(dashes * 3)
    print(board_look[1][0] + str(board_look[1][1]) + str(board_look[1][2]) + pipes_empty)
    print(dashes * 3)
    print(board_look[2][0] + str(board_look[2][1]) + str(board_look[2][2]) + pipes_empty)
    print(dashes * 3)
    return board_marked


if __name__ == "__main__":
    game = [[2, 1, 1],
            [1, 2, 1],
            [0, 1, 1]]
    board_converter(game)



