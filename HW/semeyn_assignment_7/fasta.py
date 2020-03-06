# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 7 - Global, Semi-Global, and Local Alignment
# File: fasta.py
# Due date: 2/27/2020

import sys


def fasta():
    f = open(sys.argv[1])                                           # open first fasta file
    seq = []
    if f:                                                           # if file is open
        for line in f:
            if not line.startswith('>'):                            # skip information line in fasta file
                dna_check(line)                                     # check if sequence is only AGTC
                seq.append(line)
    else:
        print("Error: ", sys.argv[1], " cannot be opened.")         # print error message
    f.close()                                                       # close first fasta file
    f = open(sys.argv[2])                                           # open second fasta file
    if f:                                                           # if file is open
        for line in f:
            if not line.startswith('>'):                            # skip information line in fasta file
                dna_check(line)                                     # check if sequence is only AGTC
                seq.append(line)
    else:
        print("Error: ", sys.argv[2], " cannot be opened.")         # print error message
    f.close()                                                       # close second fasta file
    return seq                                                      # return two sequences in a list


def dna_check(sequence):
    # for each base in the sequence, check to make sure it only contains A, C, G, and T
    for base in sequence:
        if not base.lower() == 'a' and not base.lower() == 'g' and not base.lower() == 'c' and not base.lower() == 't':
            print("Error: Not a valid DNA sequence")
            sys.exit(1)
