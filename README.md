# Request Log Analyser

## Overview

A Python script that scans server logs to identify IP addresses with the most requests. Useful for detecting possible bot traffic and server overload.

## Log Format Example

Each log line could look like this:

172.30.1.74 - FR - [02/07/2025:09:18:29] "GET /api/articles HTTP/1.1" 404 1234 "-" "User-Agent" 513

## Requirements

- Python 3.8 or higher

## Usage

1. Place your log file inside the `logs` folder (e.g., `logs/example.log`)
2. Run the script with your log file name as an argument:

```bash
python script.py example.log