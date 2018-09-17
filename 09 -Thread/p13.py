# coding=utf-8

# python2
# from Queue import Queue

# python3
import queue
import threading
import time
class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize 返回 queue 内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品' + str(count)
                    # 向 queue 中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Counsumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # 从 queue 中取出值
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Counsumer()
        c.start()
