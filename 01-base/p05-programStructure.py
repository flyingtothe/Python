# coding=utf-8

# 指定任何非0和非空（null）值为true，0 或者 null为false
# input() 返回类型为字符串      python3 只有 input 没有 raw_input

# 分支结构
# if 基本用法
# if 语句的判断条件可以用>（大于）、=（大于等于）、<=（小于等于）来表示其关系
# flag = False
# name = 'luren'
# if name == 'python':            # 判断变量否为'python'
#     flag = True                 # 条件成立时设置标志为真
#     print ('welcome boss')      # 并输出欢迎信息
# else:
#     print (name)                # 条件不成立时输出变量名称

# elif 用法
# 由于 python 并不支持 switch 语句，多个条件判断，用 elif 实现，如果判断需要多个条件需同时判断时，可以使用 or （或），
# 表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
# num = 5
# if num ==3 :                    # 判断num的值
#     print ('boss')
# elif num ==3:
#     print ('user')
# elif num == 1:
#     print ('worker')
# elif num < 0 :                  # 值小于零时输出
#     print ('error')
# else:
#     print ('roadman')           # 条件均不成立时输出

# if 语句多个条件
# if有多个条件时用括号来判断先后顺序，括号中的优先执行，此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，
# 即大于和小于在没有括号的情况下会比与或要优先判断。
# num = 9
# if (num >= 0 and num <= 10):    # 判断值是否在0~10之间
#     print ('hello')             # 输出结果
#
# num = 10
# if num < 0 or num > 10:         # 判断值是否在小于0或大于10
#     print ('hello')
# else:
#     print ('undefine')          # 输出结果
# num = 8
# # 判断值是否在0~5或者10~15之间
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
#     print ('hello')
# else:
#     print ('undefine')          # 输出结果
# var = 100
# if ( var == 100 ):
#     print('Good bye')


# 循环结构
# 提供了for循环和while循环，没有do..while循环
# while 循环 在给定的判断条件为 true 时执行循环体，否则退出循环体。
# for 循环 重复执行语句
# 嵌套循环 你可以在while循环体中嵌套for循环

# 如果变量名不重要，可用下划线代替（_）
# break     在语句块执行过程中终止循环，并且跳出整个循环
# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:             # 非双数时跳过输出
#         continue
#     print (i)                 # 输出双数2、4、6、8、10
# continue  在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
# i = 1
# while 1:  # 循环条件为1必定成立
#     print (i)                 # 输出1~10
#     i += 1
#     if i > 10:                # 当i大于10时跳出循环
#         break
# pass      pass是空语句  略过  是为了保持程序结构的完整性
# while True:
#     pass                      # 等待键盘中断

# while循环
# 执行语句可以是单个语句或语句块。判断条件可以是任何表达式
# 任何非零、或非空（null）的值均为true，当判断条件假false时，循环结束
# benqian = 10000
# year = 0
# while benqian < 20000:
#     benqian = benqian * (1+0.067)
#     year += 1
#     print ('第 {0} 年拿了 {1} 块钱'.format(year,benqian))
# else:
#     print('终于翻倍了')

# 判断语句永远为 true
# var = 1
# while var == 1:
#     num = input('Enter a number') # 根据输入类型 自动转换
#     print ('You entered :',num)
# print ('Good bye')

# 循环中使用 else 语句
# while … else：while 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 while 不是通过 break 跳出而中断的）的情况下执行
# count = 0
# while count < 5:
#     print (count, 'is less than 5')
#     count = count + 1
# else:
#     print (count, 'is not less than 5')
#
# flag = 1
# while(flag):
#     print ('Gien falg is really true!')
# print ('Good bye')

# for 循环语句
# for 循环可遍历任何序列的项目，如一个列表或者一个字符串
# for letter in 'Python':
#     print ('当前字母:',letter);
# fruits = ['banana','apple','mango']
# for fruit in fruits:
#     print ('当前字母:',fruit)
# print ('Good bye')

# 通过序列索引迭代
# 函数 len() 返回列表的长度，即元素的个数   函数range() 返回一个序列的数。
# fruits = ['banana','apple','mango']
# for index in range(len(fruits)):
#     print ('当前水果：',fruits[index])
# print ('Good bye')

# 循环使用 else 语句
# for … else: for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
# for num in range(10,20):        # 迭代 10 到 20 之间的数字
#     for i in range(2,num):      # 根据因子迭代
#         if num%i == 0:          # 确定第一个因子
#             j=num/i             # 计算第二个因子
#             print ('%d 等于 %d * %d' % (num,i,j))
#             break               # 跳出当前循环
#     else:                       # 循环的 else 部分
#         print (num, '是一个质数')

# 嵌套循环
# 允许在一个循环体里面嵌入另一个循环  如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环
# 输出 2-100 间素数
# i = 2
# while(i<100):
#     j = 2
#     while(j <=(i/j)):
#         if not(i%j):
#             break
#         j =j + 1
#     if(j > i/j):
#         print (i, '是素数')
#     i = i +1
# print ('Good bye')