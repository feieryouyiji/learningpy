
class my_cls():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self, action_name):
        print(f"{self.name}正在玩{action_name}")


ffl = my_cls("ffl", 27)
ffl.play("basketball")

print(ffl.name)
