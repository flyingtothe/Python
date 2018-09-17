# class Person():
#     name = 'noname'
#     age = 0
#     __score = 0
#     _petname = 'ss'
#     def sleep(self):
#         print('sleeping')
# # 父类写在括号中
# class Teacher(Person):
#     teacher_id = '9527'
#     def make_test(self):
#         print('attention')
# t = Teacher()
# print(t.name)
# # 受保护变量不能外部访问   ？？？
# print(t._petname)
# # 公开访问私有变量报错
# # print(t.__score)
# t.sleep()
# print(t.teacher_id)
# t.make_test()

# 子类和父类定义同一个变量
# class Person():
#     name = 'noname'
#     age = 0
#     __score = 0
#     _petname = 'ss'
#     def sleep(self):
#         print('sleeping')
# class Teacher(Person):
#     teacher_id = '9527'
#     name = 'iii'
#     def make_test(self):
#         print('attention')
# t = Teacher()
# print(t.name)

# 子类扩充父类功能
# class Person():
#     name = 'noname'
#     age = 0
#     __score = 0
#     _petname = 'ss'
#     def sleep(self):
#         print('sleeping')
#     def work(self):
#         print('money')
# class Teacher(Person):
#     teacher_id = '9527'
#     name = 'iii'
#     def make_test(self):
#         print('attention')
#     def work(self):
#         # 扩充父类的功能只需调用父类相应的函数
#         # Person.work(self)
#         # 使用super扩充父类
#         # super().work()
#         self.make_test()
# t = Teacher()
# print(t.work())

# 构造函数
# class Dog():
#     # __init__是构造函数
#     # 实例化时第一个被自动调用
#     def __init__(self):
#         print('is a dog')
# # 实例化的时候，括号内的参数需跟函数参数匹配
# kaka = Dog()

# 继承中的构造 - 1
# class Animel():
#     pass
# class BuruAni(Animel):
#     pass
# class Dog(BuruAni):
#     def __init__(self):
#         print('is a dog')
# # 实例化的时候,自动调用了Dog的构造
# kaka = Dog()

# 继承中的构造 - 2
# class Animel():
#     def __init__(self):
#         print('Animel')
# class BuruAni(Animel):
#     def __init__(self):
#         print('Bu ru dong wu')
# class Dog(BuruAni):
#     def __init__(self):
#         print('is a dog')
# # 实例化的时候,自动调用了Dog的构造
# kaka = Dog()
#
# class Cat(BuruAni):
#     # 没有构造函数，查找父类
#     pass
# c = Cat()

# 继承中的构造 - 3
# class Animel():
#     def __init__(self):
#         print('Animel')
# class BuruAni(Animel):
#     def __init__(self,name):
#         print('Bu ru dong wu {0}'.format(name))
# class Dog(BuruAni):
#     def __init__(self):
#         print('is a dog')
# # 实例化的时候,自动调用了Dog的构造
# d = Dog()
# class Cat(BuruAni):
#     pass
# # 因为构造参数需要两个参数，实例化时给了一个，报错
# c = Cat()

# 继承中的构造 - 4
# class Animel():
#     def __init__(self):
#         print('Animel')
# class BuruAni(Animel):
#     pass
# class Dog(BuruAni):
#     pass
# # 实例化的时候,自动调用了Dog的构造
# d = Dog()
# class Cat(BuruAni):
#     pass
# # 因为构造参数需要两个参数，实例化时给了一个，报错
# c = Cat()

# super 示例
# print(type(super))
# help(super)
# class A():
#     pass
# class B(A):
#     pass
# print(A.__mro__)
# print(B.__mro__)

# 继承
# class Fish():
#     def __init__(self, name):
#         self.name = name
#     def swim(self):
#         print('i am swiming')
# class Bird():
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print('i am flying')
# class Person():
#     def __init__(self, name):
#         self.name = name
#     def work(self):
#         print('i am working')
# # 多继承
# class SuperMan(Person, Bird, Fish):
#     def __init__(self, name):
#         self.name = name
# s = SuperMan('yeuyeu')
# s.fly()
# s.swim()
# # 单继承
# class Student(Person):
#     def __init__(self, name):
#         self.name = name
# stu = Student('ii')
# stu.work()

# 菱形问题
# class A():
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass

# 构造函数的调用顺序 - 1
# class A():
#     def __init__(self):
#         print('A')
# class B(A):
#     def __init__(self):
#         print('B')
# class C(B):
#     pass
# # 自身没有，则向上按照MRO顺序查找，直到找到为止
# c = C()

# 构造函数的调用顺序 - 2
# class A():
#     def __init__(self):
#         print('A')
# class B(A):
#     def __init__(self, name):
#         print('B')
#         print(name)
# class C(B):
#     # C 中扩展 B 的构造函数，在调用后添加一些功能
#     '''
#     # 第一种
#     def __init__(self, name):
#         # 首先调用父类构造
#         B.__init__(self, name)
#         # 再添加自己功能
#         print('这是C中的附加功能')
#     '''
#     # 第二种，使用super调用
#     def __init(self, name):
#         super(C, self).__init__(name)
#         print('这是C附加的功能')
# # 参数结构不对应，报错
# c = C("我是C")

# Mixin案例
# class Person():
#     name = 'qqq'
#     age = 11
#     def eat(self):
#         print('eat')
#     def drink(self):
#         print('drink')
#     def sleep(self):
#         print('sleep')
# class Teacher(Person):
#     def ework(self):
#         print('work')
# class Student(Person):
#     def study(self):
#         print('study')
# class Tuotr(Teacher, Student):
#     pass
# t = Tuotr()
# print(Tuotr.__mro__)
# print(t.__dict__)
# print(Tuotr.__dict__)
# print('*' * 20)
# class TeacherMixin():
#     def work(self):
#         print('work')
# class StudentMixin():
#     def study(self):
#         print('study')
# class TutorM():
#     pass
# tt = TutorM()
# print(TutorM.__mro__)
# print(tt.__dict__)
# print(TutorM.__dict__)


# issubclass
# class A():
#     pass
# class B(A):
#     pass
# class C():
#     pass
# print(issubclass(B, A))

# isinstance
# class A():
#     pass
# a = A()
# print(isinstance(a, A))
# print(isinstance(A, A))

# hasattr
# class A():
#     name = 'noname'
# a = A()
# print(hasattr(a,'name'))

# dir
class A():
    pass
print(dir(A))
a = A()
print(dir(a))
