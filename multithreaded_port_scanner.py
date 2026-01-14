"""
Multithreaded Port Scanner
--------------------------
Author: Dan Zolotov
Date: 14/01/2026
Description:
    CLI tool to scan a target IP for open ports using multithreading.
    Performs a TCP connect scan and attempts to grab the service banner.

Usage:
    python scanner.py -t <TARGET_IP> [-s <START_PORT>] [-e <END_PORT>] [--threads <NUM>]

    Example:
    python scanner.py -t scanme.nmap.org -s 1 -e 1024
"""

import argparse
import random
import socket
import sys
import threading
from datetime import datetime
from queue import Empty, Queue


def get_arguments():
    """
    Parses command-line arguments using argparse.

    Returns:
        argparse.Namespace: Object containing target, start_port, end_port, and threads.
    """
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner")

    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        required=True,
        help="Target domain or IP address to scan",
    )

    parser.add_argument(
        "-s",
        "--start",
        dest="start_port",
        type=int,
        default=1,
        help="Start Port (default: 1)",
    )
    parser.add_argument(
        "-e",
        "--end",
        dest="end_port",
        type=int,
        default=1024,
        help="End Port (default: 1024)",
    )
    parser.add_argument(
        "--threads",
        dest="threads",
        type=int,
        default=100,
        help="Number of threads (default: 100)",
    )
    parser.add_argument(
        "-r",
        "--random",
        dest="randomise",
        action="store_true",
        help="Randomise the order of ports scanned",
    )

    return parser.parse_args()


# Global Variables
args = get_arguments()
target = args.target
queue = Queue()
open_ports = []


def scan_port(port):
    """
    Attempts to connect to a specific port on the target.
    If successful, attempts to grab the banner and adds the port to the open_ports list.
    """
    try:
        # Create IPv4 TCP socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Prevent hanging on filtered ports
        s.settimeout(1)
        # Attemp connection
        result = s.connect_ex((target, port))

        if result == 0:
            # Banner Grabbing
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "Unknown Service"

            print(f"Port {port} is OPEN: {banner}")
            open_ports.append(port)

        s.close()
    except socket.error as e:
        print(f"Socket error: {e}")


def worker():
    """
    Worker thread function.
    Continuously pulls ports from the queue and scans them until the queue is empty.
    """
    while True:
        try:
            # Prevent thread from blocking if queue becomes empty
            port = queue.get_nowait()
            scan_port(port)
            queue.task_done()
        except Empty:
            break


def run_scanner():
    """
    Main controller function.
    Resolves target, populates queue, spawns threads, and manages execution flow.
    """
    try:  # Verify hostname can be resolved
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Could not resolve hostname: {target}")
        sys.exit()

    print(f"Scanning Target: {target}")
    print(f"Target IP: {target_ip}")
    print(f"Ports: {args.start_port} to {args.end_port}")
    print(f"Threads: {args.threads}")

    # Record start time
    start_time = datetime.now()
    print(f"Scan started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 30)

    ports = list(range(args.start_port, args.end_port + 1))
    # Randomise ports if needed
    if args.randomise:
        random.shuffle(ports)

    # Populate Queue
    for port in ports:
        queue.put(port)

    # Create & start threads
    threads = []
    for _ in range(args.threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)

    for thread in threads:
        thread.start()

    # Wait for completion
    for thread in threads:
        thread.join()  # Ensures main program waits for all threads to finish

    # Record end time
    end_time = datetime.now()
    total_time = end_time - start_time

    print("-" * 30)
    print(f"Scan ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Scan complete. Open ports: \n{sorted(open_ports)}")

    # Dynamic time formatting
    hours, remainder = divmod(total_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        dynamic_time = f"{int(hours)}h {int(minutes)}m {seconds:.2f}s"
    elif minutes > 0:
        dynamic_time = f"{int(minutes)}m {seconds:.2f}s"
    else:
        dynamic_time = f"{seconds:.2f}s"

    print(f"Time elapsed: {dynamic_time}")


if __name__ == "__main__":
    try:
        run_scanner()
    except KeyboardInterrupt:
        print("\n\nScan cancelled by user.")
        sys.exit()
