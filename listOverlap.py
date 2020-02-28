a = [2,4,2,4,4,43,5,5,3,42,435]
b = [56,5,67546,43,6,67,54,54,3,435]
new_list = []
for i in a:
    if i in b and i not in new_list:
        new_list.append(i)
print(new_list)
