#!/usr/bin/python3
"""
Matrix division module - provides function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div

    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by

    Returns:
        New matrix with elements divided by div, rounded to 2 decimal places
    """
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats")

    # Check if all rows are lists containing only integers/floats
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Create new matrix with divided values
    return [[round(elem / div, 2) for elem in row] for row in matrix]
