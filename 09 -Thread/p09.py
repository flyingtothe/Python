import threading
import time
# 需继承 threading.Thread
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
    # 必须重写 run 函数
    def run(self):
        time.sleep(2)
        print('thr args for this class is {0}'.format(self.arg))
for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()
print('main thread is done')