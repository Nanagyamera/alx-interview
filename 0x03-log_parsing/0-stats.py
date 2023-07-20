#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import re
import sys


def extract_input(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    """
    log_pattern = re.compile(
        r'^(?P<ip>\S+) - \[(?P<date>.*?)\] "GET \/projects\/260 HTTP\/1\.1" (?P<status_code>\d+) (?P<file_size>\d+)'
    )
    match = log_pattern.match(input_line)
    if match:
        return match.groupdict()
    return None

def print_statistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print('File size: {}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{}: {}'.format(status_code, num), flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    line_info = extract_input(line)
    if line_info:
        status_code = line_info.get('status_code')
        if status_code in status_codes_stats:
            status_codes_stats[status_code] += 1
        total_file_size += int(line_info.get('file_size', 0))
    return total_file_size

def run():
    """
    Starts the log parser.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        for line in sys.stdin:
            total_file_size = update_metrics(
                line.strip(),
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_stats)

if __name__ == '__main__':
    run()
