import socket
import sys

if len(sys.argv) < 2:
    print("Set host ip ex.: {} 127.0.0.1".format(sys.argv[0]))
    exit()

target = sys.argv[1]
print("Scanning host with ip {}".format(target))

for port in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

