# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 7 - Global, Semi-Global, and Local Alignment
# File: main.py
# Due date: 2/27/2020

import sys
from fasta import fasta
from global_a import nw
from semi_global import semi
from local import sw


def main():
    if len(sys.argv) != 7:                                  # check for the correct number of arguments
        print("Error: Invalid number of parameters.")
        sys.exit()
    seq = fasta()                                           # get two sequences from fasta files
    if len(seq) == 2:                                       # check to make sure two sequences are returned
        if sys.argv[6] == "global":
            nw(seq[0], seq[1], int(sys.argv[3]))            # call Needleman-Wunsch algorithm
        elif sys.argv[6] == "semi-global":
            semi(seq[0], seq[1], int(sys.argv[3]))
        elif sys.argv[6] == "local":
            sw(seq[0], seq[1], int(sys.argv[3]))
        else:
            print("Error: Please choose 'global', 'semi-global', or 'local'")
    else:
        print("Error: Invalid number of sequences.")


if __name__ == '__main__':
    main()
