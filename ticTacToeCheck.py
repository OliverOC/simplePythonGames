def check_win(game_to_check):
    for i in range(3):
        if game_to_check[i] == [1, 1, 1]:
            winner = "player1"
            return winner
        elif game_to_check[i] == [2, 2, 2]:
            winner = "player2"
            return winner
        elif game_to_check[0][i] == 1 and game_to_check[1][i] == 1 and game_to_check[2][i] == 1:
            winner = "player1"
            return winner
        elif game_to_check[0][i] == 2 and game_to_check[1][i] == 2 and game_to_check[2][i] == 2:
            winner = "player2"
            return winner
        else:
            pass

    if game_to_check[0][0] == 1 and game_to_check[1][1] == 1 and game_to_check[2][2] == 1:
        winner = "player1"
        return winner
    elif game_to_check[0][0] == 2 and game_to_check[1][1] == 2 and game_to_check[2][2] == 2:
        winner = "player2"
        return winner
    else:
        if game_to_check[0][2] == 1 and game_to_check[1][1] == 1 and game_to_check[2][0] == 1:
            winner = "player1"
            return winner
        elif game_to_check[0][2] == 2 and game_to_check[1][1] == 2 and game_to_check[2][0] == 2:
            winner = "player2"
            return winner
        else:
            winner = "no winner"
            return winner


if __name__ == "__main__":
    game = [[2, 1, 1],
            [1, 0, 1],
            [0, 1, 1]]
    game1 = check_win(game)
    print(game1)




