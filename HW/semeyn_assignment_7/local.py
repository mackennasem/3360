# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 7 - Global, Semi-Global, and Local Alignment
# File: local.py
# Due date: 2/28/2020

from global_a import match
from semi_global import traceback


def sw(s1, s2, g):
    n = len(s1)                                                             # get length of first sequence
    m = len(s2)                                                             # get length of second sequence
    matrix = []
    for i in range(n + 1):                                                  # create 2D list
        matrix.append([])
        for j in range(m + 1):                                              # initialize 2D list
            matrix[i].append(0)
    for i in range(1, n + 1):                                               # compare bases in each sequence and
        for j in range(1, m + 1):                                           # get similarity values to put in matrix
            matrix[i][j] = max(matrix[i][j - 1] + g,                        # take maximum of top, diagonal, left, and 0
                               matrix[i - 1][j - 1] + match(s1[i - 1], s2[j - 1]),
                               matrix[i - 1][j] + g,
                               0)

    length = max(len(s1), len(s2))                                          # get length of longer sequence
    align1 = []                                                             # initialize alignment lists
    align2 = []
    max_val = -10000                                                        # initialize max value for comparison
    i = -1                                                                  # initialize indexing value
    j = -1                                                                  # initialize indexing value
    row_num = 0                                                             # keep track of what row in the matrix
    for row in matrix:                                                      # go through 2D matrix and find max value
        for val in row:
            if val > max_val:
                max_val = val                                               # set new max value
                i = row_num                                                 # set indices of new max value
                j = row.index(val)
        row_num += 1                                                        # increment to next row

    print("Local Alignment Score:", matrix[i][j])                           # print alignment score
    traceback(i, j, s1, s2, matrix, align1, align2)                         # call traceback function
    print(''.join(align1))                                                  # print alignments
    print(''.join(align2))
    for row in matrix:                                                      # print matrix
        print(' '.join(map(str, row)))
