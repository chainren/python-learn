## Beautiful Soup 简介

Beautiful Soup 是一个可以从 HTML 或 XML 文件中提取数据的 Python 库，它提供了一些简单的操作方式来帮助你处理文档导航，查找，修改文档等繁琐的工作。因为使用简单，所以 Beautiful Soup 会帮你节省不少的工作时间。

上一篇文章我们介绍了如何使用 Beautiful Soup 来遍历文档中的节点，这片文章我们继续血学习如何使用 Beautiful Soup 指定文档中搜索到你想要的内容。

## Beautiful Soup 搜索文档

同样为了故事的顺利发展，我们继续使用之前的 HTML 文本，下文的所有例子都是基于这段文本的。

```
html_doc = """<html><head><title>index</title></head><body><p class="title"><b>首页</b></p><p class="main">我常用的网站<a href="https://www.google.com" class="website" id="google">Google</a><a href="https://www.baidu.com" class="website" id="baidu">Baidu</a><a href="https://cn.bing.com" class="website" id="bing">Bing</a></p><div><!--这是注释内容--></div><p class="content1">...</p><p class="content2">...</p></body>"""soup = BeautifulSoup(html_doc, "lxml")
```

### 过滤器

正式讲解搜索文档之前，我们有必要了解下 Beautiful Soup 的过滤器，这些过滤器在整个搜索的 API 中都有所体现，他们可以被用在 TAG 的 name 中，属性中，字符串中或他们的混合中。听起来有点绕是么，看几个例子就懂了。

1、根据 TAG 的 name 来查找标签，下面的例子会查找文档中的所有 b 标签。同时要注意统一传入 Unicode 编码以避免 Beautiful Soup 解析编码出错。

```
# demo 1tags = soup.find_all('b')print(tags)
#输出结果[<b>首页</b>]
```

2、如果传入正则表达式作为参数，那么 Beautiful Soup 会通过正则表达式的 match() 来匹配内容。

```
# demo 2import refor tag in soup.find_all(re.compile("^b")):    print(tag.name)
#输出结果bodyb
```

3、如果传入列表参数，那么 Beautiful Soup 会将与列表中任一一个元素匹配的内容返回。

```
# demo 3for tag in soup.find_all(['a', 'b']):    print(tag)
#输出结果<b>首页</b><a class="website" href="https://www.google.com" id="google">Google</a><a class="website" href="https://www.baidu.com" id="baidu">Baidu</a><a class="website" href="https://cn.bing.com" id="bing">Bing</a>
```

4、True 可以匹配任何值，下面的例子是查找所有的 TAG 但不会返回字符串。



```
# demo 4for tag in soup.find_all(True):    print(tag.name, end=', ') #输出结果html, head, title, body, p, b, p, a, a, a, div, p, p,
```

5、方法。我们可以定义一个方法，该方法只接受一个参数，若该方法返回 True 则表示当前元素匹配并且被找到，返回 False 意味着没找到。下面的例子展示了查找所有同时包含 class 属性和 id 属性的节点。

```
# demo 5def has_id_class(tag):    return tag.has_attr('id') and tag.has_attr('class')
tags = soup.find_all(has_id_class)for tag in tags:	print(tag)	#输出结果<a class="website" href="https://www.google.com" id="google">Google</a><a class="website" href="https://www.baidu.com" id="baidu">Baidu</a><a class="website" href="https://cn.bing.com" id="bing">Bing</a>
```

大部分情况字符串过滤器就可以满足我们的需求，外加这个神奇的方法过滤器，我们就可以实现各种自定义需求了。

### find_all() 函数

该函数搜索当前节点下的所有子节点，其签名如下`find_all( name , attrs , recursive , text , **kwargs )`。我们可以传入指定 TAG 的 name 来查找节点，上面已经举过例子了，这里不在赘述。我们来看几个其他的用法。

1、如果我们传入 find_all() 函数不是搜索内置的参数名，那么搜索是就会将该参数对应到属性上去。下文的例子表示查找 id 为 google 的节点。

搜索指定名字的属性时可以使用的参数值包括：字符串，正则表达式，列表，True。也就是我们上文介绍过的过滤器。

```
# demo 6
tags = soup.find_all(id='google')
    print(tags[0]['href'])
for tag in soup.find_all(id=True): # 查找所有包含 id 属性的 TAG	    print(tag['href'])
#输出结果
https://www.google.com
https://www.google.com
https://www.baidu.comhttps://cn.bing.com
```

2、按照 CSS 类名搜索，但是镖师 CSS 的关键字 class 在 Python 中是内置关键字，从 Beautiful Soup 4.1.1 版本开始，可以通过 `class_` 参数搜索有指定 CSS 类名的 TAG：

class_ 参数同样接受不同类型的过滤器：字符串，正则表达式，方法，True。

```
# demo 7
tags = soup.find_all("a", class_="website")
for tag in tags:	
    print(tag['href'])

def has_seven_characters(css_class):    
    return css_class is not None and len(css_class) == 7

for tag in soup.find_all(class_=has_seven_characters):	
    print(tag['id'])

#输出结果
https://www.google.com
https://www.baidu.com
https://cn.bing.comgooglebaidubing
```

同时，因为 CSS 可以有多个值，所以我们可以分别搜索 CSS 中的每个值。

```
# demo 8
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
tags = css_soup.find_all("p", class_="strikeout")
print(tags)

#输出结果
[<p class="body strikeout"></p>]
```

3、不仅可以按照标签和 CSS 来搜索整个文档，还可以使用 text 来按照内容来搜索。同时 text 还可以配合其他属性一起来完成搜索任务。

```
# demo 9
tags = soup.find_all(text="Google")
print("google : ", tags)
tags = soup.find_all(text=["Baidu", "Bing"])
print("baidu & bing : ", tags)
tags = soup.find_all('a', text="Google")
print("a[text=google] : ", tags)

#输出结果
google :  ['Google']
baidu & bing :  ['Baidu', 'Bing']
a[text=google] :  [<a class="website" href="https://www.google.com" id="google">Google</a>]
```

4、限制返回数量

有时候文档树过于庞大，我们不想查查找整棵树，只想查找指定数量的节点，或者只想查找子节点，而不想查找孙子节点，指定 limit 或者 recursive 参数即可。

```
# demo 10
tag = soup.find_all("a", limit=1)
print(tag)
tags = soup.find_all("p", recursive=False)
print(tags)
#输出结果
[<a class="website" href="https://www.google.com" id="google">Google</a>][]
```

因为该对象的儿子节点没有 p 标签，所以返回的是空列表。

### find() 函数

该函数只会返回一个结果，与 find_all(some_args, limit=1) 是等价的，唯一的区别就是该函数直接返回结果，而 find_all() 函数返回包含一个结果的列表。另外 find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None。除此之外使用上没有其他差别。

### 其他函数

除了 find_all() 和 find() 外，Beautiful Soup 中还有 10 个用于搜索的 API，其中中五个用的是与 find_all() 相同的搜索参数，另外 5 个与 find() 方法的搜索参数类似，区别仅是它们搜索文档的范围不同。

find_parents() 和 find_parent() 用来搜索当前节点的父节点。

find_next_siblings() 和 find_next_sibling() 对在当前节点后面解析的所有兄弟节点进行迭代。

find_previous_siblings() 和 find_previous_sibling() 对在当前节点前面解析的所有兄弟节点进行迭代。

find_all_next() 和 find_next() 对当前节点之后的 TAG 和字符串进行迭代。

find_all_previous() 和 find_previous() 对当前节点之前的 TAG 和字符串进行迭代。

以上五组函数的区别仅仅是前者返回一个所有符合搜索条件的节点列表，而后者只返回第一个符合搜索条件的节点。

因为这 10 个 API 的使用和 find_all() 与 find() 大同小异，所有i这里不在举例，读者可以自己探索。

### CSS 选择器

在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数即可使用 CSS 选择器的语法找到 TAG。

1、通过某个标签逐层查找。

```
# demo 11tags = soup.select("body a")for tag in tags:	print(tag['href'])
#输出结果https://www.google.comhttps://www.baidu.comhttps://cn.bing.com
```

2、查找某个标签下的直接子标签

```
# demo 12tags = soup.select("p > a")print(tags)
tags = soup.select("p > #google")print(tags)
#输出结果[<a class="website" href="https://www.google.com" id="google">Google</a>, <a class="website" href="https://www.baidu.com" id="baidu">Baidu</a>, <a class="website" href="https://cn.bing.com" id="bing">Bing</a>][<a class="website" href="https://www.google.com" id="google">Google</a>]
```

3、通过 CSS 类名直接查找

```
# demo 13tags = soup.select(".website")for tag in tags:	print(tag.string)
#输出结果GoogleBaiduBing
```

4、通过标签的 id 属性查找

```
# demo 14tags = soup.select("#google")print(tags)
#输出结果[<a class="website" href="https://www.google.com" id="google">Google</a>]
```

5、通过属性的值来查找

```
# demo 15tags = soup.select('a[href="https://cn.bing.com"]')print(tags)
#输出结果[<a class="website" href="https://cn.bing.com" id="bing">Bing</a>]
```

## Beautiful Soup 总结

本章节介绍了 Beautiful Soup 关于文档搜索的相关操作，熟练掌握这些 API 的操作可以让我们更快更好找到我们想要定位的节点，不要看到这么多函数吓怕了，其实我们只需要熟练掌握 find_all() 和 find() 两个函数即可，其余 API 的使用都大同小异，稍加练习即可快速上手。