import os, psutil

# 打印当前程序占用的内存大小
def print_memory_info(name):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    MB = 1024 * 1024
    memory = info.uss / MB
    print('%s used %d MB' % (name, memory))

# 测试函数
def foo():
    print_memory_info("foo start")
    length = 1000 * 1000
    list = [i for i in range(length)]
    print_memory_info("foo end")
    return list

# 演示循环引用时，引用计数算法的垃圾收集问题： 无法被作为垃圾回收
def foo1():
    print_memory_info("foo start")
    length = 1000 * 1000
    list_a = [i for i in range(length)]
    list_b = [i for i in range(length)]
    list_a.append(list_b)
    list_b.append(list_a)
    print_memory_info("foo end")
    return list


list = foo()
print_memory_info("main end")