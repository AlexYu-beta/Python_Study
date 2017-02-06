'''
Demo_1.py is the very first start of my Python Self-study demonstration
a simple implementation of I/O operation
from "Python: Visual Quick Start Guide"
'''
name = raw_input("please enter your name: ")
'''
it seems that function input() is more strict in grammar
in this case when entering a "string" like a name, you should add '' to make it a string
but if we use the function raw_input() instead, we can get rid of such trouble
'''
print('Hello ' + name.capitalize() + '!')