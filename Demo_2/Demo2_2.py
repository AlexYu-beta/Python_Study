'''
Demo_2 sums up all the input number collected from the input and gives the average value of the inputs
'''
number = 0
i = 0
sum = 0
average = 0
n=0
print('please enter the numbers, if it equals to 0 or be less than 0, the input will end')
while True:
    n = int(input('please enter a number: '))
    if n <= 0:
        break
    sum = sum + n
    number = number + 1
print('the sum of the numbers are: ', sum)
print('the average value of the numbers are: ',sum/number)