def get_num():
    return int(input("pick a number, any number:"))


num = get_num()
divisors = range(1,num+1)
answers = []
for i in divisors:
    if num % i == 0:
        answers.append(i)
    else:
        pass
print("Divisors: " + str(answers))
if len(answers) == 2:
    print("that was a prime number!!")
else:
    print("not a prime...")