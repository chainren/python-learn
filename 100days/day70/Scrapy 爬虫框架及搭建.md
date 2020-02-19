# Scrapy 框架实现爬虫的基本原理

Scrapy 就是封装好的框架，你可以专心编写爬虫的核心逻辑，无需自己编写与爬虫逻辑无关的代码，套用这个框架就可以实现以上功能——爬取到想要的数据。如果暂时理解不深也没关系，后边会结合实例具体介绍。

# Python 爬虫基本流程

## A 发起请求———B 解析内容———C 获取响应内容———D 保存数据

A 通过 HTTP 向目标站点发起请求，即发送一个 Request ，请求可以包含额外的 headers 等信息，等待服务器响应。

B 得到的内容可能是 HTML ，可以用正则表达式、网页解析库进行解析。可能是 Json ，可以直接转为 Json 对象解析，可能是二进制数据，可以做保存或者进一步的处理。

C 如果服务器能正常响应，会得到一个 Response ， Response 的内容便是所要获取的页面内容，类型可能有 HTML ， Json 字符串，二进制数据（如图片视频）等类型。

D 保存形式多样，可以存为文本，也可以保存至数据库，或者保存特定格式的文件。

搭建自己本机环境如下：Windows7 64bit———Python3.7———Pycharm64

## 安装 Python———安装 Pycharm———安装 Scrapy———新建爬虫项目

简单解释：将 Python 比作 Java ，那么 Pycharm 就相当于 eclipse ， Pycharm 就是 Python 语言的运行环境 IDE 工具。

# 安装 Python

在 Python 的官网 www.python.org 中找到最新版本的 Python 安装包，点击进行下载，请注意，当你的电脑是32位的机器，请选择32位的安装包，如果是64位的，请选择64位的安装包；

我自己机器是 win7 64bit 所以我下载的是 python-3.7.4.amd64.exe，其中的 add python 3.7 to PATH 一定要勾选。

另外安装 python 路径不要有中文和空格，避免以后麻烦。后边就点击下一步即可。

如果忘记勾选则需要手动添加环境变量：（需要添加两个：c:\python3.7.0;c:\python3.7.0\Scripts）

右键计算机——点击属性——点击高级系统设置——高级——环境变量——用户变量——PATH  添加自己安装 python 的路径。

# 安装 Pycharm

本篇对于环境的搭建只是起到抛砖引玉的作用，建议大家以下边做参考。

https://www.runoob.com/w3cnote/pycharm-windows-install.html

# 安装 Scrapy

由于安装 Scrapy 不是本系列重点，所以仅展示 Windows 系统上安装 Scrapy 的步骤。注意：一定按顺序安装。Cmd 进入 dos 窗口：

```
C:\Users\Administrator>python
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
C:\Users\Administrator>python -m pip -V
pip 19.0.3 from c:\python3.7.0\lib\site-packages\pip (python 3.7)  
1.python -m pip install --upgrade pip
2.python -m pip install Twisted-18.9.0-cp37-cp37m-win_amd64.whl
3.python -m pip install pypiwin32
4.python -m pip install scrapy
5.python -m pip install requests
```

如果中途安装遇到问题请及时 Google 查阅资料，查阅就是积累的过程。

# Scrapy 创建新项目：

Pycharm 中用 alt+F12 切换到命令行，在命令行输入：

```
E:\>scrapy startproject peilv
```

创建项目可能报错：

```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: 'd:\\devsoft\\python\\python38-32\\Lib\\site-packages\\cryptography\\hazmat\\bindings\\_openssl.cp38-win32.pyd'
```

需要安装cryptography

```
pip install -I cryptography --user
```



就会生成 Scrapy 项目，项目名称是 peilv ，结构如下：主要改写2个文件：“items、settings”，新增2个文件：“爬虫主程序”、itemcsvexporter。

```
peilv
scrapy.cfg                     #创建项目时自动生成，项目的配置文件
peilv/
    __init__.py                #创建项目时自动生成，无需任何改动
    items.py                   #创建项目时自动生成，定义爬取的字段    
    pipelines.py               #创建项目时自动生成，如存入文件，无需任何改动    
    settings.py                #创建项目时自动生成，将爬取字段按顺序输出    
    middlewares.py             #创建项目时自动生成，无需任何改动    
    spiders/   
        __init__.py            #创建项目时自动生成，无需任何改动	
	itemcsvexporter.py     #需自己编写，代码固定	
        爬虫主程序.py          #需自己编写，爬虫的主程序
```