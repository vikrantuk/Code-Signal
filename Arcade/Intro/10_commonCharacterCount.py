'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''

def commonCharacterCount(s1, s2):
    dic = dict()
    dic1= dict()
    count = 0
    for el in s1:
        if(el not in dic):
            dic[el]=1
        else:
            dic[el]+=1
    for el in s2:
        if(el not in dic1):
            dic1[el]=1
        else:
            dic1[el]+=1
    for el in dic:
        if(el in dic1):
            count+=min(dic[el],dic1[el])
    return(count)
