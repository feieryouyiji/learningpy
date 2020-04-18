class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __call__(self):
        print('My name 111111111is %s.' % self.name)


print("-----------------------")
ffl = Student('ffl')
print("ffl-->", ffl)
print("ffl-11->", ffl())


# f = lambda:34
# print(f)
# print(f())

