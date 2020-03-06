# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 8 - Affine Gap Penalty
# File: affine.py
# Due date: 3/06/2020

import sys

neg_infinity = -sys.maxsize - 1


def match(i, j):
    if i == j:                                                                  # if bases are the same
        return int(sys.argv[5])                                                 # return match score
    else:
        return int(sys.argv[6])                                                 # return mismatch score


def affine_gap(s1, s2):
    # initialize three matrices used to score
    matrix = []
    matrix_ix = []
    matrix_iy = []
    n = len(s1)
    m = len(s2)

    # get penalties and scores
    h = int(sys.argv[3])
    g = int(sys.argv[4])

    # initialize matrices with starting values
    for i in range(n+1):
        matrix.append([])
        matrix_ix.append([])
        matrix_iy.append([])
        for j in range(m+1):
            if i == 0 and j == 0:                           # M(0, 0) = 0
                matrix[i].append(0)
            else:
                matrix[i].append(neg_infinity)              # all else equal -∞
            if j == 0:
                matrix_ix[i].append(h + g * i)              # Ix(i, 0) = open penalty + gap penalty * index
            else:
                matrix_ix[i].append(neg_infinity)           # all else equal -∞
            if i == 0:
                matrix_iy[i].append(h + g * j)              # Iy(0, j) = open penalty + gap penalty * index
            else:
                matrix_iy[i].append(neg_infinity)           # all else equal -∞

    # fill in matrices based on affine gap penalty scores
    for i in range(1, n+1):
        for j in range(1, m+1):
            matrix[i][j] = max(matrix[i-1][j-1] + match(s1[i-1], s2[j-1]),
                               matrix_ix[i-1][j-1] + match(s1[i-1], s2[j-1]),
                               matrix_iy[i-1][j-1] + match(s1[i-1], s2[j-1]))
            matrix_ix[i][j] = max(matrix[i-1][j] + h + g,
                                  matrix_ix[i-1][j] + g)
            matrix_iy[i][j] = max(matrix[i][j-1] + h + g,
                                  matrix_iy[i][j-1] + g)

    # replace python instance of negative max int with a negative infinity symbol
    for row in matrix:
        try:
            replacements = row.count(neg_infinity)
            for i in range(replacements):
                row[row.index(neg_infinity)] = "-∞"
        except ValueError:
            continue

    # print main matrix
    print("Matrix M")
    for row in matrix:
        print(row)

    # print alignment score based on matrix M
    print("\nAlignment Score:", matrix[n][m])
