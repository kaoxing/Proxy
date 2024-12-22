import logging
import select
import socket
import struct
from socketserver import StreamRequestHandler, ThreadingTCPServer
from cryptor import encrypt_data_aes256, decrypt_data_aes256, encrypt_data_chacha20_poly1305

logging.basicConfig(level=logging.DEBUG)
SOCKS_VERSION = 5


# shadowsocks客户端实现
if __name__ == '__main__':
    # 本地监听端口
    LOCAL_HOST = '127.0.0.1'
    LOCAL_PORT = '9527'
    # 远端服务器地址
    REMOTE_SERVER = '127.0.0.1'
    # 远端服务器端口
    REMOTE_PORT = '9527'
    # chacha20-poly1305密钥
    key = b'0123456789abcdef0123456789abcdef'

    # 创建一个socket对象，连接远端服务器（shadowsocks服务器）
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((REMOTE_SERVER, int(REMOTE_PORT)))


    # 创建一个socket对象，本地监听
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind((LOCAL_HOST, int(LOCAL_PORT)))

