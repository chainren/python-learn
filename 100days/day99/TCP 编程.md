网络连接与通信是我们学习任何编程语言都绕不过的知识点。Python 也不例外，本文就介绍因特网的核心协议 TCP ，以及如何用 Python 实现 TCP 的连接与通信。

## TCP 协议

TCP协议（Transmission Control Protocol， 传输控制协议）是一种面向连接的传输层通信协议，它能提供高可靠性通信，像 HTTP/HTTPS 等网络服务都采用 TCP 协议通讯。那么网络通讯方面都会涉及到 socket 编程，当然也包括 TCP 协议。

## Network Socket

我们来看看定义：

> Network Socket（网络套接字）是计算机网络中进程间通信的数据流端点，广义上也代表操作系统提供的一种进程间通信机制。

这些计算机术语都很学术，难于理解，每个字都认识，加在一起就不认识了。我们可以通俗地理解成发快递：A 需要给 B 寄快递，首先需要知道 B 的地址和手机号码，那么这个地址就相当于 网络中的主机 IP 地址，而手机就相当于 主机的端口号。然后 A 还需要指定哪家快递公司，是顺丰还是中通？这个快递公司就相当于通信的传输协议。

## TCP 连接流程

上述快递的例子中，寄快递的我们可以叫做客户端，收快递的我们叫做服务器。专业点就是主动发起连接的一方叫做客户端，被动响应的一方叫做服务器。例如，我们在浏览器中访问百度搜索时，我们自己的电脑就是客户端，浏览器会向百度的服务器发送连接请求，如果百度的服务器接受了我们的请求，那么一个 TCP 连接就建立起来了，后面就是百度向我们传输搜索结果了。

我们来看一个流程图：

![img](https://mmbiz.qpic.cn/mmbiz_png/SAy0yVjKWyxlibdNv9SAs9FLHAHQuNJtOJbIaZXT2lXz3O7qjib2FFT9eicZ6m3utqibzQn3tuBFRicPhlAG1ruOOyg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

TCP服务器的建立可以归纳这几步：

- 创建 socket（套接字）
- 绑定 socket 的 IP 地址和端口号
- 监听客户端的连接请求
- 接受客户端的连接请求
- 与客户端对话
- 关闭连接

TCP客户端的创建可总结为这几步：

- 创建 socket（套接字）
- 连接服务器 socket
- 与服务器对话
- 关闭连接

这里需要注意的是 TCP 客户端连接到服务器的 IP 和端口号必须是 TCP 服务器的 IP 和监听的端口号，服务器调用 listen() 开始监听端口，然后调用 accept() 时刻准备接受客户端的连接请求，此时服务器处于阻塞状态，直到服务器监听到客户端的请求后，接收请求并建立连接为止。

### TCP 客户端

创建 socket 连接，可以这样做：

```python
# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(("127.0.0.1", 6000))
```

创建 socket 时，第一个参数 socket.AF_INET 表示指定使用 IPv4 协议，如果要使用 IPv6 协议，就指定为 socket.AF_INET6。SOCK_STREAM 指定使用面向流的 TCP 协议。然后我们调用 connect() 方法，传入 IP 地址（或者域名），指定端口号就可以建立连接了。

接下来我们就可以向服务器发送数据了：

```
s.send(b'Hello, Mr Right!')
```

接收数据时，调用 recv(max) 方法，一次最多接收指定的字节数，因此，在一个 while 循环中反复接收，直到 recv() 返回空数据，表示接收完毕，退出循环。

```python
# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
```

最后，我们需要关闭连接，很简单：

```
s.close()
```

### TCP 服务器

相比于客户端，服务器端稍微复杂一些，需要先绑定一个 IP 地址和端口号，然后监听客户端的请求，收到请求后丢到一个线程去处理。

创建 socket 跟客户端方法一样：

```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

接下来需要绑定监听地址和端口：

```
s.bind(('127.0.0.1', 6000))
```

然后就可以开始监听端口了，监听时需要传入一个参数，指定等待连接的最大数量：

```
s.listen(5)
```

接下来就是无限循环等待客户端的连接，直到有连接请求过来，就用一个线程去处理：

```python
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
```

这里为什么需要多线程处理呢？想象一下菜鸟驿站，如果里面只有一个人的话，那么多个人寄件就需要排队，一个个来；但是如果有多个人的话，那么每个人都可以处理一个寄件请求。

我们来看一下处理客户端请求的方法：

```python
# 处理tcp连接
def tcplink(conn, addr):
    print("Accept new connection from %s:%s" % addr)
    # 向客户端发送欢迎消息
    conn.send(b"Server: Welcome!\n")
    while True:
        conn.send(b"Server: What's your name?")

        data = conn.recv(1024)
        # 如果客户端发送 exit 过来请求退出，结束循环
        if data == b"exit":
            conn.send(b"Server: Good bye!\n")
            break
        conn.send(b"Server: Hello %s!\n" % data)

    # 关闭连接
    conn.close()
    print("Connection from %s:%s is closed" % addr)
```

例子中，我们先想客户端发送欢迎消息，然后询问客户端名称，收到名称后发送欢迎消息，直到接收到客户端的 'exit' 命令，退出循环，关闭连接。

## 实例

我们把上面的分步讲解代码合并起来，形成一个可运行的实例。

服务器端代码：

```python
import socket
import threading
import time

# 处理tcp连接
def tcplink(conn, addr):
    print("Accept new connection from %s:%s" % addr)
    # 向客户端发送欢迎消息
    conn.send(b"Server: Welcome!\n")
    while True:
        conn.send(b"Server: What's your name?")

        data = conn.recv(1024)
        # 如果客户端发送 exit 过来请求退出，结束循环
        if data == b"exit":
            conn.send(b"Server: Good bye!\n")
            break
        conn.send(b"Server: Hello %s!\n" % data)

    time.sleep(5)
    # 关闭连接
    conn.close()
    print("Connection from %s:%s is closed" % addr)


# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(("127.0.0.1", 6000))
# 设定等待连接的最大数量为5
s.listen(5)
print("Waiting for connection...")
# 等待接收连接
while True:
    # 接受一个新连接
    conn, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()
```

客户端代码：

```python
import socket
import time

# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(("127.0.0.1", 6000))

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
```

注意，在代码中，我加入了一些休眠（sleep）操作，主要是为了控制台能够顺利打印出来，不然程序运行太快，打印顺序和内容有可能和预期不一样。

先运行服务器端代码，然后再运行客户端代码，我们可以看到服务器端控制台打印内容如下：

```
# 服务器端打印消息
Waiting for connection...
Accept new connection from 127.0.0.1:53503
Connection from 127.0.0.1:53503 is closed
```

客户端控制台打印内容如下：



```
# 客户端打印消息
Server: Welcome!
Server: What's your name?
Server: Hello Michael!
Server: What's your name?
Server: Hello Tracy!
Server: What's your name?
Server: Hello Sarah!
Server: What's your name?
Server: Good bye!
```

大家可以对照着打印内容和代码，体会一下服务器端和客户端通信的原理。

## 总结

本文为大家介绍了 TCP 编程的基本原理和如何使用 Python 实现一个最简单的 TCP 通信过程。通过介绍和实例，大家要在脑海中形成一个 TCP 通信的过程，熟悉了这个过程是处理后续复杂通信需求的基础。