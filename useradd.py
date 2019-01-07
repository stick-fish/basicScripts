#!/usr/bin/python

# Simple script to add a user to a windows system regular user (python pyinstaller.py --onefile useradd.py)
import subprocess

user_add = subprocess.call('net user stickfish secret /add',shell=True)

if user_add == 0 :
        print '[+] User stickfish added to system'
        subprocess.call('net user stickfish',shell=True)
        # subprocess.call('net localgroup Administrators stickfish /add'),shell=True)
else:
        print '[!] User add unsucessful'
