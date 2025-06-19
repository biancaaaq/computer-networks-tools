
FROM python:3.12-slim
#lucram in containerul app
WORKDIR /app

COPY dns_server.py blacklist.txt ./
#copiem cele 2 fisiere
RUN pip install --no-cache-dir scapy
#executa scriptul din fisier
CMD ["python", "dns_server.py"]
