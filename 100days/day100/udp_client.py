import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器ip，port
addr = ('127.0.0.1', 5000)

while True:
    # 控制台输入
    msg = input('>>>')
    
    if msg == 'exit':
        break

    # 发送数据报
    sk.sendto(msg.encode('utf-8'), addr)

    # 接收数据报
    msg_recv, addr = sk.recvfrom(1024)

    # 打印
    print(msg_recv.decode('utf-8'))

# 关闭
sk.close()