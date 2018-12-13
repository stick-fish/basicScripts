#!/bin/bash

# Checking Windows users 1.3.6.1.4.1.77.1.2.25
# Open TCP Ports 1.3.6.1.2.1.6.13.1.3
# Software installed 1.3.6.1.2.1.25.6.3.1.2
# Running Windows processes 1.3.6.1.2.1.25.4.2.1.2

for ip in $(cat $1); do
        cmd=$(snmpwalk -c public -v 1 $ip 1.3.6.1.4.1.77.1.2.25);
        printf "[+] Scanning... $ip \n"
        printf "$cmd \n"
        printf "[+] Done \n\n"
done;
