# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 5 - Motif Finding
# Due Date: 2/24/2020
# main.py
# This file contains the main function that validates the input and calls the necessary
# functions to find the putative motif

import sys
from semeyn_assignment_5.input.fasta import fasta
from semeyn_assignment_5.motif.motif_functions import get_distance, translate_dna, find_lmers, make_suffix_tree


def main():
    # check for valid number of arguments
    if len(sys.argv) != 3:
        print("ERROR: Invalid number of arguments.")
    else:
        t_seq = fasta()                          # get set of DNA sequences from the fasta file
        dna = translate_dna(t_seq)               # translate DNA sequences into numeric sequences
        tree = make_suffix_tree()                # create suffix tree
        all_lmers = find_lmers(dna)              # find all possible l-mers
        results = get_distance(all_lmers, tree)  # get result set of motifs
        if results:                              # print out results
            print("Motif(s):", *results, sep=" ")
        else:
            print("No motif found.")


if __name__ == '__main__':
    main()
