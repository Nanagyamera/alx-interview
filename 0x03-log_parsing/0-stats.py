#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
from collections import defaultdict


def compute_metrics():
    # Variables to store metrics
    total_file_size = 0
    status_code_counts = defaultdict(int)

    # Counter for lines processed
    line_count = 0

    try:
        for line in sys.stdin:
            # Remove leading/trailing whitespace and split the line
            line = line.strip()
            parts = line.split()

            if len(parts) == 7:
                # Parse the file size as an integer
                file_size = int(parts[6])

                # Update metrics
                total_file_size += file_size
                status_code_counts[parts[4]] += 1

                line_count += 1

            if line_count % 10 == 0:
                # Print statistics after every 10 lines
                print("Total file size:", total_file_size)
                for status_code in sorted(status_code_counts.keys(), key=int):
                    print(status_code + ":", status_code_counts[status_code])
                print()

    except KeyboardInterrupt:
        # If interrupted by CTRL + C, print the final statistics
        print("Total file size:", total_file_size)
        for status_code in sorted(status_code_counts.keys(), key=int):
            print(status_code + ":", status_code_counts[status_code])
        print()

if __name__ == "__main__":
    compute_metrics()
