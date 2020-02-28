def duplicate_destroyer_using_loops(list_input):
    new_list = []
    for i in list_input:
        if i in list_input and i not in new_list:
            new_list.append(i)
    return new_list


def duplicate_destroyer_using_sets(list_input2):
    new_list = set(list_input2)
    return new_list


list1 = [1, 5, 93, 267, 382, 2, 5, 3 ,6 ,3 ,5 ,1 ,6 ,7]
list1_no_dupes = duplicate_destroyer_using_loops(list1)
print(list1)
print(list1_no_dupes)

list2 = list1
list2_no_dupes = duplicate_destroyer_using_sets(list2)
list2_list_from_set = list(list2_no_dupes)
print(list2_no_dupes)
print(list2_list_from_set)