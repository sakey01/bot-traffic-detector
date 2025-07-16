import re
import sys
import collections

# file setup
if len(sys.argv) < 2:
    print("file name missing")
    sys.exit()

logFile = 'logs/' + sys.argv[1]

# regex to get IP
regex = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")

# request count setup
reqCount = collections.Counter()

# parses file to match regex conditions
with open(logFile, "r") as file:
    for line in file:
        match = regex.match(line)
        if match:
            ip = match.group(1)
            reqCount[ip] += 1

# prints IPs with requests over 300
print("Most Common Requests")
for i, count in reqCount.most_common(100):
    if (count > 300):
        print(f"{i}: {count} requests")

# exports ips to a txt file
with open('ip_alerts.txt', 'w') as f:
    f.write("FLAGGED\n")
    for ip, count in reqCount.items():
        if count >= 300:
            f.write(f"{ip} - {count} requests\n")