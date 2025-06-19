# TCP Client
import socket
import logging
import time
import random

logging.basicConfig(format='[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)

port = 12345
adresa = '198.7.0.2'  # IP-ul serverului (containerul `retele-bbb-server`)
server_address = (adresa, port)

try:
    logging.info('Handshake cu %s', str(server_address))
    sock.connect(server_address)

    while True:
     try:
        mesaj = f"Mesaj random de test la {time.time()}"
        sock.send(mesaj.encode('utf-8'))
        data = sock.recv(1024)
        logging.info('Content primit: "%s"', data)
        time.sleep(2)
     except Exception as e:
        logging.error("Eroare: %s", e)
        break
finally:
    logging.info('Inchidere socket.')
    sock.close()
