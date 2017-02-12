class student:
    '''
    a simple class to represent students
    '''

    def __init__(self, name = 'Student', age = 21):
        '''
        the constructor with name and age
        :param name: the name of the student
        :param age: the age of the student
        '''
        self.name = name
        self.age = age

    def display_student(self):
        '''
        a user-defined function to display a student
        :return: None
        '''
        print(str(self))

    def display_student_officially(self):
        '''
        a user-defined function to display a student officially
        :return: None
        '''
        print(repr(self))

    def __str__(self):
        '''
        a system-defined function to display a student
        :return: display string
        '''
        return "Student('%s',%d)"%(self.name,self.age)
    """
    def __repr__(self):
        '''
        a system-defined function to display a student officially
        :return: display string
        '''
        return str(self)
    """