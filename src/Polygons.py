import numpy as np


def combine_matrices(matrices):
    combined = np.zeros_like(matrices[0])
    for matrix in matrices:
        combined = np.where(matrix == 1, matrix, combined)
    return combined


def flood_fill(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0])

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if matrix[x][y] != 0:
        return

    matrix[x][y] = 1

    flood_fill(matrix, x + 1, y)
    flood_fill(matrix, x - 1, y)
    flood_fill(matrix, x, y + 1)
    flood_fill(matrix, x, y - 1)


def scanline_fill(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        intersections = []
        for col in range(cols):
            if matrix[row][col] == 1:
                intersections.append(col)

        if len(intersections) % 2 != 0:
            intersections.append(cols - 1)

        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                for col in range(intersections[i] + 1, intersections[i + 1]):
                    matrix[row][col] = 1

    return matrix