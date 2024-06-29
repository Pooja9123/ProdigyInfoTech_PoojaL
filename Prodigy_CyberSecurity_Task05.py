from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        
        # Check if packet has TCP or UDP layer
        if TCP in packet:
            payload = packet[TCP].payload
            print(f"TCP Payload: {payload}")
        elif UDP in packet:
            payload = packet[UDP].payload
            print(f"UDP Payload: {payload}")
        
        print("="*50)

# Sniff network packets with a filter (adjust as needed)
sniff(filter="ip", prn=packet_callback, count=10)
