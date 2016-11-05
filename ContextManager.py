# python3 上下文管理器
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

"""——————————————————关闭文件——————————————————"""
print("""——————————————————关闭文件——————————————————""")
# without context manager
f = open("new.txt", "w")
print(f.closed)  # whether the file is open
f.write("Hello World!")
f.close()
print(f.closed)

# with context manager
with open("new2.txt", "w") as f:  # 两段程序实际上执行的是相同的操作。
    print(f.closed)  # 我们的第二段程序就使用了上下文管理器 (with...as...)。
    f.write("Hello World!")  # 上下文管理器有隶属于它的程序块。
print(f.closed)

# 当隶属的程序块执行结束的时候(也就是不再缩进)，
# 上下文管理器自动关闭了文件 (我们通过f.closed来查询文件是否关闭)。
# 我们相当于使用缩进规定了文件对象f的使用范围。
#
#
# 当我们使用上下文管理器的语法时，
# 我们实际上要求Python在进入程序块之前调用对象的__enter__()方法，在结束程序块的时候调用__exit__()方法。
# 对于文件对象f来说，它定义了__enter__()和__exit__()方法(可以通过dir(f)看到)。
# 在f的__exit__()方法中，有self.close()语句。

"""——————————————————自定义——————————————————"""
print("""——————————————————自定义——————————————————""")


# customized object
class VOW(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "I say: " + self.text  # add prefix
        return self  # note: return an object

    # __enter__()
    # 返回一个对象。上下文管理器会使用这一对象作为as所指的变量，也就是myvow。在__enter__()
    # 中，我们为myvow.text增加了前缀("I say: ")。在__exit__()
    # 中，我们为myvow.text增加了后缀("!")。


    def __exit__(self, exc_type, exc_val, exc_tb):  # 的参数中exc_type, exc_value, traceback用于描述异常。
        self.text += "!"  # add suffix

        # 注意: __exit__()
        # 中有四个参数。当程序块中出现异常(exception)，__exit__()
        # 的参数中exc_type, exc_value, traceback用于描述异常。
        # 我们可以根据这三个参数进行相应的处理。如果正常运行结束，这三个参数都是None。
        # 在我们的程序中，我们并没有用到这一特性。

# 由于上下文管理器带来的便利，它是一个值得使用的工具。
with VOW("I'm fine") as myvow:  # 我们可以看到，在进入上下文和离开上下文时，
    # 对象的text属性发生了改变(最初的text属性是"I'm fine")。
    print(myvow.text)
print(myvow.text)
