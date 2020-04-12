'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''

def palindromeRearranging(inputString):
    dic = dict()
    oddflag = False

    for el in inputString:
        if(el not in dic):
            dic[el] = 1
        else:
            dic[el] += 1
    
    for el in dic:
        if(dic[el]%2!=0):
            if(oddflag == True):
                return False
            else:
                oddflag = True
    return True
