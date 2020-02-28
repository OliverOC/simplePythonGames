import random

def compare_numbers(number, player_guess):
    cowbull = [0,0] #number of cows and bulls respectively
    for i in range(4):
        if number[i] == player_guess[i]:
            cowbull[1] += 1
        elif number[i] in list(str(player_guess)):
            cowbull[0] += 1
            return cowbull

answer = compare_numbers(1234, 1949)
print(answer)



# game
guess

# #functions at top for random number
# guess_counter = 0
# random_num = 5555
# #random_num = random.randint(1000,9999)
# guess = input("Guess a 4-digit number:")
#
#
# while len(str(guess)) != 4:
#     print("Error, please input a 4-digit number")
#     guess = input("Guess a 4-digit number:")
#
# while random_num != guess:
#     print("Wrong!")
#     if guess == "stop":
#         pass
#     else:
#         guess = input("Guess again!:")
#         guess_counter = guess_counter + 1
#         print("Guesses:" + str(guess_counter))
#
# print("Correct!")


# while len(str(guess)) != 4:
#     if guess == random_num:
#         print("Wow!!! You got it first time.")
#     else:
#         while random_num != guess:
#             if guess == "stop":
#                 pass
#             else:
#                 guess = input("Guess again!:")
#                 guess_counter = guess_counter + 1
#                 print("Guesses:" + str(guess_counter))
# else:
#     print("Error, please input a 4-digit number")
