import threading
import asyncio
# 使用协程
# @asyncio.coroutine
async def hello():
    print('hello world (%s)' % threading.currentThread())
    print('start (%s)' % threading.currentThread())
    await asyncio.sleep(10)
    print('done (%s)' % threading.currentThread())
    print('hello again (%s)' % threading.currentThread())
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()