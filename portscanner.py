import socket 

target = input("Enter the IP address to Scan : ")
portrange = input("Enter the port range to scan (ex 5-500):")

lowport = int(portrange.split("-")[0])
highport = int(portrange.split("-")[1])

print("Scanning Host ", target , "from port", lowport , "to port", highport )

for port in range(lowport, highport ):
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	status = s.connect_ex((target,port))
	if(status == 0):
		print("** Port ", port ,"- OPEN ***")
#	else: 
#		print ("port", port , "-CLOSED*")
	s.close()

