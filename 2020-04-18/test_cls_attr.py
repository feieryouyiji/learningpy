# class Student(object):

#     grade = "one class"

#     def __init__(self, name):
#         self.name = name

# ffl = Student('ffl')

# print(ffl)
# print("name==>",ffl.name)
# print("grade==>",ffl.grade)
# print("Student==>",Student.grade)


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


ffl = Student()
ffl.name = "ffl"
ffl.age = "27"
ffl.gender = "female"
print("ffl,", ffl)
print("age,", ffl.age)
print("gender,", ffl.gender)
