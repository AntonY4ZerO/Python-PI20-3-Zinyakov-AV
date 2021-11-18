import threading
from socket import *
import pyprind


N = 2 ** 16 - 1
ip = input('Enter IP: ')


def scan_port(ip, port):
    global z
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        if port!=0:
            z.append(port)
        sock.close()
    except:
        pass
bar = pyprind.ProgBar(N)
z=[]
for i in range(N):
    thr = threading.Thread(target=scan_port, args=(ip, i))
    thr.start()
    bar.update()
for i in z:
    print('Port', i, 'is opened')

