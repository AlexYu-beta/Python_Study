'''
Demo_2 is a simple implementation of factorial calculation
'''
n = int(input('please enter a number: '))
fac = 1
for n in range(n):
    fac = fac * (n + 1)
print('the answer is: ', fac)