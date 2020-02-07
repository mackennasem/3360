# Mackenna Semeyn
# Computational Biology Spring 2020
# Assignment 3 - BLAST
# Due date: 2/7/2020
# blast.py

import subprocess
import sys


def refseq_blastn():
    # get taxid number from command line arguments
    taxid = sys.argv[2]

    # set value for e-value and output file
    if len(sys.argv) == 5:
        e_val = sys.argv[3]
        o_file = sys.argv[4]
    else:
        e_val = 10  # default value for e if not specified
        o_file = sys.argv[3]  # alternate index for file name

    # set arguments for Popen and blastn executable
    args = ['blastn.exe', '-db', 'Nucleotide collection', '-seqidlist', 'input.txt', 'taxids', taxid, '-evalue', e_val,
            '-out', o_file, '-outfmt "6 qseqid evalue ppos qseq"']
    query = subprocess.Popen(args)
    if query.returncode == 0:   # successful run indication
        print("TRUE")


def fasta_blastn():
    # get taxid number from command line arguments
    taxid = sys.argv[2]

    # set value for e-value and output file
    if len(sys.argv) == 5:
        e_val = sys.argv[3]
        o_file = sys.argv[4]
    else:
        e_val = 10  # default value for e if not specified
        o_file = sys.argv[3]  # alternate index for file name

    # get list of fasta files
    files = sys.argv[1].split(",").__str__()

    # loop for each fasta file
    for file in files:
        # set arguments for Popen and blastn executable
        args = ['blastn.exe', '-db', 'Nucleotide collection', 'taxids', taxid, '-query', file, '-out', o_file,
                '-outfmt "6 qseqid evalue ppos qseq"', '-evalue', e_val]
        query = subprocess.Popen(args)
        if query.returncode == 0:   # successful run indication
            print("TRUE")
