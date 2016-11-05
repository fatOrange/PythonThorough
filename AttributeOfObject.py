# python3 对象的属性
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

# Python一切皆对象(object)，每个对象都可能有多个属性(attribute)。Python的属性有一套统一的管理方案。

"""—————————————————属性的__dict__系统—————————————————"""
print("""—————————————————属性的__dict__系统—————————————————""")


# 对象的属性可能来自于其类定义，叫做类属性(class attribute)。
# 类属性可能来自类定义自身，也可能根据类定义继承来的。
# 一个对象的属性还可能是该对象实例定义的，叫做对象属性(object attribute)。
class bird(object):
    feather = True


class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age


summer = chicken(3)
print(bird.__dict__)  # 对象的属性储存在对象的__dict__属性中。
print()
print(chicken.__dict__)  # __dict__为一个词典，键为属性名，对应的值为属性本身。
print()
print(summer.__dict__)  # 当我们需要调用某个属性的时候，Python会一层层向上遍历，直到找到那个属性。
# (某个属性可能出现再不同的层被重复定义，
# Python向上的过程中，会选取先遇到的那一个，
# 也就是比较低层的属性定义)。

summer.__dict__['age'] = 4
print(summer.__dict__['age'])

summer.age = 5
print(summer.age)
print(summer.__class__.__base__)  # 我们可以利用__class__属性找到对象的类，然后调用类的__base__属性来查询父类

"""—————————————————2、特性—————————————————"""
print("""—————————————————2、特性—————————————————""")
""" 同一个对象的不同属性之间可能存在依赖关系。
    当某个属性被修改时，我们希望依赖于该属性的其他属性也同时变化。
    这时，我们不能通过__dict__的方式来静态的储存属性
    Python提供了多种即时生成属性的方法。
    其中一种称为特性(property)。特性是特殊的属性。
"""


class Cat(object):
    feather = True


class Tiger(Cat):
    fly = False

    def __init__(self, age):
        self.age = age

    def getAdult(self):
        if self.age > 1.0:
            return True
        else:
            return False  # 当对象的age超过1时，adult为True；否则为False：

    adult = property(getAdult)  # property is built-in


summer = Tiger(2)
print(summer.adult)
summer.age = 0.5
print(summer.adult)

""" 特性使用内置函数property()来创建。
    property()最多可以加载四个参数。
    前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。
    最后一个参数为特性的文档，可以为一个字符串，起说明作用。
"""


class num(object):
    def __init__(self, value):
        self.value = value

    def getNeg(self):
        return -self.value

    def setNeg(self, value):
        self.value = -value

    def delNeg(self):
        print("value also deleted")
        del self.value

    neg = property(getNeg, setNeg, delNeg, "I'm negative")  # 前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。


x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg

"""————————————————————3、使用特殊方法__getattr__————————————————————"""


class Dog(object):
    feather = True


class Wolf(Dog):
    fly = False

    def __init__(self, age):
        self.age = age

    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)

"""(Python中还有一个__getattribute__特殊方法，用于查询任意属性。
__getattr__只能用来查询不在__dict__系统中的属性)
__setattr__(self, name, value)和__delattr__(self, name)可用于修改和删除属性。
它们的应用面更广，可用于任意属性。
"""
autumn = Wolf(7)

print(autumn.adult)
autumn.age = 0.5
print(autumn.adult)
