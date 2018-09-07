#!/usr/bin/python3
import os

''' Basic IP ping sweeper, just specify range for the last octet. Then specify first 3 octets in
in target range for a /24 subnet. Ping sweeper will then pipe various bash
commands to output just a standard IPv4 address if found. '''

# Host scan range
hosts = range(0,254)

# ips eg: "192.168.1"
ip = "X.X.X"

# Text file output name
ping_res = 'results_ping.txt'

# Loops through specified range and runs ping command
# Using longer wait time gives a better scan result, change -W to increase or decrease
for i in hosts:
  ip_scan = ip + '.' + str(i)
  command = os.system("ping -c 1 -W 10 '{0}' | grep 'bytes from' | cut -d ' ' -f 4 | sed s/:/''/ >> '{1}' &".format(ip_scan,ping_res))

#Basic usage to view file
print('To view file contents use: cat',ping_res)
