# -- coding: utf-8 --

# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。

import socket

# SOCK_DGRAM指定了这个Socket的类型是UDP.绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8899))


print('Bind UDP on 8899')
while True:
    # 接收数据
    data, addr = server.recvfrom(1024)
    print('Received from %s:%s' % addr)
    server.sendto(b'Hello %s' % data, addr)