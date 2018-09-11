# encoding=utf8

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1', 8899))

# 接收消息
wel = s.recv(1024).decode('utf-8')
print(wel)

# 发送消息
for data in (b'Michael', b'Tracy', b'Sarah'):
    s.send(data)
    back = s.recv(1024).decode('utf-8')
    print(back)
s.send(b'exit')
s.close()

