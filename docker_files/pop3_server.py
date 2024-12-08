# pop3_server.py
import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    conn.sendall(b'+OK POP3 server ready\r\n')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode().strip()
        print(f"Received: {command}")
        if command.upper() == 'QUIT':
            conn.sendall(b'+OK Goodbye\r\n')
            break
        elif command.upper().startswith('USER'):
            conn.sendall(b'+OK User accepted\r\n')
        elif command.upper().startswith('PASS'):
            conn.sendall(b'+OK Password accepted\r\n')
        elif command.upper() == 'STAT':
            conn.sendall(b'+OK 0 0\r\n')
        elif command.upper() == 'LIST':
            conn.sendall(b'+OK No messages\r\n.\r\n')
        else:
            conn.sendall(b'-ERR Unknown command\r\n')
    conn.close()
    print(f"Connection with {addr} closed")

def main():
    host = '0.0.0.0'
    port = 110  # POP3 default port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"POP3 server listening on port {port}")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == '__main__':
    main()
