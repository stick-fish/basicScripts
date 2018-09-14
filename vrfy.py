#!/usr/bin/python

import socket
import sys

''' Short script to probe the SMTP port, if initial username is not successfull
the script loads a short default list of users. The script then tests the default list against
a given host to verify if that user email exists on the system.'''

if len(sys.argv) != 3:
	print 'Usage: ' + sys.argv[0] + ' <username> <host>'
	sys.exit(0)

addr = sys.argv[2]
port = 25
user = sys.argv[1]

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to server
connect = s.connect((sys.argv[2], port))

#Receive the banner
banner = s.recv(1024)
code = banner[0:3]

#VRFY Section
if code == '220':
	print banner
	#VRFY user
	s.send('VRFY ' + sys.argv[1] + '\r\n')
	result = s.recv(1024)
	print result

	if result[0:3] == '550':
		print 'Loading default file...'
		with open('small_username.lst', 'r') as uname:
			for name in uname:
				s.send('VRFY ' + name)
				result = s.recv(1024)
				print result				
	s.close()
else:
	print 'Unsuccessful connection'

#NOTES:

#Codes for SMTP responses https://www.greenend.org.uk/rjk/tech/smtpreplies.html
	#220 - Domain ready
	#250 - Perfect response
	#550 - User does not exist
#My TODO:
	#Clean VRFY section, create function to handle requests to avoid duplication
	#Create try except block for error handling
	#Create summary output for successfull attempts
