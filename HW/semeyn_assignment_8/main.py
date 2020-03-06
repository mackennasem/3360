# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 8 - Affine Gap Penalty
# File: main.py
# Due date: 3/06/2020

import sys
from fasta import fasta
from affine import affine_gap


def main():
    if len(sys.argv) != 7:
        print("Error: Invalid number of parameters")
        sys.exit(1)

    seq = fasta()
    if len(seq) == 2:
        affine_gap(seq[0], seq[1])


if __name__ == '__main__':
    main()
