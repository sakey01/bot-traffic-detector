import re
import sys
import collections
import datetime

# file setup
if len(sys.argv) < 2:
    print("file name missing")
    sys.exit(1)

logFile = 'logs/' + sys.argv[1]

print(f"Analysing {sys.argv[1]}...")

# regex to get IP and timestamp
ip_regex = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")
timestamp_regex = re.compile(r'\[(\d{2}/\d{2}/\d{4}:\d{2}:\d{2}:\d{2})\]')

# request count setup
reqCount = collections.Counter()
timestamps = []
ip_timestamps = collections.defaultdict(list)

# parses file to match regex conditions
with open(logFile, "r") as file:
    for line in file:
        ip_match = ip_regex.match(line)
        timestamp_match = timestamp_regex.search(line)
        if ip_match and timestamp_match:
            ip = ip_match.group(1)
            ts_str = timestamp_match.group(1)
            ts = datetime.datetime.strptime(ts_str, "%d/%m/%Y:%H:%M:%S")
            reqCount[ip] += 1
            timestamps.append(ts)
            ip_timestamps[ip].append(ts)

# finds the duration requests are made over
if timestamps:
    start_date = min(timestamps)
    end_date = max(timestamps)
    duration = end_date - start_date
else:
    start_date = end_date = duration = None

# stores results in ip_alerts.txt
with open('ip_alerts.txt', 'w') as f:
    f.write(f"IP Alerts - Activity over full log duration\n")
    f.write("-------------------------------------------\n\n")

    for ip, count in reqCount.most_common(100):
        if count > 250:
            active_days = max(1, len({ts.date() for ts in ip_timestamps[ip]}))
            avg_per_day = count / active_days if active_days else count
            f.write(f"{ip} - {count} requests, {avg_per_day:.0f} per day over {active_days} days\n")

print ("script successful")