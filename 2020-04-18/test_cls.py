class Animal(object):
    def run(self):
        print('Animal is running...')


class Cat(Animal):
    def run(self):
        print("I am cat, i am running")


class Dog(Animal):
    def run(self):
        print("I am dog, i am running")


cat = Dog()
print("cat--->", cat)
print("cat--->", cat.run())

res = isinstance(cat, Animal)
print("isinstance-->", res)
print("type-->", type(cat))


print(getattr(cat, "name", '404'))