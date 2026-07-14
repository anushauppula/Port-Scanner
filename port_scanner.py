import socket

print("Port Scanner Started")
target = input("Enter target IP address: ")  # Mundhu IP teesko
print("Target is:", target)
print(f"Scanning target {target}...")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print("Port", port, "is OPEN")
    
    s.close()

print("Scan complete")
import socket
import threading
from queue import Queue

print("Fast Port Scanner Started")
target = input("Enter target IP address: ")
print(f"Scanning {target}...")

queue = Queue()
open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        s.close()
    except:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

for port in range(1, 1001):  # 1000 ports
    queue.put(port)

thread_list = []
for t in range(100):  # 100 threads
    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()
    thread_list.append(thread)

queue.join()
print(f"\nScan complete. Open ports: {sorted(open_ports)}")
import socket
import threading
from queue import Queue

print("Fast Port Scanner Started")
target = input("Enter target IP address: ")

# Range mundhu teesko
port_range = input("Enter port range e.g 1-1000: ")
start, end = port_range.split('-')
start = int(start)
end = int(end)

print(f"Target is: {target}")
print(f"Scanning {target} ports {start}-{end}...")

queue = Queue()
open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        s.close()
    except:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

# User ichina range ne scan chey
for port in range(start, end + 1):
    queue.put(port)

thread_list = []
for t in range(100):  # 100 threads
    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()
    thread_list.append(thread)

queue.join()
print(f"\nScan complete. Open ports: {sorted(open_ports)}")
