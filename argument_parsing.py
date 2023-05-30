"""Argument parsing means getting arguments from Command Line"""
"""In C and C++ we have int argc and char** argv to store the length and vector of arguments
   in python we use the system module to get argv
"""

import sys

#print(sys.argv)

""" Example - suppose we want the user to input filename and a message that he wants to write in that file
    we can do this using argument parsing
"""

#if len(sys.argv) < 3: #check so that user inputs correct number of parameters
#    raise Exception("Atleast 2 command line arguments required!")
#
#filename = sys.argv[1]
#message = sys.argv[2]
#
## USAGE: python3  file.py  filename  message
#with open(filename, "w+") as f:
#    f.write(message)


"""Optional Arguments (optargs)"""

import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message:"])

#NOTE: ':' in the above f:m: specifies that we expect some argument after -f or -m in command line

"""args are stored as positional arguments and opts as keyword arguments"""

print(opts)
print(args)

#python3 .\argument_parsing.py -m hello -f hello.txt random_text
#>>> [('-m', 'hello'), ('-f', 'hello.txt')]
#>>> ['random_text']
