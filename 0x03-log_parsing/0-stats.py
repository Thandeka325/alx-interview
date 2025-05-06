#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
Expected input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys

# Tracked status codes
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {}
total_size = 0
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        print("{}: {}".format(code, status_count[code]))


try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 7:
            continue
        # Extract status code and file size from the correct positions
        code = parts[-2]
        size = parts[-1]

        try:
            total_size += int(size)
        except ValueError:
            continue

        if code in status_codes:
            status_count[code] = status_count.get(code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
