class MyDict(dict):
    def __init__(self, **kwargs):
        super(MyDict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def __str__(self):
        return f' i am fake dict'


# mydict = MyDict(name="ffl", age=23)
# print("mydict==>", mydict)
# print("type==>", type(mydict))
