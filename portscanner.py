## Implement port scanner

import socket
import sys
import time

ip = input("Enter IP address: ")
initial_port = int(input("Enter initial port: "))
final_port = int(input("Enter final port: "))

# Translate hostname to IPv4
try:
    ip = socket.gethostbyname(ip)
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

# Banner
print("-" * 50)
print("Please wait, scanning remote host", ip)
print("-" * 50)

# Check what ports and services are open
try:
    for port in range(initial_port, final_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((ip, port))
        if result == 0:
            service = socket.getservbyport(port, 'tcp')
            print("Port {}: Open - {}".format(port, service))
        else:
            print("Port {}: Closed".format(port))

        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# End of script
print("-" * 50)
print("Scan completed")
print("-" * 50)