谈一谈 python 中 del 的用法
del涉及到python中的内存管理机制，从c/c++转过来的同学可能会踩一些语法坑，下面上一些代码及运行结果，谈谈今天要讲的问题，后面再解释具体原理机制。
```python
a = 1
b = a
c = a
print(a)
print(b)
print(c)
```
结果
1
1
1
这个结果是很显然的，不多解释。
下面，del a和b, 打印c看一看:
```python
a=1       # 对象 1 被 变量a引用，对象1的引用计数器为1
b=a       # 对象1 被变量b引用，对象1的引用计数器加1 = 2
c=a       #1对象1 被变量c引用，对象1的引用计数器加1 = 3
del a     #删除变量a，解除a对1的引用
del b     #删除变量b，解除b对1的引用
print(c)  #最终变量c仍然引用1
结果：
1
```
很奇怪，明明a已经被del了，c=a还是可以得到1的结果。
这就是python的GC也就是垃圾回收机制：
由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。
将a和b del之后，1的引用计数仍然为1，所以不会被清除
由于python都是引用，而python有GC机制，所以，del语句作用在变量上，而不是数据对象上。
```python
if __name__=='__main__':
    a=1       # 对象 1 被 变量a引用，对象1的引用计数器为1
    b=a       # 对象1 被变量b引用，对象1的引用计数器加1
    c=a       #1对象1 被变量c引用，对象1的引用计数器加1
    del a     #删除变量a，解除a对1的引用
    del b     #删除变量b，解除b对1的引用
    print(c)  #最终变量c仍然引用1
```
del删除的是变量，而不是数据。
另外。关于list。
```python
if __name__=='__main__':
    li=[1,2,3,4,5]  #列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]
    first=li[0]     #拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
    del li[0]
    print(li)      #输出[2, 3, 4, 5]
    print(first)   #输出 1
```