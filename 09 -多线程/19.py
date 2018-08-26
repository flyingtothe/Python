import multiprocessing
from time import sleep, ctime

def clock(interval):
    while True:
        print('the tiem id %s' % ctime())
        sleep(interval)
if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    while True:
        print('sleep')
        sleep(1)