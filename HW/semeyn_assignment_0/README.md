# Assignment 0 - Probablility
main.py file has three program arguments: the file path for s1, the file path for s2, and the integer for t

The Process:
- The fasta file for s2 is read, skipping any lines that begin with '>' indicating a description line
- The size of s2 is calculated based on the length of the string 
- The fasta file for s1 is read, skipping any lines that begin with '>' indicating a description line
- The size of s1 is calculated based on the length of the string
- Regex function re.findall(s2, s1) is used to calculate all instances of the string s2 in the string s1
- The expected probability is calculated using the equation: s2 length / s1 length * t
- The observed frequency of s2 in s1 is calculated by finding the size of the array returned by re.findall(s2, s1)
- The results are printed to the screen