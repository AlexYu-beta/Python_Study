'''
Demo_2 is a simple implementation of factorial calculation
using while loop
'''
n = int(input("please enter a number: "))
fac = 1
i = 1
while i <= n:
    fac = fac * i
    i = i + 1
print("the answer is: ", fac )