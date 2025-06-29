#!/bin/bash
set -x
# remove default gateway 172.7.1.1
ip route del default
# make router container the default router
ip route add default via 172.7.0.3
# add route to subnet 172.7.0.0/16 via IP 198.7.0.1
# ip route add 172.7.0.0/16 via 198.7.0.1
# add 8.8.8.8 nameserver
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
# we need to drop the kernel reset of hand-coded tcp connections
# https://stackoverflow.com/a/8578541
iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
