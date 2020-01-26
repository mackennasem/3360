# Mackenna Semeyn
# Computational Biology Spring 2020
# main2.py
# This python script translates a DNA sequence with translation functions
# To exit the program, type 'q' and press enter

import re                                                       # import for regex search function


def main():
    pre = "ATCG"                                                # characters that need to be replaced
    post = "TAGC"                                               # characters to replace with
    transtable = str.maketrans(pre, post)                       # create translation table
    while True:
        line = input("Enter a DNA sequence: ")                  # prompt and receive input
        if 'q' == line.rstrip() or 'Q' == line.rstrip():        # check for exit command
            break
        match = re.search(r'[^ATCGatcg]', line)                 # use regex to search for any invalid characters
        if not match:                                           # if no matches for invalid characters
            # translate and reverse the DNA sequence
            reversecomp = ''.join(reversed(str.translate(line.upper(), transtable)))
            print(reversecomp)                                  # print the reverse complement to standard out
        else:
            print("ERROR: Invalid sequence, ending translation.")


if __name__ == '__main__':
    main()
