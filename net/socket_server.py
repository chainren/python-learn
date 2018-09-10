# encoding=utf8

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', '8899'))

# 开始监听端口
s.listen(5)
print('Waitting for connection...')


def handler(sock, addr):
    pass


while True:
    # 接受一个新连接:
    sock, addr = s.accept()

    # w创建新线程处理连接
    t = threading.Thread(target=handler, args=(sock, addr))
    t.start()
