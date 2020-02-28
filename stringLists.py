entry = input("Hello there, I would like you to input a word please:")
rev_entry = entry[::-1]
half_length = len(entry)/2
if entry[0:half_length] == rev_entry[0:half_length]:
    print(entry + " is a palindrome")
else:
    print(entry + " is not a palindrome")
