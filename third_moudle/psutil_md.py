# encoding=utf8


# psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块

# 安装： pip install psutil


import psutil

# 获取cpu数
cpu_count = psutil.cpu_count(logical=False)
print(cpu_count)
cpu_times = psutil.cpu_times()
print(cpu_times)


# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
def cpu_usage():
    for x in range(10):
      s = psutil.cpu_percent(interval=1, percpu=True)
      print(s)

# cpu_usage()


# 获取内存信息
print(psutil.virtual_memory()) # 物理内存
print(psutil.swap_memory()) # 交换内存


# 获取磁盘信息
print(psutil.disk_partitions()) # 磁盘分区
print(psutil.disk_usage('C:')) # 磁盘使用情况
print(psutil.disk_io_counters()) #　磁盘IO


#　获取网络信息
print(psutil.net_connections('inet4')) # 网络读写字节
print('\n', psutil.net_if_addrs()) # 网络接口
print('\n', psutil.net_if_stats()) # 网络接口状态


# 获取进程信息
print('\n', psutil.pids()) # 获取所有进程ID

# 获取指定进程
p = psutil.Process(10496)

print('\n')
print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
print(p.username())
print(p.create_time())
# print(p.terminal())
print(p.cpu_times)
print(p.memory_info())
print(p.connections())
print(p.threads())
print('.....')

