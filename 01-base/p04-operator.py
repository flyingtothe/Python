# coding=utf-8

# 算数运算符
# + 加 - 两个对象相加;                                    - 减 - 得到负数或是一个数减去另一个数;
# * 乘 - 两个数相乘或是返回一个被重复若干次的字符串;      / 除 - x除以y;（py2取整，小数四舍五入；py3数学除法）
# % 取模- 返回除法的余数;                                 ** 幂 - 返回x的y次幂;
# // 取整除 - 返回商的整数部分
# python没有自增自减运算符
a = 21
b = 10
c = 0
c = a + b
print ('1 - c 得知为:',c)
c = a - b
print ('2 - c 的值为:',c)
c = a * b
print ('3 - c 的值为:',c)
c = a / b
print ('4 - c 的值为:',c)
c = a % b
print ('5 - c 的值为:',c)
# 修改变量 a, b, c
a = 2
b = 3
c = a ** b
print ('6 - c 的值为:',c)
a = 10
b = 5
c = a // b
print ('7 - c 的值为',c)

# 比较运算符
# 结果是布尔值
# == 等于 - 比较对象是否相等
a = 3 ** 4
b = a == 80
print(b)
# != 不等于 - 比较两个对象是否不相等
# <> 不等于 - 比较两个对象是否不相等（py3以后版本没有）   > 大于 - 返回x是否大于y
# < 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。
# >= 大于等于 - 返回x是否大于等于y。                      <= 小于等于 - 返回x是否小于等于y。
a = 21
b = 10
c = 0
if ( a != b ) :
    print ('2 - a 不等于 b')
else:
    print ('2 - a 等于 b')
if ( a < b ):
    print ('4 - a 小于 b')
else:
    print ('4 - a 大于等于 b')
if ( a > b ):
    print ('5 - a 大于 b')
else:
    print ('5 - a 小于等于 b')
# 修改变量 a 和 b 的值
a = 5;
b = 20;
if ( a <= b ):
    print ('6 - a 小于等于 b')
else:
    print ('6 - a 大于 b')
if( b >= a ):
    print ('7 - a 大于等于 b')
else:
    print ('7 - a 小于于 b')

# 赋值运算符
# = 简单的赋值运算符       += 加法赋值运算符           -= 减法赋值运算符
# *= 乘法赋值运算符        /= 除法赋值运算符           %= 取模赋值运算符
# **= 幂赋值运算符         //= 取整除赋值运算符
a = 21
b = 10
c = a +  b
print ('1 - c 的值为', c)
c += a
print ('2 - c 的值为', c)
c *= a
print ('3 - c 的值为', c)
c /= a
print ('4 - c 的值为', c)
c = 2
c %= a
print ('5 - c 的值为', c)
c **= a
print ('6 - c 的值为', c)
c //= a
print ('7 - c 的值为', c)

# 逻辑运算符
# and   逻辑与 - 可看做乘法
# or    逻辑或 - 可看做加法
# not   逻辑非 - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
# python 没有异或运算
a = True
b = False
c = True
d = a and b or c
print(d)
d = a or b and a
print(d)
# 短路问题：一旦能确定表达式的值，则不再进行计算
# a = True or (python 不支持包含表达式)     a = a or (b=9) and 6

# 成员运算符
# 用来检测一个变量是否包含另一个变量
# in  在返回TRUE，否则返回false     not in  在返回false，不在返回TRUE
a = 10
b = 20
list = [1, 2, 3, 4, 5];
if( a in list ):
    print ('1 - 变量 a 在给定的列表 list 中')
else:
    print ('1 - 变量 a 不在给定的列表 list 中')
if( b not in list ):
    print ('2 - 变量 a 不再给定的列表 list 中')
else:
    print ('2 - 变量 b 在给定的列表 list 中')
# 修改变量 a 的值
a = 2
if( a in list ):
    print ('3 - 变量 a 在给定的列表 list 中')
else:
    print ('3 - 变量 a 不在给定的列表 list 中')

# 身份运算符
# is        是判断两个标识符是不是引用自一个对象      x is y, 如果 id(x) 等于 id(y) , is 返回结果 1
# is not    是判断两个标识符是不是引用自不同对象	  x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 1
a = 20
b = 20
if( a is b ):
    print('1 - a 和 b 有相同的标识')
else:
    print ('1 - a 和 b 没有相同的标识')
if( id (a) == id (b) ):
    print ('2 - a 和 b 有相同的标识')
else:
    print ('2 - a 和 b 没有相同的标识')
# 修改变量 b 的值
b = 30
if( a is b ):
    print ('3 - a 和 b 有相同的标识')
else:
    print ('3 - a 和 b 没有相同的标识')
if( a is not b ):
    print ('4 - a 和 b 没有相同的标识')
else:
    print ('4 - a 和 b 有相同的标识')
a = 'i love wangxiaojing'
b = 'i love wangxiaojing'
print(a is b)

# 运算符优先级
# ()        具有最高优先级
# **	    指数 (最高优先级)          ~ + -	                    按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //	乘，除，取模和取整除       + -	                        加法减法
# >> <<	    右移，左移运算符           &	                        位 'AND'
# ^ |	    位运算符                   <= < > >=	                比较运算符
# <> == !=	等于运算符                 = %= /= //= -= += *= **=	    赋值运算符
# is is not	身份运算符                 in not in	                成员运算符
# not or and 逻辑运算符
a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d     #( 30 * 15 ) / 5
print ('(a + b) * c / d 运算结果为：', e)
e = ((a + b) * c) / d   # (30 * 15 ) / 5
print ('((a + b) * c) / d 运算结果为：', e)
e = a + (b * c) / d;      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)
e = (a + b) * (c / d);    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)

# 位运算符 : 二进制计算
# & 按位与运算符 (a & b) 输出结果 12 ，二进制解释： 0000 1100
# | 按位或运算符 (a | b) 输出结果 61 ，二进制解释： 0011 1101
# ^ 按位异或运算符 (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
# ~ 按位取反运算符 (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
# << 左移动运算符 a << 2 输出结果 240 ，二进制解释： 1111 0000
# >> 右移动运算符 a >> 2 输出结果 15 ，二进制解释： 0000 1111
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0
c = a & b;        # 12 = 0000 1100
print ('1 - c 的值为', c)
c = a | b;        # 61 = 0011 1101
print ('2 - c 的值为', c)
c = a ^ b;        # 49 = 0011 0001
print ('3 - c 的值为', c)
c = ~a;           # -61 = 1100 0011
print ('4 - c 的值为', c)
c = a << 2;       # 240 = 1111 0000
print ('5 - c 的值为', c)
c = a >> 2;       # 15 = 0000 1111
print ('6 - c 的值为', c)