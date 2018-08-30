# 成员描述符案例
# 学生类具有Student.name属性，但 nmae 格式不统一
# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.setName(name)
#     def intro(self):
#         print('hi, my name is {0}'.format(self.name))
#     # 将书写格式修改为大写
#     def setName(self, name):
#         self.name = name.upper()
# s1 = Student('LIU xue LI', 12)
# s2 = Student('liu xue li', 24)
# s1.intro()
# s2.intro()

# ptoperty案例
# 定义Person类，具有 name, age属性
# class Person():
#     # 函数名称可任意
#     def fget(self):
#         return self._name * 2
#     def fset(self,name):
#         self._name = name.upper()
#     def fdel(self):
#         self._name = 'noname'
#     name = property(fget, fset, fdel, "ccc")
# p1 = Person()
# p1.name = 'qq'
# print(p1.name)

# class Person():                           #　报错
#     '''
#     去哦哦我
#     '''
#     def fget(self):
#         return self._age
#     def fset(self, age):
#         self.age = int(age)
#     def fdel(self):
#         self._name = 'noname'
#     age = property(fget, fset, fdel, "ccc")
# i = Person()
# i.age = 14.56
# print(i.age)


# 属性的三种用法
# class A():
#     def __init__(self):
#         self.name = 'aa'
#         self.age = 12
# # 1.赋值
# # 2.读取
# # 3.删除
# a = A()
# a.name = 'bbb'
# print(a.name)
# del a.name
# print(a.name)

# 类属性 property
# 应用场景：初三中普通操作外，增加一些对变量的操作，用 property
# class A():
#     def __init__(self):
#         self.name = 'aaaa'
#         self.age = 12
#     def fget(self):
#         print('读取了')
#         return self.name
#     def fset(self, name):
#         print('被写入')
#         self.name = name
#     def fdel(self):
#         print('删除了')
#     # property 四个参数顺序固定
#     # 1、代表读取时需要调用的参数
#     # 2、代表写入时需要调用的参数
#     # 3、删除
#     name2 = property(fget, fset, fdel, '123')
# a = A()
# print(a.name)
# print(a.name2)


# 类内置属性演示
# print(Person.__dict__)
# print(Person.__doc__)

# __call__示例
# class A():
#     def __init__(self):
#         print('daiouong')
#     def __call__(self):
#         print('aaa')
# a = A()
# a()

# __str__示例
# class A():
#     def __init__(self):
#         print('daiouong')
#     def __call__(self):
#         print('aaa')
#     def __str__(self):
#         return 'iiiiiii'
# a = A()
# print(a)

# __getattr__
# class A():              #　为什么会打印出None
#     name = 'no'
#     age = 18
#     def __getattr__(self, name):
#         print('mei')
# a = A()
# print(a.name)
# print(a.addr)

# __steattr__示例
# class Person():
#     def __init__(self):
#         pass
#     def __setattr__(self, name, value):
#         print('设置属性：{0}'.format(name))
#         # 下面语句会导致死循环
#         # self.name = value
#         # 为避免死循环，福IDing同意调用父类魔法函数
#         super().__setattr__(name, value)
# p = Person()
# print(p.__dict__)
# p.age = 18

# __gt__演示
# class Stuent():
#     def __init__(self, name):
#         self._name = name
#     def __gt__(self, obj):
#         print('哈哈，{0}会比{1}大吗'.format(self, obj))
#         return self._name > obj._name
# stu1 = Stuent('one')
# stu2 = Stuent('two')
# print(stu1 > stu2)
# 将比较结果抓变为 one 会比 two 大吗


# 三种方法案例
# class Person():
#     # 实例方法
#     def eat(self):
#         print(self)
#         print('eat')
#     # 类方法
#     # 方法的第一个参数一般命名为cls，区别于self
#     @classmethod
#     def play(cls):
#         print(cls)
#         print('play')
#     # 静态方法
#     # 不粗要用一个参数表示自身或类
#     @staticmethod
#     def say():
#         print('say')
# yy = Person()
# # 实例方法
# yy.eat()
# # 类方法
# Person.play()
# yy.play()   # 实例调用类方法
# # 静态方法
# Person.say()
# yy.say()


# 抽象方法
# class Animel():
#     def sayHello(self):
#         pass
# class Dog():
#     def sayHello(self):
#         print('wen')
# class Person():
#     def sayHello(self):
#         print('kiss')
# d = Dog()
# d.sayHello()
# p = Person()
# p.sayHello()

# 抽象类的实现
# import abc
# # 声明一个类并指定当前类的元类
# class Human(metaclass=abc.ABCMeta):
#     # 定义一个抽象的方法
#     @abc.abstractmethod
#     def somking(self):
#         pass
#     # 定义类抽象方法
#     @abc.abstractclassmethod
#     def drink(c):
#         pass
#     # 定义静态抽象方法
#     @abc.abstractstaticmethod
#     def play():
#         pass

# 自己组装一个类
# class A():
#     pass
# def say(self):
#     print('qqqq')
# class B():
#     def say(self):
#         print('iiii')
# say(9)
# A.say = say
# a = A()
# a.say()
#
# b = B()
# b.say()

# 组装类
# 通过 MethodType 将方法与类进行组装
# from types import MethodType
# class A():
#     pass
# def say(self):
#     print('uuu')
# a = A()
# a.say = MethodType(say, A)
# a.say()
# help(MethodType)

# 利用type创建类
# 限定一类应具有的成员函数
# def say(self):
#     print('saying')
# def talk(self):
#     print('talking')
# # 用 type 来创建一个类
# A = type('aname', (object, ), {'class_say':say, 'class_talk':talk})
# # 然后可象一般类一样访问
# a = A()
# print(dir(a))
# a.class_say()
# a.class_talk()

# 元类演示
# 元类写法是固定的，必须继承自type
# 一般以MetaClass结尾
class TulingMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己的业务处理
        print('我是元类')
        attrs['id'] = '00000000'
        attrs['addr'] = '火星'
        return type.__new__(cls, name, bases, attrs)
# 元类定义完就可以使用，使用时注意写法
class Techer(object, metaclass=TulingMetaClass):
    pass
t = Techer()
print(t.__dict__)
print(t.id)