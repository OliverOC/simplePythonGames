def string_reverser(string_input):
    string_split = string_input.split()
    string_split_reversed = string_split[::-1]
    extracted_string_split_reversed = " ".join(string_split_reversed)
    return extracted_string_split_reversed


string1 = "my name is Oliver and I am 23"
string1_reversed = string_reverser(string1)
print(string1_reversed)