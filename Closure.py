# python3 闭包
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

"""——————————————————1、函数对象的作用域————————————————"""


def line_conf():
    def line(x):
        return 2 * x + 1

    print(line(5))  # within the scope


line_conf()
# print(line(5))      # out of the scope
