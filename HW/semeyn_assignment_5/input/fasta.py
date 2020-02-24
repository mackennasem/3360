# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 5 - Motif Finding
# Due Date: 2/24/2020
# fasta.py
# This file validates if the given input file is in fasta format, then places the given DNA sequences in a set

import sys


def fasta():
    f = open(sys.argv[1])                               # import file from command line
    t_seq = []                                          # declare set for holding DNA sequences
    if f:                                               # if file was opened successfully
        for line in f:                                  # for every line in the fasta file
            if not line.startswith('>'):                # skip header lines
                t_seq.append(line.rstrip().lower())     # append DNA sequence to list as lowercase and no endline chars
        f.close()                                       # close file once complete
        return t_seq                                    # return set of DNA sequences
    else:
        print("ERROR: File unable to be opened.")       # print error message if file could not be opened
