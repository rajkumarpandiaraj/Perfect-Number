num = int(input('Enter the Number You want to check : '))
listOfDivisor = []
result = 0
for i in range(1, num) :
    if num % i == 0 :
        listOfDivisor.append(i)
for j in listOfDivisor :
    result += j
if result == num :
    print(num, 'is a perfect number')
else :
    print(num, 'is not a perfect number')

