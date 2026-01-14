# Multithreaded Port Scanner

A simple, multithreaded TCP port scanner written in Python using the `socket` and `threading` modules.

## Features

- **Multithreading:** Uses a queue and worker threads to scan ports concurrently for faster execution.
- **Banner Grabbing:** Attempts to retrieve the service banner for open ports.

### Command Line Interface

Allows for easy configuration of the target, port range, thread count, and scanning mode directly from the terminal.

### Randomised Scanning

Scanner provides an option to shuffle the order of ports to be scanned. This avoids sequential scanning patterns often flagged by intrusion detection systems.

### Integrity Checking

Includes coverage verification step at the end of the scan to confirm that every port in the specified range was processed.

### Smart Duration Reporting

Scan execution time is tracked and displayed in a dynamic, human-readable format.

### Error Handling

The scanner gracefully handles common issues such as invalid hostnames, socket connection errors, and user interruptions.

## Usage

1. **Prerequisites:** Ensure you have Python installed.
2. **Run the scanner:**
   Run the script from the command line, specifying the target IP or domain.

   ```bash
   python multithreaded_port_scanner.py -t <TARGET_IP>
   ```

   **Arguments:**

   - `-t`, `--target`: Target domain or IP address (**Required**)
   - `-s`, `--start`: Start Port (default: 1)
   - `-e`, `--end`: End Port (default: 1024)
   - `--threads`: Number of threads (default: 100)
   - `-r`, `--random`: Randomise the order of ports scanned

   **Example:**
   Scan `scanme.nmap.org` from port 1 to 500 with 50 threads:

   ```bash
   python multithreaded_port_scanner.py -t scanme.nmap.org -s 1 -e 500 --threads 50
   ```

## Disclaimer

This tool is for educational and practice purposes only. Only scan networks or systems you own or have explicit permission to test.
