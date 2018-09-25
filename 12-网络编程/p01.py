# 服务器端
import socket

# 模拟服务器的函数
def serverFunc():
    # 建立socket
    # socket.AF_INET：使用IPV4
    # socket.SOCK_DGRAM：使用 UDP 通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定 IP 和 port
    # 地址是一个 tuple 类型(ip, port,)
    addr = ('127.0.0.1', 7852)
    sock.bind(addr)

    # 接收消息
    # recvfrom 接收，返回只是一个元组，前项表示数据，后项表示地址
    # 参数：缓冲区大小
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))

    # 数据是以字节流发送的，接收后需解码转换为 str 格式
    # decode 默认参数是utf-8
    text = data.decode()
    print(type(text))
    print(text)

    # 反馈给对方的消息
    rsp = ' i ha hah jkj'

    # 将数据编码成 bytes 格式
    # 默认 utf-8
    data = rsp.encode()
    sock.sendto(data, addr)     # UDP格式

if __name__ == '__main__':
    print('starting server')
    serverFunc()
    print('end server')