import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8093))
sock.listen(1)

while True:
    connection, client_address = sock.accept()

    print(client_address)

    data = connection.recv(1024)

    for line in data.decode().split('\n'):
        print(line)

    connection.close()
