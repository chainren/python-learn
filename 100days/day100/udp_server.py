import socket

# 创建socket
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip、端口
sk.bind(('127.0.0.1', 5000))

while True:
    # 接收数据报
    msg, addr = sk.recvfrom(1024)
    # 打印
    print('来自[%s:%s]的消息: %s' % (addr[0], addr[1], msg.decode('utf-8')))

    # 等待输入
    inp = input('>>>')

    # 发送数据报
    sk.sendto(inp.encode('utf-8'), addr)

# 关闭socket
sk.close()
