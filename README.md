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

### JSON Output

The results can be saved to a JSON file for further analysis or reporting. This includes scan metadata and detailed findings.

### Testing Suite

Includes a comprehensive test suite using `pytest` and `unittest.mock` to ensure reliability and correct functionality of core components.

## Usage

1. **Prerequisites:** Ensure you have Python installed.
2. **Run the scanner:**
   Run the script from the command line, specifying the target IP or domain.

   ```bash
   python scanner.py -t <TARGET_IP>
   ```

   **Arguments:**

   - `-t`, `--target`: Target domain or IP address (**Required**)
   - `-s`, `--start`: Start Port (default: 1)
   - `-e`, `--end`: End Port (default: 1024)
   - `--threads`: Number of threads (default: 100)
   - `-r`, `--random`: Randomise the order of ports scanned
   - `-o`, `--output`: Path to save the results as a JSON file

   **Examples:**

   Scan `scanme.nmap.org` from port 1 to 1024 with 100 threads:

   ```bash
   python scanner.py -t scanme.nmap.org -s 1 -e 1024 --threads 100
   ```

   Scan with randomized order and save results to JSON:

   ```bash
   python scanner.py -t scanme.nmap.org -o results.json -r
   ```

## Disclaimer

This tool is for educational and practice purposes only. Only scan networks or systems you own or have explicit permission to test.
