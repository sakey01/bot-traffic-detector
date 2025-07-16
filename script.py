import re
import sys
import collections

# add log file as argument to cli
if len(sys.argv) < 2:
    print("file name missing")
    sys.exit()

logFile = 'logs/' + sys.argv[1]

# regex to get IP
ipRegex = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")

# store IP count
ipCount = collections.Counter()

# parses files
with open(logFile, "r") as file:
    for line in file:
        match = regex.match(line)
        if match:
            ip = match.group(1)
            ipCount[ip] += 1

# prints requests over 300
print("Most Common Requests")
for i, count in ipCount.most_common(100):
    if (count > 300):
        print(f"{i}: {count} requests")