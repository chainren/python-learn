 #### 1. selenium 的环境搭建
```
pip install -U selenium
```

#### 2. 安装浏览器驱动
对于 Selenium 3，要使用其功能，我们需要安装浏览器驱动。每个浏览器厂家都有自己的驱动，本文以 Chrome 浏览器为例，向大家介绍怎么安装浏览器驱动。
Chrome 的每个浏览器版本都会有对应版本的驱动， 所以我们第一步是要知道我们浏览器的版本。Chrome 浏览器的版本信息在“设置->关于 Chrome”里面可以找到.
找到浏览器版本后，我们到 http://chromedriver.storage.googleapis.com/index.html 下载对应的 chromedriver 。以前的老版本都是2.x的版本，大家需要到网上搜一下版本对应关系。Chrome 从版本70之后就很好找了，所以建议大家将 Chrome 版本升级至最新的，驱动也好找些。

下载完成后，解压压缩包，会得到 chromedriver 的驱动。不同的操作系统有不同的安装方式：
Windows 操作系统的安装关键步骤是：
>① 把下载成功的驱动包chromedriver.exe解压出来，放在谷歌浏览器安装目录下的Application目录中（鼠标右键点击谷歌图标，选择属性，可在起始位置查看谷歌目录）。

>② 然后配置系统环境变量在path中添加chromedriver.exe的路径。

>③ 将chromedriver.exe放在C盘中windows文件夹下的SysWOW64，如果是32位系统则放在System32中。

笔者用的是 Mac 操作系统， Mac 系统安装驱动在网上搜索可以搜到两种方法：第一种是将 chromedriver 复制到 /usr/bin 目录下， 另一种是将 chromedriver 复制到 /usr/local/bin 目录下。
笔者采取的是第二种方案，因为第一种方案存在一个问题：Mac 对 /usr/bin 这个路径有权限的限制，即使你是 root 用户，也无法正常移动文件过去，这时，需关闭 Mac 的 SIP 方法 ，具体操作可参考：https://jingyan.baidu.com/article/e5c39bf5d13bf939d76033cf.html 。
至于网上说的将 chromedriver 驱动文件复制到 /usr/bin 或者 /usr/local/bin 后，需要在环境变量里面配置相应的目录，笔者试过不配置也没问题，当然配置了也不会出问题，所以为了省事，可以不用配置。
接下来，我们在命令行输入如下命令就可以查看我们的 chromedriver 版本了：
```
chromedriver --version
```
返回版本信息：
```
ChromeDriver 75.0.3770.140 (2d9f97485c7b07dc18a74666574f19176731995c-refs/branch-heads/3770@{#1155})
```

看到这个就表示 Chrome 驱动安装成功了。
现在我们来用最简单的语句测试一下，看能不能运行 Selenium：
```
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
```

我们会看到弹出一个浏览器，并打开了百度首页，这就代表我们的程序正常运行了，我们的环境配置成功了。