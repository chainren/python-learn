# coding=utf8

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    client.sendto(data, ('127.0.0.1', 8899))
    # 接收数据
    print(client.recv(1024).decode('utf-8'))
#关闭连接
client.close()
