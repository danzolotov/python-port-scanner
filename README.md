# Multithreaded Port Scanner

[![CI](https://github.com/danzolotov/multithreaded-port-scanner/actions/workflows/ci.yml/badge.svg)](https://github.com/danzolotov/multithreaded-port-scanner/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A multithreaded TCP port scanner written in Python using only the standard library (`socket`, `threading`, `queue`). Designed as a portfolio project demonstrating concurrent networking, CLI design, and software testing practices.

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

### Docker Support

Run the scanner without installing Python directly — use the provided `Dockerfile` to build a self-contained image.

## Usage

1. **Prerequisites:** Ensure you have Python 3.10+ installed (or Docker).
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

3. **Run with Docker:**

   ```bash
   docker build -t port-scanner .
   docker run --rm port-scanner -t scanme.nmap.org -s 1 -e 1024
   ```

## Development

Install development dependencies and run the test suite:

```bash
pip install -r requirements-dev.txt
pytest test_scanner.py -v
flake8 scanner.py test_scanner.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full contribution guidelines.

## Roadmap

Planned improvements are tracked in [ROADMAP.md](ROADMAP.md) and on the [GitHub Project board](https://github.com/danzolotov/multithreaded-port-scanner/projects). Highlights include UDP scanning, asyncio rewrite, additional output formats, and OS fingerprinting.

## Disclaimer

This tool is for educational and practice purposes only. Only scan networks or systems you own or have explicit permission to test.
