# python3 装饰器
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

"""装饰器是一种高级Python语法。装饰器可以对一个函数、方法或者类进行加工。"""

"""———————————————————1、装饰函数和方法————————————————"""

print("""———————————————————1、装饰函数和方法————————————————""")


# get square sum
def square_sum(a, b):
    return a ** 2 + b ** 2


# get square diff
def square_diff(a, b):
    return a ** 2 + b ** 2


print(square_sum(3, 4))
print(square_diff(3, 4))


# 在拥有了基本的数学功能之后，我们可能想为函数增加其它的功能
# modify: print input
# 比如打印输入。我们可以改写函数来实现这一点：
# get square sum
def square_sum2(a, b):
    print("input:", a, b)
    return a ** 2 + b ** 2


# get square diff
def square_diff2(a, b):
    print("input:", a, b)
    return a ** 2 - b ** 2


print(square_sum2(3, 4))
print(square_diff2(3, 4))


# 现在，我们使用装饰器来实现上述修改：
def decorator(F):
    def new_F(a, b):
        print("input:", a, b)
        return F(a, b)

    return new_F


# get square sum
@decorator  # 在函数square_sum和square_diff定义之前调用@decorator，我们实际上将square_sum或square_diff传递给decorator
def square_sum3(a, b):
    return a ** 2 + b ** 2  # 并将decorator返回的新的可调用对象赋给原来的函数名(square_sum或square_diff)


# get square diff
@decorator  # 在函数square_sum和square_diff定义之前调用@decorator，我们实际上将square_sum或square_diff传递给decorator
def square_diff3(a, b):
    return a ** 2 - b ** 2  # 并将decorator返回的新的可调用对象赋给原来的函数名(square_sum或square_diff)
    # 装饰器可以用def的形式定义


print(square_sum3(3, 4))
print(square_diff3(3, 4))

square_sum4 = decorator(square_sum3)  # square_sum4 = new_F F = square_sum3
print(square_sum4(3, 4))  # new_F(3,4) F=square_sum3(3,4)

"""_____________________2、含参的装饰器_________________"""

print("""_____________________2、含参的装饰器_________________""")


# a new wrapper layer
def pre_str(pre=''):
    # old decorator
    def decorator2(F):
        def new_F(a, b):
            print(pre + "input", a, b)
            return F(a, b)

        return new_F

    return decorator2


# get square sum
@pre_str('^_^')
def square_sum5(a, b):
    return a ** 2 + b ** 2


# get square diff
@pre_str('T_T')
def square_diff5(a, b):
    return a ** 2 - b ** 2


print(square_sum5(3, 4))
print(square_diff5(3, 4))
# 上面的pre_str是允许参数的装饰器。
# 它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
# 我们可以将它理解为一个含有环境参量的闭包。

"""——————————————————————————3、装饰类————————————————————————"""
print("""——————————————————————————3、装饰类————————————————————————""")


# 在Python 2.6以后，装饰器被拓展到类。
# 一个装饰器可以接收一个类，并返回一个类，从而起到加工类的效果。

def decorator2(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aClass(age)

        def display(self):
            self.total_display += 1
            print("total display", self.total_display)

    return newClass


@decorator2  # newClass = decorator2(Bird)
class Bird:
    def __init__(self, age):
        self.age = age


eagleLord = Bird(5)  # newClass(5)
for i in range(3):      # 装饰器与闭包关系严密
    eagleLord.display()  # 类里面的方法装饰器里不一定要有
