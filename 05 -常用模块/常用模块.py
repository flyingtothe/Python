# claendar 案例
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周多占用额行数
# c = 每个月之间的间隔字符数
import calendar
# cal = calendar.calendar(2017)
# print(type(cal))
# print(cal)

# isleap:判断莫一年是否是闰年
# print(calendar.isleap(2002))

# leapdays:获取指定年份之间的闰年个数
# print(calendar.leapdays(2000,2018))

# moth() 获取某个月的日历字符串
# 格式：calendar.mothh(年， 月）
# 返回值：月日历的字符串
# m3 = calendar.month(2018, 3)
# print(m3)

# monthrange() 获取一个月的周几开始和天数
# w, t = calendar.monthrange(2017, 3)
# print(t)
# print(w)

# monthclaendar() 返回一个月每天的矩阵列表
# 返回值：二级列表
# 注意：矩阵中没有天数用0表示
# m = calendar.monthcalendar(2018, 3)
# print(type(m))
# print(m)

# # prcal:print calendar 直接打印日历
# calendar.prcal(2018)

# prmonth() 打印整月日历
# calendar.prmonth(2013, 3)
#
# # weekday() 获取周几
# print(calendar.weekday(2018, 3, 26))


# time模块案例
# 导入模块
import time

# 时间模块的属性
# timezone：当前时区和utc时间相差的秒数，在没夏令时的情况下
# print(time.timezone)

# altzong：当前时区和utc时间相差的秒数，在夏令时的情况下
# print(time.altzone)

# daylight：检测当前是否是夏令时状态， 0 表示是
# print(time.daylight)

# 得到时间戳
# print(time.time())

# 获取当前时间的时间结构
# t = time.localtime()
# print(t.tm_hour)

# asctime()：返回元祖的正常字符串化之后的时间格式
# t = time.localtime()
# tt = time.asctime(t)
# print(type(tt))
# print(tt)

# ctime()：获取字符串化的当前时间
# t = time.ctime()
# print(type(t))
# print(t)

# mktime()：使用时间元组获取对应的时间戳
# 返回值：浮点数
# lt = time.localtime()
# ts = time.mktime(lt)
# print(type(ts))
# print(ts)

# clock：获取CPU时间，3.0-3.0可使用，不在范围内调用有问题
# def p():
#     time.sleep(2.5)
# t0 = time.clock()
# # p()
# time.sleep(5)
# t1 = time.clock()

# sleep：使程序进入睡眠，到时间后继续
# for i in range(10):
#     print(i)
#     time.sleep(0.5)

# strftime：将时间元组转化为自定义的字符串格式
'''
%y 两位数的年份表示（00-99）                    %Y 四位数的年份表示（000-9999）
%m 月份（01-12）                                %d 月内中的一天（0-31）
%H 24小时制小时数（0-23）                       %I 12小时制小时数（01-12）
%M 分钟数（00=59）                              %S 秒（00-59）
%a 本地简化星期名称                             %A 本地完整星期名称
%b 本地简化的月份名称                           %B 本地完整的月份名称
%c 本地相应的日期表示和时间表示                 %j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符                       %U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始              %W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示                           %X 本地相应的时间表示
%Z 当前时区的名称                               %% %号本身
'''
# t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(t)

# datetime案例
# import datetime

# 常见属性
# datetime.date:一个理想化的日期，提供年、月、日属性
# t = datetime.date(2018, 3, 26)
# print(t)
# print(t.day)
# print(t.year)
# print(t.month)

# datetime.time：提供一个理想化的时间，提供时、分、秒等属性
# from datetime import datetime
# 常用方法
# dt = datetime(2018, 3, 26)
# today
# print(dt.today())
# now
# print(dt.now())
# utcnow
# print(dt.utcnow())
# fromtimestamp：从时间戳中返回本地时间
# print(dt.fromtimestamp(time.time()))

# datetime.datetime：提供提起与时间的组合
# from datetime import datetime as dt
# print(dt.now())

# datetime.timedlta：提供一个时间差
# from datetime import datetime, timedelta
# t1 = datetime.now()
# print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# # 表示一小时的时间长度
# td = timedelta(hours=1)
# # 当前实际啊你加上时间间隔后，将得到的时间格式化输出
# print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

# timeit：时间测量工具
# 测量程序运行时间间隔
# def p():
#     time.sleep(3.6)
# t = time.time()
# p()
# print(time.time() - t)
# 比较列表生成时间
import timeit
# c = '''
# sum = []
# for i in range(1000):
#     sum.append(i)
# '''
# t1 = timeit.timeit(stmt='[i for i in range(1000)]', number=100000)
# t2 = timeit.timeit(stmt=c, number=100000)
# print(t1)
# print(t2)
# 测量函数执行时间
# def doIt():
#     num = 3
#     for i in range(num):
#         print('repeat for {0}'.format(i))
# t = timeit.timeit(stmt=doIt, number=10)
# print(t)

# s = '''
# def doIt(num):
#     for i in range(num):
#         print("repeat for {0}".format(i))
# '''
# # 执行doIt(num)
# # setup负责将环境准备好
# t = timeit.timeit('doIt(num)', setup=s+'num=3',number=10)
# print(t)


# os模块
# getcwd()：获取当前的工作目录,返回字符串
import os
# mydir = os.getcwd()
# print(mydir)

# chdir()：改变当前工作目录
# os.chdir(路径)

# listdir()：获取一个目录中都有子目录和文件的名称列表
# ld = os.listdir()
# print(ld)

# makedir()：递归创建文件夹
# makedir(路径)

# system()：运行系统shell命令
# rst = os.system("ls")
# # print(rst)

# getenv()：获取制定的系统环境变量值
# ret = os.getenv('PATH')
# print(ret)

# exit(）：退出当前程序


# 值案例
# print(os.pardir)
# print(os.curdir)
# print(os.sep)
# print(os.linesep)
# print(os.name)

# os.path模块
import os.path as op

# abspath()：将路径转化为绝对路径
# 一个点代表当前目录     两个点代表父目录
# absp = op.abspath(".")
# print(absp)

# basename()获取路径中的文件名部分，返回文件名字符串
# bn = op.basename('e:/python')
# print(bn)

# join()：将多个路径拼接为一个路径
# bd = '/home/tlxy'
# fn = 'dana.haha'
# p = op.join(bd, fn)
# print(p)

# split()：经路径切割为文件夹部分和当前文件部分，返回路径和文件名组成的元组
# t = op.split('/home/tlxy/dana.haha')
# print(t)
# d,p = op.split('/home/tlxy/dana.haha')
# print(d, p)

# isdir()：检测是否是目录，返回布尔值
# rst = op.isdir('/home/tlxy/dana.haha')
# print(rst)

# exists()：检测文件或目录是否存在,返回布尔值
# e = op.exists('/home/tlxy/dana.haha')
# print(e)


# shuyil模块
import shutil

# copy()：复制     返回目标路径
# 拷贝同时可给文件重命名




# rst = shutil.copy('/home/tlxy/dana.haha', '/home/tlxy/haha.haha')
# print(rst)

# copy2()：复制文件，保留元数据（文件信息）  返回目标路径

# copyfile()：将一个文件中的内容复制到另一个文件中
# rst = shutil.copyfile('dana.haha', 'haha.haha')
# print(rst)

# move()：移动文件/文件夹
# rst = shutil.move('home/tlxy/dana.haha', 'home/tlxy/dana')
# print(rst)


# 归档和压缩案例

# make_archive()：归档操作   返回归档后地址
# shutil.make_archive(归档之后的目录和文件名， 后缀， 需要归档文件）
# rst = shutil.make_archive('home/tlxy/tuling', 'rar', 'home/tlxy/dana')
# print(rst)

# unpack_archive():解包操作     返回解包后的地址

# zip-压缩包   模块名：zipfile
# import zipfile

#zipfile.ZipFile(file[, mode[,compression[, allowZip64]]])
# zf = zipfile.ZipFile('/home/tlxy/tuling.zip')

# ZipFile.getinfo(name)：获取zip文档中指定的文件信息，返回zipfile.ZuoUnfo对象，包括文件详细信息
# rst = zf.getinfo('dana.haha')

# ZipFile.namelist()：获取zip文档内所有文件的名称列表
# nl = zf.namelist()
# print(nl)

# ZipFile.extractall([path[, memners[, ped]]])：解压zip文档中的所有文件到当前目录。members:默认值为zip文档内的都有文件名称列表
# rst = zf.extractall('/home/tlxy/tuling')
# print(rst)


# random案例
import random

# random()：获取 0-1 之间的随机小数   返回 0-1 之间的小数
# print(random.random())

# choice()：随即返回序列中的某个值
# l = [str(i)+'haha' for i in range(10)]
# print(l)
# rst = random.choice(l)
# print(rst)

# shuffle()：随机打乱列表  返回打乱后的列表
# l1 = [i for i in range(10)]
# print(l1)
# random.shuffle(l1)
# print(l1)

# randint(a, b)：返回一个 a 到 b 之间的随机整数，包含 a 和 b
# print(random.randint(0, 100))