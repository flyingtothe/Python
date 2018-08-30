import multiprocessing
from time import sleep, ctime
class ClockProcess(multiprocessing.Process):
    '''
    两个参数
    1.init 构造函数
    2.run
    '''
    def __init__(self, interval):
        super().__init__()
        self.interval = interval
    def run(self):
        while True:
            print('the time is %s ' % ctime())
            sleep(self.interval)
if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    while True:
        print('sleep')
        sleep(1)