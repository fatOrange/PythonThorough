# python3 作业
#  _*_ coding: utf-8 _*_
# _author_ = 'YourName'

# 通过闭包对一个数据 x 做“流水线操作”，至少三层闭包，每一层依次进行一项操作，（如先求绝对值，再开方，再求相反数）。

def absa(x):
    def squ(x):
        def oppo(x):
            x *= -1
            return x

        x *= x
        return oppo(x)

    if x < 0:
        x = x * -1
    return squ(x)
print (absa(4))


def xf(F):
    def new_F(x):
        return 