# -- coding: utf-8 --

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 8899))

# 开始监听端口
s.listen(5)
print('Waiting for connection...')


def handler(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        msg = b'Hello, %s' % data.decode('utf-8').encode('utf-8')
        sock.send(msg)
    sock.close()
    print('Connection from %s:%s closed.' % addr)



while True:
    # 接受一个新连接:
    sock, addr = s.accept()

    # w创建新线程处理连接
    t = threading.Thread(target=handler, args=(sock, addr))
    t.start()

