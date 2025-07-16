<<<<<<< HEAD
# Server Logs Analyser
=======
# Request Log Analyser
>>>>>>> d4603cd92c155aa068e457103c114a1d48583283

## Overview

A Python script that scans server logs to identify IP addresses with the most requests. Useful for detecting possible bot traffic and server overload.

<<<<<<< HEAD
=======
## Log Format Example

Each log line could look like this:

172.30.1.74 - FR - [02/07/2025:09:18:29] "GET /api/articles HTTP/1.1" 404 1234 "-" "User-Agent" 513

>>>>>>> d4603cd92c155aa068e457103c114a1d48583283
## Requirements

- Python 3.8 or higher

<<<<<<< HEAD
## How to Use

1. [Download or clone](https://github.com/sakey01/log-reader) the repository from GitHub  
2. Place your log file inside the `logs` folder (e.g., `logs/example.log`)  
3. Open your terminal or command prompt  
4. Navigate to the root directory of the project:

```bash
cd path/to/log-reader
python script.py your-log-name.log
=======
## Usage

1. Place your log file inside the `logs` folder (e.g., `logs/example.log`)
2. Run the script with your log file name as an argument:

```bash
python script.py example.log
>>>>>>> d4603cd92c155aa068e457103c114a1d48583283
