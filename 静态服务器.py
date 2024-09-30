import socket

def service_client(new_socket):
    request=new_socket.recv(1024)
    print(request)
    response='HTTP/1.1 200 OK \r\n'
    response +='\r\n'
    response += '你好，欢迎来的我的服务器 :)'
    response +='\r\n'
    response += '这是用python搭建的静态服务器'
    response +='\r\n'
    response += '#############################'
    new_socket.send(response.encode('GBK'))
    new_socket.close()
    

def main():
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    tcp_server_socket.bind(('',80))
    tcp_server_socket.listen(128)
    while True:
        new_socket,client_addr=tcp_server_socket.accept()
        service_client(new_socket)


if __name__ == "__main__":
    main()

