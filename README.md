# Multithreaded Port Scanner

A simple, multithreaded TCP port scanner written in Python using the `socket` and `threading` modules.

## Features

- **Multithreading**: Uses a queue and worker threads to scan ports concurrently for faster execution.
- **Banner Grabbing**: Attempts to retrieve the service banner for open ports.
- **Configurable**: Easily adjustable target, port range, and thread count.

## Usage

1. **Prerequisites:** Ensure you have Python installed.
2. **Configuration:** Edit the `TARGET` variable in `multithreaded_port_scanner.py` to specify the host you want to scan.
   ```python
   TARGET = "127.0.0.1"
   ```
3. **Run the scanner:**
   ```bash
   python multithreaded_port_scanner.py
   ```

## Disclaimer

This tool is for educational and practice purposes only. Only scan networks or systems you own or have explicit permission to test.
