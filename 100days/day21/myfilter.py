# 自定义过滤器
# 过滤器实质就是个函数，所以，第一定义一个过滤器函数，第二，注册到Jinjia2的过滤器中。

# 求字符长度
def mylen(str):
    return len(str)

# 超出长度后的字符显示省略号
def omit(str, max):
    sub = str[0: max]
    return "%s..." % sub
