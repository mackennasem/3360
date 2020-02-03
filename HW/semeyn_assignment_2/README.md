Assignment 2 - ENSEMBL

import statements used in ensembl.py:
- ftplib
- io
- sys
- requests
- os
- time
- gzip
- urllib.request
- urllib.error

import statements used in main.py:
- sys

This assignments takes two arguments from the command line, the first argument being either a Ref-Seq ID or a taxid. 
The second argument is the name of the file to save the sequence information to without the file extension. The program 
saves the filename with the extension ".fasta" so the user does not need to.

main.py imports the get_sequence() function from ensembl.py, and the rest of the code is executed by the functions in 
ensembl.py.
