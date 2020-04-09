def my_print(name):
    print(f"welcome {name}, haha")


# my_print("wanglin")


def add(a, b, *arg, **kwargs):
    print("add--arg", arg, kwargs)
    s = 0
    for x in arg:
        s += x
    return s


print(add(2, 5, 8, 9, name="ffl"))
