"""Argument parsing means getting arguments from Command Line"""
"""In C and C++ we have int argc and char** argv to store the length and vector of arguments
   in python we use the system module to get argv
"""

import sys

print(sys.argv)

""" Example - suppose we want the user to input filename and a message that he wants to write in that file
    we can do this using argument parsing
"""

if len(sys.argv) < 3: #check so that user inputs correct number of parameters
    raise Exception("Atleast 2 command line arguments required!")

filename = sys.argv[1]
message = sys.argv[2]

# USAGE: python3  file.py  filename  message
with open(filename, "w+") as f:
    f.write(message)

