# python3
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

"""———————————————————内存管理————————————————"""
print("""———————————————————内存管理————————————————""")
# 这里以Python语言为例子，说明一门动态类型的、面向对象的语言的内存管理方式。
a = 1

print(id(a))
print(hex(id(a)))
# 整数1为一个对象。而a是一个引用。Python是动态类型的语言(参考动态类型)，对象与引用分离

# 在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用。
a = 1
b = 1
print(id(a))
print(id(b))
"""可见a和b实际上是指向同一个对象的两个引用。"""

# True
a = 1
b = 1
print("int is same?", a is b)

# True
a = "good"
b = "good"
print("String is same?", a is b)

# True
a = "very good morning"
b = "very good morning"
print("String is same?", a is b)

# False
a = []
b = []
print("list is same?", a is b)

# True
a = 1.1
b = 1.1
print("float is same?", a is b)

# True
a = 1e10
b = 1e10
print("long is same?", a is b)

# 在Python中，每个对象都有存有指向该对象的引用总数，即引用计数(reference count)。
# 我们可以使用sys包中的getrefcount()，来查看某个对象的引用计数。

from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = a
print(getrefcount(b))
# 需要注意的是，当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用。
# 因此，getrefcount()所得到的结果，会比期望的多1。

"""————————————————————2、对象引用对象——————————————————"""


class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj


b = [1, 2, 3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))
# 可以看到，a引用了对象b。

from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = [a, a]
print(getrefcount(a))

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

"""————————————————————引用减少————————————————————"""
print("""————————————————————引用减少————————————————————""")
from sys import getrefcount

# 比如，可以使用del关键字删除某个引用:
a = [1, 2, 3]
b = a
print(getrefcount(b))
del a
print(getrefcount(b))
# del也可以用于删除容器元素中的元素，比如:
a = [1, 2, 3]
del a[0]
print(a)

a = [1, 2, 3]
b = a
print(getrefcount(b))

a = 1
print(getrefcount(b))

"""————————————————————4、垃圾回收————————————————————"""
# 我们可以通过gc模块的get_threshold()方法，查看垃圾回收阈值:
import gc
# (700, 10, 10)
# 后面的两个10是与分代回收相关的阈值，后面可以看到。
# 700即是垃圾回收启动的阈值。可以通过gc中的set_threshold()方法重新设置。
print(gc.get_threshold())
# 手动启动垃圾回收
gc.collect()
