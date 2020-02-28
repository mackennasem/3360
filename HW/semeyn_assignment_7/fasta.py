# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 7 - Global, Semi-Global, and Local Alignment
# File: fasta.py
# Due date: 2/27/2020

import sys
import re


def fasta():
    f = open(sys.argv[1])                                           # open first fasta file
    seq = []
    if f:                                                           # if file is open
        for line in f:
            if not line.startswith('>'):                            # skip information line in fasta file
                x = re.search(r"[^atcgACTG]", line)                 # search for any character that is not AGCT
                if not x:
                    seq.append(line)                                # add sequence to list
                else:
                    print("Error: Not a DNA sequence.")             # print error message
    else:
        print("Error: ", sys.argv[1], " cannot be opened.")         # print error message
    f.close()                                                       # close first fasta file
    f = open(sys.argv[2])                                           # open second fasta file
    if f:                                                           # if file is open
        for line in f:
            if not line.startswith('>'):                            # skip information line in fasta file
                x = re.search(r"[^atcgACTG]", line)                 # search for any character that is not AGCT
                if not x:
                    seq.append(line)                                # add sequence to list
                else:
                    print("Error: Not a DNA sequence.")             # print error message
    else:
        print("Error: ", sys.argv[2], " cannot be opened.")         # print error message
    f.close()                                                       # close second fasta file
    return seq                                                      # return two sequences in a list
