# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 6 - Global Alignment
# File: main.py
# Due date: 2/26/2020

import sys
from HW.semeyn_assignment_6.fasta import fasta
from HW.semeyn_assignment_6.needleman_wunsch import nw


def main():
    if len(sys.argv) != 6:                                  # check for the correct number of arguments
        print("Error: Invalid number of parameters.")
    seq = fasta()                                           # get two sequences from fasta files
    if len(seq) == 2:                                       # check to make sure two sequences are returned
        nw(seq[0], seq[1], int(sys.argv[3]))                # call Needleman-Wunsch algorithm
    else:
        print("Error: Invalid number of sequences.")


if __name__ == '__main__':
    main()
