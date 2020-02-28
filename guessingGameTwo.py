# system guesses number
# i say higher or lower
# system will guess again
# repeat until the system gets the right number
# count the attempts taken

import random
guess_count = 0
MIN = 1
MAX = 100
system_guess = random.randint(MIN, MAX)
print(system_guess)
higher_lower = input("correct, higher or lower?:")
if higher_lower == "lower":
    MAX = system_guess - 1
elif higher_lower == "higher":
    MIN = system_guess + 1
elif higher_lower == "correct":
    print("Correct!!!")
    pass
else:
    print("error")
    pass

while higher_lower != "correct":
    guess_count = guess_count + 1
    print("Guesses:" + str(guess_count))
    if higher_lower == "higher":
        system_guess = random.randint(system_guess+1, MAX)
        print(system_guess)
        higher_lower = input("correct, higher or lower?:")
        if higher_lower == "lower":
            MAX = system_guess - 1
        elif higher_lower == "higher":
            MIN = system_guess + 1
        elif higher_lower == "correct":
            print("Correct!!!")
            break
        else:
            print("error")
            break

    elif higher_lower == "lower":
        system_guess = random.randint(MIN,system_guess-1)
        print(system_guess)
        higher_lower = input("correct, higher or lower?:")
        if higher_lower == "lower":
            MAX = system_guess - 1
        elif higher_lower == "higher":
            MIN = system_guess + 1
        elif higher_lower == "correct":
            print("Correct!!!")
            break
        else:
            print("error")
            break

    else:
        break
print("game over")
