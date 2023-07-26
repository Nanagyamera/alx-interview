#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import signal


# Dictionary to store the number of lines by status code
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Variables to store the total file size and current line count
total_file_size = 0
line_count = 0

def print_statistics():
    print("Total file size:", total_file_size)
    for status_code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{status_code}: {count}")

try:
    for line in sys.stdin:
        # Split the line into its components
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip lines that don't match the input format

        # Extract the file size and status code from the line
        file_size = int(parts[-1])
        status_code = int(parts[-3])

        # Update metrics
        total_file_size += file_size
        line_count += 1
        status_code_count[status_code] += 1

        # Check if it's time to print statistics
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing current statistics:")
    print_statistics()
    sys.exit(0)
