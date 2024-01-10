#!/usr/bin/python3
"""Lazy Matrix multiplication using NumPy
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or contains elements that are not integers or floats.
        ValueError: If m_a or m_b is empty or not a rectangle,
                     or if the matrices can't be multiplied.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list)
                        else "m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists"
                        if not all(isinstance(row, list) for row in m_a)
                        else "m_b must be a list of lists")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a) \
       or any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_a should contain only integers or floats"
                        if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a)
                        else "m_b should contain only integers or floats")

    if not all(len(row) > 0 for row in m_a) or not all(len(row) > 0 for row in m_b):
        raise ValueError("m_a can't be empty" if not all(len(row) > 0 for row in m_a)
                         else "m_b can't be empty")

    if len(set(len(row) for row in m_a)) != 1 or len(set(len(row) for row in m_b)) != 1:
        raise ValueError("each row of m_a must be of the same size"
                         if len(set(len(row) for row in m_a)) != 1
                         else "each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    result = np.dot(np_a, np_b)
    return result.tolist()

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/101-lazy_matrix_mul.txt")
