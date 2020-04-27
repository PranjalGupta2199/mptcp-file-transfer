import socket, argparse

def recvall(filename, sock, delimiter):
    file_ = open(filename, 'wb')
    recvd_bytes = 0
    data = b''
    while True:
        more = sock.recv(1024)
        data += more
        if data[-4:] == delimiter:
            break
        data = data[-10:]
        file_.write(more)
        file_.flush()

    file_.close()

def server(ip, port, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    sock.listen(10)
    print('Listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        recvall(filename, sc, b'bye$')
        sc.sendall(b'Thank you$')
        sc.close()
        print('  Reply sent, socket closed')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    server(args.host, args.p, "server_recvd.mkv")