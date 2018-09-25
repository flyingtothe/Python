import time
import threading
def fun():
    print('start fun')
    time.sleep(2)
    print('end fun')
print('mian thread')
t1 = threading.Thread(target=fun, args=())
# 守护线程需在 start 前设置，否则无效
# t1.setDaemon(True)
t1.daemon = True
t1.start()
time.sleep(1)
print('main thread end')