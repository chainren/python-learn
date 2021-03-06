#### 1. 垃圾回收算法
##### 1. 引用计数器

> 什么时候对象的引用次数才会增加呢。下面四种情况都会导致对象引用次数加一。

1. 对象被创建（num=2）
2. 对象被引用（count=num）
3. 对象作为参数传递到函数内部
4. 对象作为一个元素添加到容器中


> 同理，对象引用次数减一的情况也有四种。

1. 对象的别名被显式销毁（del num）
2. 对象的别名被赋予新的对象（num=30）
3. 对象离开它的作用域（函数局部变量）
4. 从容器中删除对象，或者容器被销毁

> 引用计数算法的缺点： 当出现循环引用时，无法正确回收垃圾。
> 为了解决交叉引用的问题，Python 引入了标记清除算法和分代回收算法。

----


##### 2. 标记清除

显然，可以包含其他对象引用的容器对象都有可能产生交叉引用问题，而标记清除算法就是为了解决交叉引用的问题的。

标记清除算法是一种基于对象可达性分析的回收算法，该算法分为两个步骤，分别是标记和清除。标记阶段，将所有活动对象进行标记，清除阶段将所有未进行标记的对象进行回收即可。那么现在的问题变为了 GC 是如何判定哪些是活动对象的？

事实上 GC 会从根结点出发，与根结点直接相连或者间接相连的对象我们将其标记为活动对象（该对象可达），之后进行回收阶段，将未标记的对象（不可达对象）进行清除。前面所说的根结点可以是全局变量，也可以是调用栈。

标记清除算法主要用来处理一些容器对象，虽说该方法完全可以做到不误杀不遗漏，但 GC 时必须扫描整个堆内存，即使只有少量的非可达对象需要回收也需要扫描全部对象。这是一种巨大的性能浪费。

##### 3. 分代收集
 由于标记清除算法需要扫描整个堆的所有对象导致其性能有所损耗，而且当可以回收的对象越少时性能损耗越高。因此 Python 引入了分代回收算法，将系统中存活时间不同的对象划分到不同的内存区域，共三代，分别是 0 代，1 代 和 2 代。新生成的对象是 0 代，经过一次垃圾回收之后，还存活的对象将会升级到 1 代，以此类推，2 代中的对象是存活最久的对象。

那么什么时候触发进行垃圾回收算法呢。事实上随着程序的运行会不断的创建新的对象，同时也会因为引用计数为零而销毁大部分对象，Python 会保持对这些对象的跟踪，由于交叉引用的存在，以及程序中使用了长时间存活的对象，这就造成了新生成的对象的数量会大于被回收的对象数量，一旦二者之间的差值达到某个阈值就会启动垃圾回收机制，使用标记清除算法将死亡对象进行清除，同时将存活对象移动到 1 代。以此类推，当二者的差值再次达到阈值时又触发垃圾回收机制，将存活对象移动到 2 代。

这样通过对不同代的阈值做不同的设置，就可以做到在不同代使用不同的时间间隔进行垃圾回收，以追求性能最大。

事实上，所有的程序都有一个相似的现象，那就是大部分的对象生存周期都是相当短的，只有少量对象生命周期比较长，甚至会常驻内存，从程序开始运行持续到程序结束。而通过分代回收算法，做到了针对不同的区域采取不同的回收频率，节约了大量的计算从而提高 Python 的性能。

除了上面所说的差值达到一定阈值会触发垃圾回收之外，我们还可以显示的调用 gc.collect() 来触发垃圾回收，最后当程序退出时也会进行垃圾回收。