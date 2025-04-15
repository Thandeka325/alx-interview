#!/usr/bin/python3
"""
Module for Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # Start each row with 1

        # Add the in-between values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
