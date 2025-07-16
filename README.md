# Request Log Analyser

## Overview

A Python script that scans server logs to find IP addresses making the most requests. Helps detect possible bot traffic or areas of overload.

## Log Format Example

Each log line should follow this structure:

172.30.1.74 - FR - [02/07/2025:09:18:29] "GET /api/articles HTTP/1.1" 404 1234 "-" "User-Agent" 513

## Requirements

- Python 3.8 or higher

## How to Use

1. Place your log file inside the `/logs` folder (e.g., `logs/example.log`)
2. Run the script:

```bash
python script.py