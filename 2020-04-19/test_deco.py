
def log(time):
    def decorate(func)
        def wrapper(*args, **kwargs):
            print("i want to log you", args)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@log
def now():
    print('2015-3-25')

now()