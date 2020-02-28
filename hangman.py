from pickWord import random_word


def initialise_board(length):
    dash = "_ "
    board = dash*length
    return board


def limited_digit_input(prompt, digits):
    number_input = input(prompt)
    while len(number_input) > digits:
        print('only '+str(digits)+' digit(s) allowed')
        number_input = input(prompt)
    return number_input


def show_correct_letter(word, current_board, letter):
    locations_x2 = [i * 2 for i, x in enumerate(word) if x == letter]
    current_board_list = list(current_board)
    for i in locations_x2:
        current_board_list[i] = letter
    current_board_str = ''.join(current_board_list)
    return current_board_str


def check_win(word, current_board):
    current_board_split = current_board.strip().split(' ')
    word_list = list(word)
    if current_board_split == word_list:
        print("CONGRATS!!! You got it... ")
        return False
    else:
        return True


def draw_hangman(remaining_guesses):
    remaining_guesses_to_hanging = remaining_guesses
    part1 = " __________ "
    part2 = "  |\n  |\n  |\n  |\n  |"
    part2_4 = "  |\n  |\n  |\n  |"
    part2_5 = "  |\n  |\n  |"
    part2_6 = "  |"
    part3 = "  _______"
    part4 = "  |     |"
    part5 = "  |    _O_"
    part6 = "  |     |\n  |    / \\"

    if remaining_guesses_to_hanging > 5:
        pass
    elif remaining_guesses_to_hanging == 5:
        print(part1)
    elif remaining_guesses_to_hanging == 4:
        print(part2)
        print(part1)
    elif remaining_guesses_to_hanging == 3:
        print(part3)
        print(part2)
        print(part1)
    elif remaining_guesses_to_hanging == 2:
        print(part3)
        print(part4)
        print(part2_4)
        print(part1)
    elif remaining_guesses_to_hanging == 1:
        print(part3)
        print(part4)
        print(part5)
        print(part2_5)
        print(part1)
    elif remaining_guesses_to_hanging == 0:
        print(part3)
        print(part4)
        print(part5)
        print(part6)
        print(part2_6)
        print(part1)


if __name__ == "__main__":

    word_to_guess = random_word()
    # word_to_guess = "duck"
    word_to_guess_lower = word_to_guess.lower().strip()
    word_length = len(word_to_guess_lower)
    board_empty = initialise_board(word_length)
    board_updated = board_empty
    print(board_empty)
    guesses = 6

    play = True
    while play:
        guess_letter = limited_digit_input('Guess a letter:', 1)
        guess_letter_lower = guess_letter.lower()
        if guess_letter_lower in word_to_guess_lower:
            board_updated = show_correct_letter(word_to_guess_lower, board_updated, guess_letter_lower)
            print(board_updated)
            play = check_win(word_to_guess_lower, board_updated)
        else:
            guesses = guesses - 1
            print("You have " + str(guesses) + " guesses remaining!")
            draw_hangman(guesses)
            if guesses == 0:
                play = False
    pass
    print("The word was "+str(word_to_guess))



