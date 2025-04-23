import socket

target = input("enter target: ") 
# enter target like "scanme.nmap.org" or IP like "192.168.1.1"

for port in range(1, 1025):  # Scan ports 1 through 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Timeout if no response
    result = s.connect_ex((target, port))  # Try to connect

    if result == 0:
        print(f"[+] Port {port} is open")

    s.close()
