# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 5 - Motif Finding
# Due Date: 2/24/2020
# motif_functions.py
# This file contains functions for scoring distance and other stuff
import collections

from HW.semeyn_assignment_5.input.fasta import fasta
import sys


# run time: O(n)
# finding distance between motifs
def hamming_distance(v, w):
    dist = 0                        # initialize distance to zero
    for ch1, ch2 in zip(v, w):      # for each character in two strings of equal length
        if ch1 != ch2:              # if the characters are not equal
            dist += 1               # increment the distance by one
    return dist                     # return the total distance between the strings


# store nodes in level order in an array (similar to heap implementation)
def make_suffix_tree():
    alphabet = ['1', '2', '3', '4']                                          # create alphabet
    suffix_length = int(sys.argv[2])                                         # get length of suffix
    alpha_length = 4                                                         # set length of alphabet
    suffixes = ['0']                                                         # initialize array with root node
    total_nodes = int((alpha_length**(suffix_length+1)-1)/(alpha_length-1))  # calculate total number of nodes in tree
    node_count = 1                                                           # nodes in the tree so far
    for i in range(alpha_length):                                            # add first level of nodes
        suffixes.append(alphabet[i])
        node_count += 1
    alpha_count = 0
    for i in range(node_count - 1, total_nodes - 1):                         # create the rest of the suffix tree
        suffixes.append(suffixes[int(i/alpha_length)] + alphabet[alpha_count])
        alpha_count += 1
        if alpha_count == 4:                                                 # reset index if out of range
            alpha_count = 0
    return suffixes                                                          # return suffix tree stored in an array


# translate alpha characters to numeric representation
def translate_dna(t_seq):
    dna = []                                            # make empty list for translated sequences
    for seq in t_seq:                                   # for each DNA sequence from the fasta file
        translation = seq.maketrans("acgt", "1234")     # make translation table
        dna.append(seq.translate(translation))          # add translated sequence to new list
    return dna                                          # return list of translated sequences


# translate alpha characters to numeric representation
def translate_nums(t_seq):
    dna = []                                            # make empty list for translated sequences
    for seq in t_seq:                                   # for each numeric representation of the sequences
        translation = seq.maketrans("1234", "acgt")     # make translation table
        dna.append(seq.translate(translation))          # add translated sequence to new list
    # print(dna)
    return dna                                          # return list of translated sequences


# get unique l-mers from each sequence of DNA in the fasta file
def find_lmers(dna):
    lmers = []                                      # declare empty list for sets of all possible l-mers per sequence
    for seq in dna:                                 # for each sequence of DNA from the fasta file
        a = []                                      # declare empty list for possible l-mers
        tail = int(sys.argv[2])                     # get length of l-mers
        for i in range(len(seq) - (tail - 1)):      # get all possible l-mers
            a.append(seq[i:tail])                   # split string based on indices
            tail += 1                               # increment the tail index
        a = list(set(a))                            # get unique l-mers
        a.sort()                                    # sort l-mers in ascending order
        lmers.append(a)                             # add set to list of all sets
    return lmers                                    # return list of all sets of l-mers for each sequence


def get_distance(lmers, suffixes):
    one = []
    index = first_child()                                    # get index of first leaf node to narrow search space
    for l_set in lmers:                                      # for every list in lmers
        dist_one = []
        for lmer in l_set:                                   # for each l-mer in the list
            for suffix in suffixes[index:len(suffixes)]:     # for each suffix in the suffix tree
                dist = hamming_distance(lmer, suffix)        # compare the l-mer with the suffix
                if dist == 0:                                # if found in the suffix tree
                    dist_one.append(suffix)                  # add to list of results for l-mer
        one.append(dist_one)
    result = []
    for elem in one:                                         # filter out duplicates
        elem = list(set(elem))                               # get unique suffixes from sublist
        elem.sort()                                          # sort into ascending order
        result.append(elem)                                  # append to result set

    return find_motifs(result)                               # call find function to get result list of motifs


# find index of first leaf node in suffix tree array
def first_child():
    alpha_length = 4                    # length of the alphabet
    motif_length = int(sys.argv[2])     # length of the motif being found
    index = 0                           # initialize index to 0
    for i in range(motif_length):       # sum up number of nodes above leaf nodes
        index += alpha_length ** i      # add number of nodes at given level to sum
    return index                        # return index of first leaf node in the array


# find all motifs common between DNA sequences
def find_motifs(result):
    res = set(result[0]).intersection(*result[1:])      # convert to a set and find the intersection between sublists
    motifs = list(res)                                  # convert result set into a list
    return translate_nums(motifs)                       # translate result set back into DNA sequences
