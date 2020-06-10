### Xpath和lxml
XPath 全称为 Xml Path Language，即 Xml 路径语言，是一种在 Xml 文档中查找信息的语言。它提供了非常简洁的路径选择表达式，几乎所有的节点定位都可以用它来选择。      
XPath 可以用于 Xml 和 Html，在爬虫中经常使用 XPath 获取 Html 文档内容。     
lxml 是 Python 语言用 Xpath 解析 XML、Html文档功能最丰富的、最容易的功能模块。


### XPath术语
在 XPath 中有七种节点分别是元素、属性、文本、文档、命名空间、处理指令、注释，前3种节点为常用节点    
请看下面的 Html 例子，(注：这个例子全文都需要使用)
```html
<!DOCTYPE html>
<html>
    <body>
        <div>
            <!-- 这里是注释 -->
            <h4>手机品牌商<span style="margin-left:10px">4</span></h4>
            <ul>
               <li>小米</li>
               <li>华为</li> 
               <li class='blank'> OPPO </li>
               <li>苹果</li>
            </ul>
        </div>
        <div>
            <h4>电脑品牌商<span style="margin-left:10px">3</span></h4>
            <ul class="ul" style="color:red">
                <li>戴尔</li> 
                <li>机械革命</li> 
                <li>ThinkPad</li>
            </ul>
        </div>
    </body>
</html>
```
在上面的例子中
```
<html> 为文档节点
<li>小米</li> 为元素节点
class='blank' 为属性节点
<!-- 这里是注释 --> 为注释节点
```

#### 节点关系
在 XPath中有多中节点关系分别是父节点、子节点、同胞节点、先辈节点、后代节点      
在上面的例子中
1. 父节点：每个元素以及属性都有一个父节点，如：div 节点的父节点是 body 节点
2. 子节点：元素节点可有零个、一个或多个子节点，如：第一个 ul 节点的子节点是4个 li 节点
3. 同胞节点：拥有相同的父节点的节点，如：两个 div 节点是同胞节点
4. 先辈节点：某节点的父节点、父节点的父节点...，如：ul 节点的先辈节点有 div 节点、body 节点
5. 后代节点：某个节点的子节点，子节点的子节点...，如：body 节点的后代节点有div 节点、ul 节点、li 节点

XPath 语法

基本语法

|表达式  |	描述  |
| ----- | ------ |
| nodeName |	选择nodeName节点的所有子节点 |
| /	    |   从根节点开始 | 
|//	    | 从匹配的节点开始选择节点 | 
|.	    | 选择当前节点 | 
|..	    | 选择当前节点的父节点 | 
|@	    | 选择元素 | 
|*	    | 匹配任意元素节点 | 
|@*	    | 匹配任意属性节点 | 

用上面的 Html 文档举个例子

| 路径表达式 | 描述                                  |
| :--------- | :------------------------------------ |
| body       | 选取 body 的所有子节点                |
| /html      | 选取 html 节点                        |
| //div      | 选取所有 div 节点                     |
| //div/./h4 | div 节点下的 h4 节点                  |
| ../div     | 选取当前节点的父节点下的所有 div 节点 |
| //@class   | 所有带有 class 元素的节点             |
| //*        | 选择所有节点                          |
| //@*       | 选择所有属性节点                      |


#### 常用函数
| 表达式                            | 描述                                                        |
| :-------------------------------- | :---------------------------------------------------------- |
| position()                        | 返回节点的 index 位置                                       |
| last()                            | 返回节点的个数                                              |
| contains(string1,string2)         | string1 是否包含 string2                                    |
| text()                            | 返回文本节点                                                |
| comment()                         | 返回注释节点                                                |
| normalize-space(string)           | 去除首位空格，中间多个空格用一个空格代替                    |
| substring(string,start,len)       | 返回从 start 位置开始的指定长度的子字符串,第一个字符下标为1 |
| substring-before(string1,string2) | 返回string1中位于第一个string2之前的部分                    |
| substring-after(string1,string2)  | 返回string1中位于第一个string2之后的部分                    |

同样用上面的Html文档举个例子

| 路径表达式                            | 描述                                       |
| :------------------------------------ | :----------------------------------------- |
| //div[position()>1]                   | 选择第二个 div 节点                        |
| //div[last()]                         | 选择最后一个 div 节点                      |
| contains(//h4[2],'手机')              | 第二个 h4 标签是否包含手机字符串           |
| //li/text()                           | li 节点中的文本内容                        |
| //div/comment()                       | div 节点下的 html 注释                     |
| normalize-space(//li[@class='blank']) | li 节点下 class属性为 blank 的文本去掉空格 |
| substring(//h4[1],1,2)                | 第一个 h4 节点的前2个字                    |
| substring-before(//h4[1],'品牌商')    | 第一个 h4 节点的品牌商字符串之前的字符串   |
| substring-after(//h4[1],'品牌商')     | 第一个 h4 节点的品牌商字符串之后的字符串   |

#### 谓语
XPath 中的谓语就是删选表达式，相当于 SQL 中的 Where 条件，谓语被嵌在 [ ] 中

| 路径表达式                   | 描述                                    |
| :--------------------------- | :-------------------------------------- |
| //div[1]                     | 选择第一个 div 节点                     |
| //div[2]/ul/li[last()]       | 选择第二个 div 节点下的最后一个 li 节点 |
| //div[2]/ul/li[position()>3] | 选择第二个 div 节点下的前两个 li 节点   |
| //ul[@class]                 | 选择所有带 class 属性的 ul 节点         |
| //ul[@class='computer']      | 选择 class 属性为 computer 的 ul 节点   |
| //h4[span = 4]               | 选择 h4 节点下 span 值等于4的节点       |


### lxml 模块

#### 安装 
```python
pip install lxml==4.4.1
```

#### 解析 HTML 文档

lxml.etree 一个强大的 Xml 处理模块，etree 中的 ElementTree 类是一个主要的类，用于对XPath的解析、增加、删除和修改节点。

etree.parse() 函数可以解析一个网页文件还可以解析字符串， 在网页中下载的数据一般都是字符串形式的，使用 parse(StringIO(str)) 将整个页面内容解析加载构建一个 ElementTree 对象，ElementTree 可以使用 XPath 语法精准找到需要的数据。

