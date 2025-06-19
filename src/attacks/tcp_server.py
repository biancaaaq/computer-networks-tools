# TCP Server
import socket  #pt comunic TCP/IP
import logging #pt loguri
import time

logging.basicConfig(format='[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
                        #IPv4            TCP                     protocol
port = 12345
adresa = '0.0.0.0'  #pe toate interfetele adica toate IP urile locale
server_address = (adresa, port)
sock.bind(server_address)  #leaga socketul de adresa
logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
sock.listen(5) #max 5 conexiuni in asteptare

while True:
    logging.info("Asteptam conexiuni...")
    conexiune, address = sock.accept() #blocheaza conexiunea pana se conecteaza cnv
    logging.info("Handshake cu %s", address) # adresa clientului adica

    try:
        while True:
            data = conexiune.recv(1024) #adica primeste pana la 1024 bytes
            if not data:
                break
            logging.info('Content primit: "%s"', data)
            conexiune.send(b"Server a primit mesajul: " + data)
            time.sleep(2)
    except Exception as e:
        logging.error("Eroare in comunicare: %s", e)

    conexiune.close() #inchide socketul pentru clientul curent si se intoarce in while
