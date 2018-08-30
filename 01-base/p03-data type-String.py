#!/usr/bin/python
# -*- coding:utf-8 -*-

# 字符串：字符串或串(String)是由数字、字母、下划线组成的一串字符
# 从左到右索引默认0开始的，最大范围是字符串长度少1
# 从右到左索引默认-1开始的，最大范围是字符串开头
# 与C字符串不同的是，Python字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
s = 'ilovepython'
print (s[1:5])  # 使用以冒号分隔的字符串，返回新的对象，包含了下边界 最大范围不包括上边界

# 使用引号来创建字符串  创建字符串很简单，只要为变量分配一个值即可 单引号/双引号/三单引号/三双引号(嵌套使用)
var1 = 'Hello World!'
var2 = 'Python w3cschool'
name = 'john'
print(name)
a = b = c = 'tom'
print(a, b, c)
d, e, f = 'jerry', 'andy', "jhon"
print(d, e, f)
var1 = 1
var2 = 10
print(var1, var2)
# del 删除对象引用
del (var1, var2)
# print(var1, var2)
html = '<a style="color:red">dfsfa</a>'
print(html)

# 访问字符串中的值
# Python不支持单字符类型，单字符也在Python也是作为一个字符串使用
# Python访问子字符串，可以使用方括号来截取字符串
var1 = 'Hello World!'
var2 = 'Python w3cschool'
# print 'var1[0]:',var1[0];     # python2 函数
# print 'var2[1:5]:',var2[1:5];
print ('var1[0]:',var1[0]);     # python3 函数
print ('var2[1:5]:',var2[1:5]);

# 字符串更新
# 可以对已存在的字符串进行修改，并赋值给另一个变量
var1 = 'Hello World!';
print ('更新字符串:-',var1[:6] + 'w3cschool!')

# 转义符：以\开头将内容转义
# \(在行尾时)	续行符        \\	反斜杠符号       \'	单引号
# \"	双引号                \a	响铃             \b	退格(Backspace)
# \e	转义                  00	空               \n	换行
# \v	纵向制表符            \t	横向制表符       \r	回车
# \f	换页  \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出
# 换行：windows:\n     linux:\r\n
s = 'let\'s go'
print(s)
# 不想发生转义，在字符串前面添加一个r，表示原始字符串
print('C:\some\name')
print(r'C:\some\name')

# 格式化：将字符串按一定格式打印或填充
# 字符串格式化
print ('My name is %s and weight is %d kg!'%('zara',21))    # 基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中
print ('My name is %s !'%'zara')
# 字符串格式化符号：
#  %c	 格式化字符及其ASCII码            %s	 格式化字符串
#  %d	 格式化整数                       %u	 格式化无符号整型
#  %o	 格式化无符号八进制数             %x	 格式化无符号十六进制数
#  %X	 格式化无符号十六进制数（大写）   %f	 格式化浮点数字，可指定小数点后的精度
#  %e	 用科学计数法格式化浮点数         %E	 作用同%e，用科学计数法格式化浮点数
#  %g	 %f和%e的简写                     %G	 %f 和 %E 的简写
#  %p	 用十六进制数格式化变量的地址
# 格式化操作符辅助指令：
# *	定义宽度或者小数点精度                        -	    用做左对齐
# +	在正数前面显示加号( + )                       <sp>	在正数前面显示空格
# #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	显示的数字前面填充'0'而不是默认的空格         %	    '%%'输出一个单一的'%'
# (var)	映射变量(字典参数)                        m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
# 三引号（triple quotes）:将复杂的字符串进行复制
# 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
# 三引号的语法是一对连续的单引号或者双引号
hi = '''hi
there'''
hi #reper()
'hi\nthere'
print (hi) #str()
# 自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的
# 典型用例:
# errHTML = '''
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# '''
# cursor.execute('''
# CREATE TABLE users (
# login VARCHAR(8),
# uid INTEGER,
# prid INTEGER)
# ''')
# format():{}和: 代替%号，后面用format带参数完成
s = 'I love {}'.format("mongey")
print(s)
s = "Yes , i am {1} years old,I love {0} and i am {1} years old".format("学习",18)
print(s)

# None;没有   用来占位或解除变量绑定

# 表达式：由一个或多个数字、变量或运算符著称的代码

# 字符串运算符
# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	H in a 输出结果 1
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	M not in a 输出结果 1
# r/R	原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	print r'\n' prints \n 和 print R'\n' prints \n
# %	格式字符串
a = 'Hello'
b = 'python'
print ('a + b 输出结果：',a + b);
print('a * 2 输出结果：',a * 2);
print ('a[1] 输出结果：',a[1]);
print ('a[1:4] 输出结果：',a[1:4]);
if( 'H' in a ):
    print ('H 在变量 a 中')
else:
    print ('H 不在变量 a 中')
if('M' not in a):
    print ('M 不在变量 a 中')
else:
    print ('M 在变量 a 中')
print (r'\n');
print (R'\n');

# unicode字符串
# Python 中定义一个 Unicode 字符串和定义一个普通字符串一样
u'Hello World !'
# 引号前小写的"u"表示这里创建的是一个 Unicode 字符串 如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码
u'Hello\u0020World !'
u'Hello World !'

# python的字符串内建函数
#