# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 6 - Global Alignment
# File: needleman_wunsch.py
# Due date: 2/26/2020

import sys


def nw(s1, s2, g):
    n = len(s1)                                                                 # get length of first sequence
    m = len(s2)                                                                 # get length of second sequence
    matrix = []
    for i in range(n+1):                                                        # create 2D list
        matrix.append([])
        for j in range(m+1):                                                    # initialize 2D list
            matrix[i].append(0)
    for i in range(0, n+1):                                                     # set boundary values for the row
        matrix[i][0] = i*g
    for j in range(0, m+1):                                                     # set boundary values for the column
        matrix[0][j] = j*g
    for i in range(1, n+1):                                                     # compare bases in each sequence and
        for j in range(1, m+1):                                                 # get similarity values to put in matrix
            matrix[i][j] = max(matrix[i][j-1] + g,                              # take maximum of top, diagonal, left
                               matrix[i-1][j-1] + match(s1[i-1], s2[j-1]),
                               matrix[i-1][j] + g)

    print("Global Alignment Score:", matrix[n][m])                              # print alignment score
    length = max(len(s1), len(s2))                                              # get length of longer sequence
    align1 = []                                                                 # initialize alignment lists
    align2 = []
    traceback(n, m, length, s1, s2, matrix, align1, align2)                     # call traceback function
    print(''.join(align1))                                                      # print alignments
    print(''.join(align2))


def match(i, j):
    if i == j:                                                                  # if bases are the same
        return int(sys.argv[4])                                                 # return match score
    else:
        return int(sys.argv[5])                                                 # return mismatch score


def traceback(i, j, length, s1, s2, matrix, align1, align2):
    g = int(sys.argv[3])                                                        # get gap penalty score
    if i == 0 and j == 0:                                                       # base case
        length = 0
    elif i > 0 and matrix[i][j] == matrix[i-1][j] + g:                          # if score came from top
        traceback(i-1, j, length, s1, s2, matrix, align1, align2)               # call traceback on top
        length += 1
        align1.append(s1[i-1])                                                  # add base to first sequence
        align2.append('-')                                                      # add gap to second sequence
    # if score came from diagonal
    elif i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + match(s1[i-1], s2[j-1]):
        traceback(i-1, j-1, length, s1, s2, matrix, align1, align2)             # call traceback on diagonal
        length += 1
        align1.append(s1[i-1])                                                  # add base to first sequence
        align2.append(s2[j-1])                                                  # add base to second sequence
    else:                                                                       # if score came from left
        traceback(i, j-1, length, s1, s2, matrix, align1, align2)               # call traceback on left
        length += 1
        align1.append('-')                                                      # add gap to first sequence
        align2.append(s2[j - 1])                                                # add base to second sequence
