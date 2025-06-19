#imaginea de baza
FROM snisioi/retele:2021

RUN apt-get update && apt-get install -y iptables iproute2 libnetfilter-queue-dev whois

RUN pip3 install --upgrade python-iptables cython
#copuaza toate fisierele .sh din src in folderul nou creat scripts
RUN mkdir -p /scripts
COPY src/*.sh /scripts/

