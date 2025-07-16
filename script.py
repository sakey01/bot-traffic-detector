import re
import sys
import collections

# file setup
if len(sys.argv) < 2:
    print("file name missing")
    sys.exit()

logFile = 'logs/' + sys.argv[1]

# regex to get IP and timestamp
ip_regex = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")
timestamp_regex = re.compile(r'\[(\d{2}/\d{2}/\d{4}:\d{2}:\d{2}:\d{2})\]')

# request count setup
reqCount = collections.Counter()

# parses file to match regex conditions
with open(logFile, "r") as file:
    for line in file:
        match = ip_regex.match(line)
        if match:
            ip = match.group(1)
            reqCount[ip] += 1

# stores flagged IPs as a txt
with open('ip_alerts.txt', 'w') as f:
    f.write("Most Common Requests\n")
    for i, count in reqCount.most_common(100):
        if count > 250:
            f.write(f"{i} - {count} requests\n")
    print("Script Succesfull")
        