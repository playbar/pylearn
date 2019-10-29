#

class Singleton(object):
    def __init__(self):
        print("test");
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2) #<__main__.Singleton object at 0x004415F0> <__main__.Singleton object at 0x004415F0>

