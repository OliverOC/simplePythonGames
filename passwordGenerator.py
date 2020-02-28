import random
import string


def password_generator(strength="high"):
    password = []
    if strength == "high":
        for i in range(8):
            rand_letter = random.choice(string.ascii_letters)
            rand_num = random.randint(1, 9)
            password.append(str(random.choice([rand_letter, rand_num])))
            password_joined = "".join(password)
        return password_joined

    elif strength == "medium":
        for i in range(6):
            rand_letter = random.choice(string.ascii_letters)
            rand_num = random.randint(1, 9)
            password.append(str(random.choice([rand_letter, rand_num])))
            password_joined = "".join(password)
        return password_joined

    elif strength == "low":
        for i in range(4):
            rand_letter = random.choice(string.ascii_letters)
            rand_num = random.randint(1, 9)
            password.append(str(random.choice([rand_letter, rand_num])))
            password_joined = "".join(password)
        return password_joined

    else:
        print("Please input low, medium, or high")


password1 = password_generator(strength=input("Choose low, medium or high security:"))
print(password1)