import socket
import paramiko

# SSH配置信息
ssh_host = '127.0.0.1'
ssh_port = 22
ssh_username = 'kaoxing'
ssh_password = 'your_ssh_password'

# 代理服务器配置信息
proxy_host = '0.0.0.0'
proxy_port = 8888

def handle_client(client_socket):
    # 建立SSH连接
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

    # 接收来自客户端的数据并转发给SSH服务器
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(data.decode())
        response = ssh_stdout.read()
        client_socket.send(response)

    # 关闭连接
    ssh.close()
    client_socket.close()

def main():
    # 创建代理服务器
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((proxy_host, proxy_port))
    server.listen(5)

    print(f'[+] Listening on {proxy_host}:{proxy_port}')

    while True:
        client_socket, addr = server.accept()
        print(f'[+] Accepted connection from {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
