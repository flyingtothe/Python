
def SayHello(name):
    print('i want to say hello sith your,{0}'.format(name))
    print('hello,{0}'.format(name))
    print('done.....')
if __name__ == '__main__':
    print('*' * 20)
    name = input('please input your name:')
    print(SayHello(name=name))
    print('@@' * 10)