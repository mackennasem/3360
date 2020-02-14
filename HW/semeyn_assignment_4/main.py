# Author: Mackenna Semeyn
# Course: Computational Biology Spring 2020
# Due date: 2/14/2020
# File: main.py
# This program, given a multiset (list of integers) will output a set of X of integers such that L = DX and the number
# of integers in X.

import HW.semeyn_assignment_4.turnpike_functions.partial_digest
import sys


def main():
    if len(sys.argv) != 2:
        print("Error: Invalid number of parameters.")
    else:
        stripset = sys.argv[1].strip('[]').split(',')
        print(stripset)
        multiset = [int(i) for i in stripset]
        print(multiset)
        HW.semeyn_assignment_4.turnpike_functions.partial_digest.partial_digest(multiset)


if __name__ == '__main__':
    main()
