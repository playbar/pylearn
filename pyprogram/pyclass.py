# coding=utf-8
from os.path import join

__metaclass__ = type

# 类型定义
# 实例方法必的第一个参数代表类型实例，类似其他语言的this。
class Animal:
    name = "未知" # 属性定义。

    def __init__(self, name): #构造方法定义。
       self.name = name

    def getName(self): # 实例方法定义。
        return self.name

    def setName(self, value):
        self.name = value

print(Animal.name) # 未知
print(Animal.__dict__["name"]) # 未知

animal = Animal("狗狗")
print(animal.__dict__);
print(animal.name) # 狗狗
print(animal.__dict__["name"]) # 狗狗
print(Animal.name) # 未知
print(Animal.__dict__["name"]) # 未知
print(animal.__class__.name) # 未知
print(animal.__class__.__dict__["name"]) # 未知

class TestClass:
    __private_property = 0

    def __private_method(self):
        pass

# print(TestClass.__dict__);

# 多重继承
class Base1:
    pass


class Base2:
    pass


class Child(Base2, Base1):
    pass


child = Child()
print(isinstance(child, Child))  # True
print(isinstance(child, Base2))  # True
print(isinstance(child, Base1))  # True


# 调用父类
class Base:
    def say(self):
        print("Base")


class Child(Base):
    def say(self):
        Base.say(self)
        super(Child, self).say()
        print("Child")


child = Child()
child.say()


class FileObject:
    '''Wrapper for file objects to make sure the file gets closed on deletion.'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


class Word(str):
    '''Class for words, defining comparison based on word length.'''

    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an immutable
        # type, so we have to initialize it early (at creation)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]  # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


print(Word("duan") > Word("wei"))


class AccessCounter:
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''

    def __init__(self, value):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', value)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Make this unconditional.
        # If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # get the first element
        return self.values[0]

    def tail(self):
        # get all elements after the first
        return self.values[1:]

    def init(self):
        # get elements up to the last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # get all elements except first n
        return self.values[n:]

    def take(self, n):
        # get first n elements
        return self.values[:n]


class Entity:
    '''Class to represent an entity. Callable to update the entity's position.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Change the position of the entity.'''
        self.x, self.y = x, y
        print(x, y)


entity = Entity(5, 1, 1)
entity(2, 2)


class Closer:
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        print("清理完成")
        return True;


with Closer() as closer:
    pass


class Meter(object):
    '''Descriptor for a meter.'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    '''Descriptor for a foot.'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    '''Class to represent distance holding two descriptors for feet and
    meters.'''
    meter = Meter()
    foot = Foot()

class Animal:
    from pyprogram.playable import play

animal = Animal();
animal.play();


class TestClass:
    def method1(self):
        print("方法1")


def method2(self):
    print("方法2")


test = TestClass()
TestClass.method2 = method2

test.method1()  # 方法1
test.method2()  # 方法2


TestClass = type("TestClass", (object,), {
    "say": lambda self : print("你好啊")
})

test = TestClass()
test.say()


def getter(name):
    def getterMethod(self):
        return self.__getattribute__(name)

    return getterMethod


def setter(name):
    def setterMethod(self, value):
        self.__setattr__(name, value)

    return setterMethod


class TestClass:
    getName = getter("name")
    setName = setter("name")


test = TestClass()
test.setName("段光伟")
print(test.getName())


print("finish");