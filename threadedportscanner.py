import socket 
import threading 
from queue import Queue


print_lock = threading.Lock()

target = input("Enter the IP address to Scan : ")
portrange = input("Enter the port range to scan (ex 5-500):")
threads = input("How many threads : ")

lowport = int(portrange.split("-")[0])
highport = int(portrange.split("-")[1])


def portscan(port):
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	try: 
		con = s.connect((target, port))
		with print_lock: 
			print("** Port ", port ,"- OPEN ***")
		con.close()			
	except:
		pass 

def threader(): 
	while True:
		worker = q.get()
		portscan(worker)
		q.task_done()

q = Queue()

for x in range(100):
	t = threading.Thread(target=threader)
	t.daemon = True 
	t.start()

for worker in range(lowport,highport):
	q.put(worker)

q.join()

