# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 3 - BLAST
# Due date: 2/7/2020
# input.py

import sys


def input_validation():
    # validate number of arguments
    if len(sys.argv) < 4:   # need at least 4 arguments: main.py, f1, f2, and o
        print("ERROR: Invalid number of arguments.")
        sys.exit()

    # validate f1
    params = sys.argv[1].split(",")     # split comma separated input into list elements
    refseq = False
    fasta = False
    # open input file for ref-seq ids
    f = open("input.txt", "x")
    for element in params:
        prefix = element[:2]    # get first two letters of string
        file_ext = element[-6:]     # get extension
        # check for ref-seq id prefixes
        if prefix == "AC" or prefix == "NC" or prefix == "NG" or prefix == "NT" or prefix == "NW" or prefix == "NS" \
                or prefix == "NZ" or prefix == "NM" or prefix == "NR" or prefix == "XM" or prefix == "XR" or \
                prefix == "AP" or prefix == "NP" or prefix == "YP" or prefix == "XP" or prefix == "ZP":
            refseq = True
            # check for mixed input
            if fasta:
                print("ERROR: Combined input types. Please enter a comma-separated list of Ref-Seq IDs or filenames"
                      " for query sequences.")
                sys.exit()
            # write ref-seq id to file for blastn executable to use
            f.write(element + '\n')
        elif file_ext == ".fasta":
            fasta = True
            # check for mixed input
            if refseq:
                print("ERROR: Combined input types. Please enter a comma-separated list of Ref-Seq IDs or filenames"
                      " for query sequences.")
                sys.exit()
        else:
            print("ERROR: Invalid form of input.")
            sys.exit()
    # close input file
    f.close()

    # validate f2
    # must be human, ecoli, or wuhan genome
    if sys.argv[2] != "9606" and sys.argv[2] != "562" and sys.argv[2] != "2697049":
        print("ERROR: Invalid TAXID.")
        sys.exit()

    # validate e
    if not sys.argv[3].isnumeric():
        print("ERROR: E-value is not a number.")
        sys.exit()
    # return codes to indicate what type of f1 input was used
    if refseq:
        return 1
    else:
        return 2
