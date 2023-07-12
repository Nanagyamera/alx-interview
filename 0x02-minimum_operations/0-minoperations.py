#!/usr/bin/python3
"""
task 0's module
"""


def minOperations(n):
    # If n is already 1, no operations needed
    if n == 1:
        return 0

    operations = 0  # Total number of operations
    divisor = 2  # Smallest possible factor

    while n > 1:
        if n % divisor == 0:  # Check if divisor is a factor of n
            n //= divisor  # Divide n by the divisor
            operations += divisor  # Add divisor to operations count
        else:
            divisor += 1  # Increment divisor and try the next smallest factor

    return operations
