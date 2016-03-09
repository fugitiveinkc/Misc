'''

Title: Ping sweeper

Purpose: Create a python script that utilizes ping to ping sweep

Sample run: python ping_sweep.py 1 124
	-argv[1] and argv[2] specify the range
	-assuming local network (192.168.1.---)

Libraries:
	-sys
	-subprocess
	-threading

'''

import sys, subprocess, threading

#1) Read input
#2) Check ip's with threads
#3) Output result

class ip_validation(threading.Thread): #Inherents from Thread so that instances of this class can be threads.
	def __init__(self, ip):
		threading.Thread.__init__(self)
		self.ip = ip
		self.status = None
	def run(self):
		process = subprocess.call(['ping','-c','2',self.ip],stdout=subprocess.PIPE)
		if process == 0:
			self.status = "Active"
		else:
			self.status = "Inactive"
		
threads = []
while True:
	start, end = int(sys.argv[1]), int(sys.argv[2])
	for ip in range(start, end+1): #IP specified range
		thread = ip_validation('192.168.1.' + str(ip)) #Start a thread and check if ping is succesful
		threads.append(thread) #Save threads
		thread.start() #starts thread
	break

for x in threads:
	x.join() #waits until all threads are terminated
	print x.ip + ' is ' + x.status

		
