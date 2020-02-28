import json


if __name__ == "__main__":
    add_more = True
    while add_more:
        with open("birthdays.json", "r") as f:
            birthdays = json.load(f)

        user_addition_name = input("Please contribute by adding a birthday of someone you know...\nname:")
        user_addition_birthday = input("Birthday (DD/MM/YYYY):")
        birthdays[user_addition_name] = user_addition_birthday

        with open("birthdays.json", "w") as f:
            json.dump(birthdays, f)

        print(birthdays)

        add_again = input("Would you like to add another? (Y or N):")
        if add_again == "Y":
            add_more = True
        elif add_again == "N":
            add_more = False
