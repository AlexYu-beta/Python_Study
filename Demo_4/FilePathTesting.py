'''
this python file collects some simple functions about file path
'''
import os
def list_cwd():
    '''
    print out the list of files and folders in current directory
    :return: list of files and folders
    '''
    return os.listdir(os.getcwd())

def files_cwd():
    '''
    print out the list of files in current directory
    :return: list of files
    '''
    return [p for p in list_cwd() if os.path.isfile(p)]

def folders_cwd():
    '''
    print out the list of folders in current directory
    :return: list of folders
    '''
    return [p for p in list_cwd() if os.path.isdir(p)]

def list_py(path = None):
    '''
    print out the list python files in current directory
    :return: list of files
    '''
    if path == None:
        path=os.getcwd()
    return [fname for fname in os.listdir(path)
            if os.path.isfile(fname) if fname.endswith('.py')]

def file_size_in_byte(fname):
    '''
    get the file size in byte
    :param fname: the file name
    :return: the size of the file in byte
    '''
    return os.stat(fname).st_size

def cwd_size_in_byte():
    '''
    get the current directory size in byte
    :return: the size of current directory in byte
    '''
    count = 0
    for name in files_cwd():
        count = count + file_size_in_byte(name)
    return count