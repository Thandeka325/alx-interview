#!/usr/bin/python3
"""
Module to rotate an n x n 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # This transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # This reverse each row
    for row in matrix:
        row.reverse()

