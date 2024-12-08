# pop3_client.py
import socket

def main():
    host = '192.168.1.107'  # POP3 server's IP
    port = 110
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    response = s.recv(1024)
    print(response.decode().strip())
    commands = ['USER test', 'PASS test', 'STAT', 'LIST', 'QUIT']
    for cmd in commands:
        s.sendall((cmd + '\r\n').encode())
        response = s.recv(1024)
        print(response.decode().strip())
    s.close()

if __name__ == '__main__':
    main()
