# Multithreaded Port Scanner

A simple, multithreaded TCP port scanner written in Python using the `socket` and `threading` modules.

## Features

- **Multithreaded:** Uses a queue and worker threads to scan ports concurrently for faster execution.
- **Banner Grabbing:** Attempts to retrieve the service banner for open ports.
- **Randomised Scanning:** Option to shuffle the order of ports to scan.
- **Command Line Interface:** Easily configurable via command-line arguments.
- **Smart Duration Reporting:** Displays elapsed time in a human-readable format.
- **Error Handling:** Gracefully handles invalid hostnames, socket errors, and user interrupts.

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
