#  Computer Networks – Security & Tunneling Tools

This repository contains a collection of advanced networking exercises implemented for the **Computer Networks 2025** university project.  
Each component simulates real-world security, communication, and network-layer attacks using **Python**, **Docker**, and **Linux tools**.


##  Contents

- **DNS Ad Blocker**  
  A DNS server that blocks ad-related domains using a blacklist and returns `0.0.0.0` for blocked queries. Tested locally and on a VPS.

- **DNS Tunnel**  
  Implements data exfiltration using DNS queries and responses. Transfers files using TXT records and a stop-and-wait protocol.

- **ARP Spoofing**  
  Performs ARP poisoning between client and server containers. Enables MITM attacks using `Scapy`.

- **TCP Hijacking**  
  Hijacks active TCP sessions and alters payloads mid-stream using `netfilterqueue`. Sessions remain uninterrupted.

- **Traceroute**  
  A custom implementation of the classic `traceroute` utility using increasing TTL and ICMP response handling.



##  Technologies

- **Languages**: Python 3  
- **Tools**: Docker, Docker Compose  
- **Libraries**: `Scapy`, `netfilterqueue`, `socket`, `dnslib`  
- **Platform**: Linux (tested on local and VPS setups)  


