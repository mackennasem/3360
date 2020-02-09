# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 2 - Ensembl
# main.py

import sys
from HW.semeyn_assignment_2.ensembl_functions.ensembl import get_sequence


def main():

    # Case 1: Invalid amount of user input
    if len(sys.argv) != 3:
        print("ERROR: Invalid number of program arguments")
    # Case 2: Valid amount of user input
    else:
        get_sequence()


if __name__ == '__main__':
    main()
