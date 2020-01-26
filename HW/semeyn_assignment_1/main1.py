# Mackenna Semeyn
# Computational Biology Spring 2020
# main1.py
# This python script translates a DNA sequence without translation functions
# To exit the program, type 'q' and press enter


def main():
    while True:                                             # for each line of input from the user
        bad = False                                         # boolean for not printing an invalid complement
        line = input("Enter a DNA sequence: ")              # prompt and receive input
        trans = ""                                          # create new string for translation
        if 'q' == line.rstrip() or 'Q' == line.rstrip():    # exit commands for the program
            break
        for char in line:                                   # for each character in the input string
            if char == 'A' or char == 'a':                  # check for case-insensitive A
                trans += 'T'                                # translate to a T
            elif char == 'T' or char == 't':                # check for case-insensitive T
                trans += 'A'                                # translate to an A
            elif char == 'C' or char == 'c':                # check for case-insensitive C
                trans += 'G'                                # translate to a C
            elif char == 'G' or char == 'g':                # check for case-insensitive G
                trans += 'C'                                # translate to a G
            elif char == '\n':                              # check for end of sequence
                break                                       # end translation
            else:
                print("ERROR: Invalid sequence, ending translation.")
                bad = True                                  # indicate sequence has an invalid complement
                break                                       # end translation
        if not bad:                                         # if sequence has a valid complement
            reversecomp = ''.join(reversed(trans.upper()))  # reverse the complement to the sequence
            print(reversecomp)                              # print the reverse complement to standard out


if __name__ == '__main__':
    main()
