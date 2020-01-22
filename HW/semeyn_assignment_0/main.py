# Author: Mackenna Semeyn
# Computational Biology Spring 2020
# main.py

import sys                               # import for command line (program) arguments
import re                                # import for regex findall() method


def main():
    s1fasta = open(sys.argv[1], "r")     # opens s1 fasta file to read
    s2fasta = open(sys.argv[2], "r")     # opens s2 fasta file to read
    t = sys.argv[3]                      # set t equal to input value

    pattern_string = ""
    for letter in s2fasta:               # go through s2 file and get sequence to search for in s1
        if not letter.startswith('>'):   # skip any description lines
            pattern_string += letter     # append sequence
    s2length = len(pattern_string)       # get length of s2 sequence
    s2fasta.close()                      # close s2 fasta file

    match_string = ""
    for char in s1fasta:                 # go through s1 file and get sequence to be searched against
        if not char.startswith('>'):     # skip any description lines
            match_string += char         # append sequence
    s1length = len(match_string)         # get length of s1 sequence
    s1fasta.close()                      # close s1 fasta file

    # use regex to search for s2 within s1 and return all instances
    result = re.findall(pattern_string, match_string)
    # get number of matches (size of the array returned)
    num_matches = len(result)

    # expected frequency - cast to a float to preserve precision
    expected_frequency = float(s2length / s1length) * float(t)

    # output of results
    print("Length of s1: ", s1length)
    print("Length of s2:", s2length)
    print("Value of t:", t)
    print("Expected probability: ", expected_frequency)
    print("Observed frequency: ", num_matches)


if __name__ == "__main__":
    main()
