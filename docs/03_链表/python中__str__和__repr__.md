如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
```
现在，在交互式命令行下用 print 试试：
```bash
>>> p = Person('Bob', 'male')
>>> print p
(Person: Bob, male)
但是，如果直接敲变量 p：
>>> p
<main.Person object at 0x10c941890>
```
似乎__str__()不会被调用。
因为 Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。
有一个偷懒的定义__repr__的方法：
```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__
```
任务
请给Student 类定义__str__和__repr__方法，使得能打印出<Student: name, gender, score>：
只要为Students 类加上__str__()和__repr__()方法即可。
参考代码:
```python
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__
```
```bash
s = Student('Bob', 'male', 88)
s
(Student: Bob, male, 88)
```
作者：Jlan
链接：https://www.jianshu.com/p/62a7e9766bc8
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。