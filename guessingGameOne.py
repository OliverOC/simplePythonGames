import random

random_num = random.randint(1, 9)
guess = input("Pick a number between 1 and 9:")
difference = guess - random_num
if difference == 0:
    print("correct!!!")
else:
    if difference > 0:
        print("lower")
    elif difference <0:
        print("higher")
    while difference != 0:
        guess2 = input("Pick a number between 1 and 9:")
        difference2 = guess2 - random_num
        if difference2 == 0:
            print("correct!!!")
            break
        elif difference2 > 0:
            print("lower")
        else:
            print("higher")
