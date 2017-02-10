'''
An example from the textbook "Python: Visual QuickStart Guide"
A collection of functions for printing simple shapes
'''

CHAR = '*'

def rectangle(height,width):
    """
    this function prints a rectangle
    :param height: the height of the rectangle
    :param width: the width of the rectangle
    :return: None
    >>> rectangle(5,1)
    *
    *
    *
    *
    *
    """
    for row in range(height):
        for column in range(width):
            print(CHAR, end = '')
        print()

def square(side):
    """
    this function prints a square
    :param side: the side of the square
    :return: None
    >>> square(1)
    *
    """
    rectangle(side,side)

def triangle(height):
    """
    print a specific-shaped triangle
    :param height: the height of the triangle
    :return: None
    """
    for row in range(height):
        for column in range(1,row+2):
            print(CHAR, end = '')
        print()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
