# # 简单异常案例
# try:
#     num = int(input('输入数字'))
#     rst = 100/num
#     print('计算结果：{0}'.format(rst))
# except:
#     print('aaaa')
#     # exit 退出程序
#     exit()

# 简单异常案例    给出提示信息
# try:
#     num = int(input('输入数字'))
#     rst = 100/num
#     print('计算结果：{0}'.format(rst))
# # 捕获异常后，将异常实例化，错误信息在实例中
# except ZeroDivisionError as e:
#     print('aaaa')
#     print(e)
#     # exit 退出程序
#     exit()
# 如果有多个错误类型，子类异常放在前面，父类异常放在后面

# raise 案例
# try:
#     print('qqqq')
#     print(3.1415926)
#     # 手动引发异常
#     raise ValueError
#     print('meiwan')
# except NameError as e:
#     print('nameerror')
# except ValueError as e:
#     print('valueerror')
# except Exception as e:
#     print('youyichang')
# finally:
#     print('肯定被执行')

# 自定义异常：必须继承系统异常类

# esle 语句案例
# 没有异常时执行，有异常时跳过
# try:
#     num = int(input('输入'))
#     rst = 100/num
#     print('结果：{0}'.format(rst))
# except Exception as e:
#     print('exception')
# else:
#     print('no exception')
# finally:
#     print(';llll')