import socket 
import struct
import binascii
import os
import helper

i = 0

s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

print '[*] packet get'

while True:
    pkt=s.recvfrom(65565)
    unpack=helper.unpack()

    print "\nEthernet Header"
    for i in unpack.eth_h(pkt[0][0:14]).iteritems():
        a,b=i
        print "{} : {}\n".format(a,b),

    print "\nIP Header"
    for i in unpack.ip_h(pkt[0][14:34]).iteritems():
        a,b=i
        print "{} : {}\n".format(a,b),

    print "\nTcp Header"
    for  i in unpack.tcp_h(pkt[0][34:54]).iteritems():
        a,b=i
        print "{} : {}\n".format(a,b),
