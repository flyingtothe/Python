import multiprocessing
from time import ctime
def consumer(input_q):
    print('into condumer:',ctime())
    while True:
        # 处理项
        item = input_q.get()
        print('pull', item, 'out of q')     # 此处替换为有用的任务
        input_q.task_done()     # 发出信号通知任务完成
    print('out of comsumer:', ctime())      # 此句未执行，因为q.join()收集到四个task_done()信号后，主进程启动，未等待完成任务
def producer(sequence, output_q):
    print('into procuder:', ctime())
    for item in sequence:
        output_q.put(item)
        print('put', item, 'into q')
        print('out of procuder:', ctime())
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()
    # 生产多个项，sequence代表要发送给消费者的项序列
    # 在实践中，可能是生成器的输出或通过一些其他方池生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.join()