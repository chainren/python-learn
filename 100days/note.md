#### 1. 安装flask-sqlalchemy
```
pip install flask-sqlalchemy
```

#### 2. 如果连接mysql，需安装flask-mysqldb
```
pip install flask-mysqldb
```

安装可能报错
```
Installing collected packages: mysqlclient
    Running setup.py install for mysqlclient ... error
    ERROR: Command errored out with exit status 1:
    building 'MySQLdb._mysql' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ 
    ...
    Build Tools": https://visualstudio.microsoft.com/downloads/
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'c:\users\chenr\appdata\local\programs\python\python37-32\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\chenr\\AppData\\Local\\Temp\\pip-install-c_uq3fo4\\mysqlclient\\setup.py'"'"'; __file__='"'"'C:\\Users\\chenr\\AppData\\Local\\Temp\\pip-install-c_uq3fo4\\mysqlclient\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\chenr\AppData\Local\Temp\pip-record-y3asnbp4\install-record.txt' --single-version-externally-managed --compile Check the logs for full command output.
```
需要安装一个sqlclient支持库     
去(https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python)下载一个对应python版本的mysqlclient     
我这里选择的是：[mysqlclient‑1.4.6‑cp37‑cp37m‑win32.whl]()

然后进行安装
```
pip install mysqlclient‑1.4.6‑cp37‑cp37m‑win32.whl
```
安装完成后，再安装flask-mysqldb即可

