import socket, argparse

def recvall(sock, delimiter):
    data = b''
    while True:
        more = sock.recv(1)
        if more == delimiter:
            break
        data += more
    return data

def client(c_ip, s_ip, filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((c_ip, 1060))
    print('Client has been assigned socket name', sock.getsockname())
    sock.connect((s_ip, 1060))
    in_file = open(filename, 'rb')
    block_size = 32
    snd_bytes = 0
    while True:
        piece = in_file.read(block_size)
        snd_bytes += block_size
        print('\r  %d bytes send' % (snd_bytes,), )
        if piece == "":
            piece = b'bye$'
            sock.sendall(piece)
            break # end of file

        sock.sendall(piece)
    in_file.close()
    message = recvall(sock, b'$')
    print (message)
    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('-c_ip')
    parser.add_argument('-s_ip')
    args = parser.parse_args()
    client(args.c_ip, args.s_ip, "client_send.mkv")