def get_fib_nums(nums):
    fibs = []
    if nums == 0:
        pass
    elif nums == 1:
        fibs.append(1)
    elif nums == 2:
        fibs.append(1)
        fibs.append(1)
    elif nums >=2:
        fibs = [1,1]
    while len(fibs) < nums:
            fibs.append(fibs[-2]+fibs[-1])
    return fibs


fib_nums = input("how many fibonacci numbers would you like?:")
fib_ans = get_fib_nums(fib_nums)
print(fib_ans)
