import random
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6666

while True:
    MESSAGE = "%s %s %s" % (
        random.randint(0, 100),
        random.randint(0, 100),
        random.choice(['rebeccapurple'])
    )
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))