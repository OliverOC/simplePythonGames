number = int(input("number:"))
divisors = range(1,number+1)
answers = []
for i in divisors:
    if number % i == 0:
        answers.append(i)
    else:
        pass
print(answers)
