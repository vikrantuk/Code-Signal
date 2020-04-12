'''
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.
'''

def differentSymbolsNaive(s):
    di = dict()
    for el in s:
        if el not in di:
            di[el]=0
    return(len(di))
