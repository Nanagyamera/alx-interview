#!/usr/bin/python3
"""
A function that defines the pascal's triangle
"""


def pascal_triangle(n):
    """
    first checks if n is less than or equal to 0 and returns an empty list
    """
    if n <= 0:
        return []

    """
    If n is greater than 0, an initial row [1] is added to the triangle list
    """
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
