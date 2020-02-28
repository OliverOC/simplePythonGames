a = [3,52,4,5,3,3,5,56,4,6,3,37929,10]
number_less_than = input("number:")
new_a = []
for nums in a:
    if nums < number_less_than:
        new_a.append(nums)
print(new_a)