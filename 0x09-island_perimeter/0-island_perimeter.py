#!/usr/bin/python3
"""
Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Start by adding all sides

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract common side

                # Check upper neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract common side

    return perimeter
