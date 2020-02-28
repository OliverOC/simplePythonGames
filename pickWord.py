import random


def random_word():
    with open('sowpods.txt', 'r') as word_list:
        word = word_list.readlines()
    rand_word = random.choice(word)
    return rand_word
