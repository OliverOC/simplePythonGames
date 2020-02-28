import random
player1 = input("rock, paper, scissors?:")
#player2 = input("rock, paper, scissors?:")
player2 = random.choice(["rock","paper","scissors"])

winner_dict = {"rock":{"rock":"draw",
                       "paper":"lose",
                       "scissors":"win"},
               "paper":{"rock":"win",
                        "paper":"draw",
                        "scissors":"lose"},
               "scissors":{"rock":"lose",
                           "paper":"win",
                           "scissors":"draw"}}
print(player2)
print(winner_dict[player1][player2])
