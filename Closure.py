# python3 闭包
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

"""——————————————————1、函数对象的作用域————————————————"""
print("""——————————————————1、函数对象的作用域————————————————""")


def line_conf():
    def line(x):
        return 2 * x + 1

    print(line(5))  # within the scope


line_conf()
# print(line(5))      # out of the scope


"""——————————————————2、闭包——————————————————"""
print("""——————————————————2、闭包——————————————————""")


def line_conf2():
    def line2(x):
        return 2 * x + 1

    return line2  # return a function object


my_line = line_conf2()
print(my_line(6))


# 上面的代码可以成功运行。line_conf 的返回结果被赋给line对象。

def line_conf3():
    b = 15

    def line3(x):
        return 2 * x + b  # line定义的隶属程序块中引用了高层级的变量b，但b信息存在于line的定义之外 (
        # 我们称b为line的环境变量。

    return line3  # return a function object


# 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。

b = 5
my_line3 = line_conf3()
print(my_line3(5))
print(my_line3.__closure__)
print(my_line3.__closure__[0].cell_contents)


def line_conf4(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf4(1, 1)
line2 = line_conf4(4, 5)  # 传递函数运行时需要的变量
print(line1(5), line2(5))  # 这两个参数的变化率是不同的 一个变化很频繁 一个变化很少

"""——————————————————3、闭包与并行运算————————————————"""
# 在并行运算的环境下，我们可以让每台电脑负责一个函数，然后将一台电脑的输出和下一台电脑的输入串联起来。
