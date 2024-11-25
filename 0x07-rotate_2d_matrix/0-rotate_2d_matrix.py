#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Transpose and then reverse all rows to achieve rotation"""
    n = len(matrix)
    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        # Reverse each row
        matrix[i] = matrix[i][::-1]
