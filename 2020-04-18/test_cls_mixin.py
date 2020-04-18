class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eating(self):
        print(f"{self.name}...正在吃饭")


class ConnectMixIn(object):
    pass


class Son(Father, ConnectMixIn):
    pass