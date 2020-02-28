def list_bookender(list_input):
    new = [list_input[0],list_input[-1]]
    return new


list1 = [1, 5, 3, 5, 823, 392, 1823]
answer = list_bookender(list1)
print(answer)