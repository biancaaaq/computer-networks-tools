#!/bin/bash

while read domain; do
  for i in {1..10}; do
    echo "Test $i pentru $domain"
    nslookup "$domain" 127.0.0.1 > /dev/null
  done
done < blacklist.txt

