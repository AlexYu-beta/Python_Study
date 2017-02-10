'''
this python file includes some functions to print contents in a file
WARNING: no exception-dealing
'''
import os
def print_file_by_line(fname):
    '''
    print the file line by line
    :param fname: the filename
    :return: None
    '''
    f = open(fname, 'r')
    for line in f:
        print(line, end='')
    f.close()

def print_file_as_a_whole(fname):
    '''
    print the file directly
    :param fname: the filename
    :return: None
    '''
    f = open(fname, 'r')
    print(f.read())
    f.close()

def write_file_test():
    '''
    a test function that can new a text file and add something in it.
    :return: None
    '''
    fname='test_pythonIO.txt'
    if os.path.isfile(fname):
        print(fname+" already exists!!")
    else:
        f = open(fname, 'w')
        f.write('test here')
        f.write('test there')
        f.close()

def append_file_test(line, fname = 'test_pythonIO.txt'):
    '''
    a test function that can append a line string to a text file
    :param line: the line string
    :param fname: filename
    :return: None
    '''
    f = open(fname, 'a')
    f.write(line)
    f.close()

def top_append_file_test(title, fname = 'test_pythonID.txt'):
    '''
    a test function that can append a title string at the beginning of a text file
    :param title: the title string
    :param fname: filename
    :return: None
    '''
    f = open(fname, 'r+')
    temp = f.read()
    temp = title + '\n\n' + temp
    f.write(temp)
    f.close()