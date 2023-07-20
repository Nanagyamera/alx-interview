#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            parts = line.split()
            
            if len(parts) != 9 or parts[2] != "GET" or not parts[6].isdigit():
                continue

            ip, _, _, _, _, _, status_code, file_size = parts
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
