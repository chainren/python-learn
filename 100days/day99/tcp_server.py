import socket

import threading
import time


def tcplink(sock, addr):
    print("Accept new connection from %s:%s" % addr)
    # 向客户端发送欢迎消息
    sock.send(b'Server: Welcome!\n')
    while True:
        sock.send(b"Server: What's your name?")
        data = sock.recv(1024)
        if data == b'exit':
            sock.send(b"Server: Good bye!\n")
            break
        sock.send(b"Server: Hello %s!\n" % data)

    time.sleep(5)
    # 关闭连接
    sock.close()
    print("Connection from %s:%s is closed" % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip、port
s.bind(('127.0.0.1', 5000))

# 开始监听
s.listen(5)

print("Waiting for connection...")

# 循环接收客户端连接
while True:
    # 接受一个新连接
    socket, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(socket, addr))
    t.start()
