#!/usr/bin/python3
"""
Pascal Triangle
"""

def pascal_triangle(n):
    '''
    Creates a list of lists of integers that represents Pascal's triangle
    of a given integer `n`.
    '''
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    res = []  # Initialize the list to hold the rows of Pascal's triangle

    for i in range(n):
        # First row is always [1]
        if i == 0:
            res.append([1])
        else:
            row = [1]  # Start each row with 1

            # Calculate the values in the middle of the row
            for j in range(1, len(res[-1])):
                row.append(res[-1][j] + res[-1][j - 1])

            row.append(1)  # End each row with 1
            res.append(row)  # Append the row to the result

    return res
