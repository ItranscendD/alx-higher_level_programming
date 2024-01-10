#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys
import signal

def compute_metrics():
    """
    Compute metrics and print statistics.
    """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            split_line = line.split()
            if len(split_line) >= 9:
                status_code = split_line[-2]
                file_size = split_line[-1]

                if status_code in status_codes:
                    total_size += int(file_size)
                    status_codes[status_code] += 1

            if i % 10 == 0:
                print(f"File size: {total_size}")
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print(f"{code}: {count}")

    except KeyboardInterrupt:
        print(f"\nFile size: {total_size}")
        for code, count in sorted(status_codes.items()):
            if count > 0:
                print(f"{code}: {count}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signal, frame: compute_metrics())
    compute_metrics()
