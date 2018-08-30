import threading
# 引入异步 io 包
import asyncio
# 使用协程
# @asyncio.coroutine
# def hello():
#     print('hello world (%s)' % threading.currentThread())
#     print('start (%s)' % threading.currentThread())
#     yield from asyncio.sleep(10)
#     print('done (%s)' % threading.currentThread())
#     print('hello again (%s)' % threading.currentThread())
# # 启动消息循环
# loop = asyncio.get_event_loop()
# # 定义任务
# tasks = [hello(), hello()]
# # asynico 使用 wait 等待 task 执行完毕
# loop.run_until_complete(asyncio.wait(tasks))
# # 关闭消息循环
# loop.close()

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    # 异步请求网络地址
    connect = asyncio.open_connection(host, 80)
    # 注意 yield from 用法
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        # http协议的换行使用\r\n
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()