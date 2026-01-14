import socket
import threading
from queue import Queue

TARGET = "scanme.nmap.org"  # Safe target provided by Nmap for testing

# Global Variables
queue = Queue()
open_ports = []


def port_scan(port):
    try:
        # Create IPv4 TCP socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Prevent hanging on filtered ports
        s.settimeout(1)
        # Attemp connection
        result = s.connect_ex((TARGET, port))

        if result == 0:
            # Banner Grabbing
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Unknown Service"

            print(f"Port {port} is OPEN : {banner}")
            open_ports.append(port)

        s.close()
    except socket.error:  # Prevent thread crash
        pass


def worker():
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()


def run_scanner(start_port, end_port, thread_count):
    print(f"Scanning TARGET {TARGET} from port {start_port} to {end_port}...")

    # Populate queue
    for port in range(start_port, end_port + 1):
        queue.put(port)

    # Create & start threads
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=worker)
        threads.append(thread)

    for thread in threads:
        thread.start()

    # Wait for completion
    for thread in threads:
        thread.join()  # Ensures main program waits for all threads to finish

    print("-" * 50)
    print(f"\nScan complete. Open ports: \n {sorted(open_ports)}")


if __name__ == "__main__":
    run_scanner(1, 1024, 100)
