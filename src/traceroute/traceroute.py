from scapy.all import * #importtoate functiile din scapy pentru creare si trimitere pachete
import socket #obtine IP -urilor dupa numele de domeniu
import sys #pentru citirea arg din linia de comanda
import requests #pt apelare IP-uri din ip-api.com

def get_ip_location(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=3) #apelez ip-ami.com sa aflu locatia unui IP
        data = r.json()
        return f"{data.get('city', 'N/A')}, {data.get('regionName', 'N/A')}, {data.get('country', 'N/A')}" #returnez string cu locatia
    except:
        return "Locatie necunoscuta" #daca nu merge conexiunea

def traceroute_extended(dest_name, max_hops=30):
    dest_ip = socket.gethostbyname(dest_name) #obtine ip-ul real pentru domeniu dat
    print(f"Traceroute catre {dest_name} [{dest_ip}]:")
    results = []

    for ttl in range(1, max_hops + 1): #parcurg fiecare TTL de la 1 la 30 routere
        pkt = IP(dst=dest_ip, ttl=ttl) / UDP(dport=33434) #creez pachet IP cu TTL fixat
        reply = sr1(pkt, verbose=0, timeout=2) #trimit pachetul si astept rasp 2 secunde

        if reply is None:
            print(f"{ttl}. * * *")
            results.append((ttl, "*", ""))
        elif reply.type == 3:  #pachet ICMP de tip 3 gen Destination Unreachable adica am ajuns la destinatie ca portul nu exista
            location = get_ip_location(reply.src)
            print(f"{ttl}. {reply.src} (destinatie atinsa) → {location}")
            results.append((ttl, reply.src, location))
            break 
        else:  #in general type 11 adica ICMP Time Exceeded , am ajuns pana la un router intermediar
            location = get_ip_location(reply.src)
            print(f"{ttl}. {reply.src} → {location}")
            results.append((ttl, reply.src, location))

    return results

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilizare: sudo python3 traceroute.py <domeniu> <fisier_output>")
    else:
        domain = sys.argv[1]
        output_file = sys.argv[2]
        result = traceroute_extended(domain)

        with open(output_file, "w") as f:
            f.write(f"Traceroute catre {domain}\n\n")
            for ttl, ip, location in result:
                f.write(f"{ttl}. {ip} → {location}\n")

        print(f"\n Rezultat salvat in: {output_file}")

