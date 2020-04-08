''' Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
'''

def firstNotRepeatingCharacter(s):
    s1 = {}
    for el in s:
        if(el in s1):
            s1[el]+=1
        else:
            s1[el]=1
    for el in s:
        if(s1[el]<2):
            return(el)
    return('_')
