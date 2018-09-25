import multiprocessing
from time import ctime

def consumer(input_q):
    print('into condumer:',ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print('pull', item, 'out of q')
    print('out of comsumer:', ctime())      # 此句执行完成，在转入主进程

def producer(sequence, output_q):
    print('into procuder:', ctime())
    for item in sequence:
        output_q.put(item)
        print('put', item, 'into q')
    print('out of procuder:', ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    # 有几个 process 放几个哨兵值
    q.put(None)
    cons_p.join()