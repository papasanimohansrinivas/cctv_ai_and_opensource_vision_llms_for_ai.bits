import socket
import struct

UDP_IP = "::1"  # localhost
UDP_PORT = 14000
MESSAGE = "Hello, World!"*64000

hop_limit = 1

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
#print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET6, # Internet
                        socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE.encode("UTF-8"), (UDP_IP, UDP_PORT))

sock.sendmsg([MESSAGE.encode('UTF-8')],
    [(socket.IPPROTO_IPV6, socket.IPV6_HOPLIMIT, struct.pack("i",hop_limit))],
    0, (UDP_IP,UDP_PORT))
