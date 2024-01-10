#!/usr/bin/python3
"""
Function pascal_triangle(n) that returns Pascal's triangle up to n.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/12-pascal_triangle.txt")
