def draw_board(size):
    dashes = " ---"
    pipes = "|   "
    for i in range(size):
        print(dashes*size)
        print(pipes*(size+1))
    print(dashes*size)


if __name__=="__main__":
    game_size = input("what size board would you like? (enter a single number):")
    draw_board(game_size)
