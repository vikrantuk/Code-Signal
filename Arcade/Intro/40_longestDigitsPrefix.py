'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
'''

def longestDigitsPrefix(inputString):
    s=""
    for el in inputString:
        if(el.isnumeric()):
            s+=el
        else:
            return(s)
    return(s)
