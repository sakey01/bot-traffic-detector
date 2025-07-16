# import required libraries
import re
import collections

# file path for logs (replace 'example.log' with your own file)
logFile = "logs/example.log"

# regex to get IP
regex = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")

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