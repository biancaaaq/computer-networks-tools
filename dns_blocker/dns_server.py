import socket
import base64
from scapy.all import DNS, DNSQR, DNSRR, IP, UDP
import time

# Incarca fisierul blacklist.txt într un set, ignorand liniile goale și comentariile
with open("blacklist.txt") as f:
    blacklist = set(line.strip() for line in f if line.strip() and not line.startswith("#"))

TUNEL_DOMAIN = "tunel.BBBRETELE.mooo.com"
FILE_PATH = "test.txt"
CHUNK_SIZE = 200

def get_file_chunks():
    with open(FILE_PATH, "rb") as f:
        data = f.read()
    chunks = [data[i:i+CHUNK_SIZE] for i in range(0, len(data), CHUNK_SIZE)]
    return chunks

# Creeaza un socket UDP care asculta cereri DNS pe portul 53
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 53))

while True:
    try:
        data, addr = sock.recvfrom(512)
        print(f"Pachet primit de la {addr}, lungime: {len(data)} bytes")

        if len(data) < 12:
            print(f"Pachet prea scurt: {len(data)} bytes, ignorat")
            continue

        dns = DNS(data)
        if dns.opcode != 0 or dns.qr != 0:
            print(f"Pachet nevalid: opcode={dns.opcode}, qr={dns.qr}, ignorat")
            continue

        qname = dns[DNSQR].qname.decode().strip(".")

        if qname.endswith(TUNEL_DOMAIN):
            parts = qname.split(".")
            if len(parts) > 3 and parts[0].startswith("fragment"):
                chunk_index = int(parts[0].replace("fragment", ""))
                chunks = get_file_chunks()

                if chunk_index < len(chunks):
                    chunk_data = base64.b64encode(chunks[chunk_index]).decode()
                    # Trimite un rsspuns DNS cu bucata de fisier ca date TXT
                    reply = DNS(
                        id=dns.id,
                        qr=1,
                        aa=1,
                        qd=dns.qd,
                        an=DNSRR(rrname=dns.qd.qname, ttl=10, type="TXT", rdata=chunk_data)
                    )
                    sock.sendto(bytes(reply), addr)
                else:
                    reply = DNS(id=dns.id, qr=1, aa=1, qd=dns.qd)
                    sock.sendto(bytes(reply), addr)
        elif qname in blacklist:
            # Blocheaza domeniul trimitand 0.0.0.0 si salveaza în log
            reply = DNS(
                id=dns.id,
                qr=1,
                aa=1,
                qd=dns.qd,
                an=DNSRR(rrname=dns.qd.qname, ttl=10, rdata="0.0.0.0")
            )
            sock.sendto(bytes(reply), addr)
            with open("log_blocari.txt", "a") as log:
                log.write(f"{time.ctime()} - {qname}\n")
                print(f"[{time.ctime()}] Domeniu blocat (log): {qname}", flush=True)
    except Exception as e:
        print(f"Eroare la procesarea pachetului: {e}")
        continue
