LOG FILE METRICS CALCULATOR

This Python script reads input from stdin line by line and computes metrics based on the input format. It then prints the statistics after every 10 lines or when interrupted by a keyboard interruption (CTRL + C).

INPUT FORMAT

The input format should follow the following pattern:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

If the line doesn't match this format, it will be skipped by the script.

METRICS COMPUTED

The script computes the following metrics:

1. Total file size: The sum of all previous file sizes processed.

2. Number of lines by status code: Counts the occurrences of different status codes (200, 301, 400, 401, 403, 404, 405, and 500) in the input.

SOLUTION APPROACH

The script uses a loop to read input line by line. It keeps track of the total file size and the count of each status code in a dictionary using the `defaultdict` from the `collections` module.

The script handles keyboard interruptions (CTRL + C) and prints the statistics computed so far after every 10 lines or when interrupted.

USAGE

To use the script, you can run it from the terminal and provide the input either by piping the contents of a log file or by typing the input manually.

```shell
python 0-stats.py < input.log
Replace input.log with the filename of your input log file. Alternatively, you can provide the input manually by typing it in the terminal.

CONCLUSION
The Log File Metrics Calculator script provides a convenient way to calculate and monitor metrics based on the input log file. It can be used to quickly get insights into the total file size and the distribution of status codes in the log data.
