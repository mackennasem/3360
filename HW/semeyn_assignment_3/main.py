# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 3 - BLAST
# Due date: 2/7/2020
# main.py

from HW.semeyn_assignment_3.validate.input import input_validation
from HW.semeyn_assignment_3.blast_functions.blast import refseq_blastn, fasta_blastn


def main():
    val = input_validation()  # call to verify input

    # run function based on type of input in f1
    if val == 1:
        refseq_blastn()
    elif val == 2:
        fasta_blastn()
    else:
        return


if __name__ == '__main__':
    main()
