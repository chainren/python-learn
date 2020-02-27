import socket
import time

#创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 5000))

# 接收服务器消息
print(s.recv(1024).decode())

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据
    s.send(data)
    time.sleep(2)
    # 打印接收到的数据
    print(s.recv(1024).decode('utf-8'))
    time.sleep(1)

time.sleep(3)
# 请求退出
s.send(b'exit')
time.sleep(2)
print(s.recv(1024).decode('utf-8'))

# 关闭连接
s.close()