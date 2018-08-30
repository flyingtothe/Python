import threading
sum = 0
loopSunm = 10000000
def myAdd():
    global sum, loopSunm
    for i in range(1, loopSunm):
        sum += 1
def myMinu():
    global sum, loopSunm
    for i in range(1, loopSunm):
        sum -= 1
if __name__ == '__main__':
    print('start {0}'.format(sum))
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu(), args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('done {0}'.format(sum))