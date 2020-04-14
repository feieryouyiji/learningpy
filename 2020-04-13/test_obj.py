# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


fyp = Student('fyp', 59)
print("fyp===>", fyp)
print("fyp===>", fyp.name)
print("fyp===>", fyp.score)
