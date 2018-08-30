# 定义学生类
# 定义一个空的类
# class Student():
#     pass
# 定义一个对象
# mingyue = Student()
# class PythonStudent():
#     # 给不确定的赋值
#     name = None
#     age = 18
#     course = 'python'
#     # 注意缩进层级
#     # 系统默认一个参数
#     def doHomework(self):
#         print('做作业')
#         return None
# yy = PythonStudent()        # 实例化一个具体对象
# print(yy.age)
# print(yy.course)
# yy.doHomework()             # 注意程艳函数的调用没有出传入参数

# class Studengt():
#     name = 'jjj'
#     age = 18
# print(Studengt.__dict__)
# yy = Studengt()
# print(yy.__dict__)

# 类实例的属性和其他对象的实例的属相在不对对象的实例属性赋值的前提下，指向同一个变量（指向同一内存）
# class A():
#     name = 'ooo'
#     age = 19
#     # 参数self类似于JAVA中的this
#     def say(self):
#         self.name = 'aaa'
#         self.age = 20
# 此时 A 称为类实例
# print(A.name)
# print(A.age)
# print('*' * 20)
# # id 可以鉴别一个变量是否与另一个变量是同一个变量
# print(id(A.age))
# print(id(A.name))
# a = A()
# print(a.name)
# print(a.age)
# print(id(a.age))
# print(id(a.name))

# print(A.name)
# print(A.age)
# print('*' * 20)
# print(id(A.age))
# print(id(A.name))
# print('*' * 20)
# a = A()
# print(A.__dict__)
# print(a.__dict__)
# a.name = 'iii'
# a.age = 16
# print(a.__dict__)
# print(a.name)
# print(a.age)
# print(id(a.age))
# print(id(a.name))


# class Student():
#     name = 'ooo'
#     age = 19
#     # self代表第一参数，不是关键字
#     def say(self):
#         self.name = 'aaa'
#         self.age = 20
#         print('may name is {0}'.format(self.name))
#         print('my age is {0}'.format(self.age))
#     def sayAgain(s):
#         print('may name is {0}'.format(s.name))
#         print('my age is {0}'.format(s.age))
# yy = Student()
# yy.say()
# yy.sayAgain()

# 绑定函数案例
# class Teacher():
#     name = '111'
#     age = 44
#     def say(self):
#         self.name = 'www'
#         self.age = 43
#         print('may name is {0}'.format(self.name))
#         # 调用类的成员变量
#         print('my age is {0}'.format(__class__.age))
#     def sayAgain():
#         print(__class__.name)
#         print(__class__.age)
#         print('hello')
# t = Teacher()
# t.say()
# # 调用绑定类函数使用类名
# Teacher.sayAgain()

# self案例
# class A():
#     name = 'lll'
#     age = 11
#     # 类似于构造函数
#     def __init__(self):
#         self.age = 200
#         self.name = 'aaaa'
#     def say(self):
#         print(self.name)
#         print(self.age)
# class B():
#     name = 'rrr'
#     age = 5
# a = A()
# a.say()
# A.say(a)
# A.say(A)
# # 只要结构相似，具备相同属性，就能使用
# A.say(B)

# 私有变量案例
# class Person():
#     name = 'eee'
#     __age = 33
# p = Person()
# print(p.name)
# # print(p.__age)
# # name mangling技术
# print(Person.__dict__)
# print(p._Person__age)
