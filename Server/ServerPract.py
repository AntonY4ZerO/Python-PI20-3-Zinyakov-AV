import socket

print('запуск сервера')
sock = socket.socket()
sock.bind(('', 1337))
print('начало прослушивания порта')
sock.listen(0)
conn, addr = sock.accept()
print('подключение пользователя')
print(addr)

msg = ''

while msg != 'exit':
    data = conn.recv(1024)
    msg = data.decode()
    print('получение данных пользователя:')
    print(msg)
    conn.send(data)

conn.close()
print('остановка сервера')
