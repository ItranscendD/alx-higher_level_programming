#!/usr/bin/python3
"""
Module for matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix (list of lists): The input matrix.
    div (int or float): The divisor.

    Returns:
    list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats,
               if each row of the matrix doesn't have the same size,
               if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    if type(matrix) is not list or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
