# import 01    #  报错
# 借助importlib包可以实现以数字开头的包
# 相当于导入了一个叫01的模块导入模块，并将值给变量
# 语法：变量 = importlib.import_moudle(模块名)
import p01
# 导入后，被导入的代码全部执行一遍
stu = p01.Student('llll', 19)
stu.say()
p01.sayHello()