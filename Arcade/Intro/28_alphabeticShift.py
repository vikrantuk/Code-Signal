'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
'''

def alphabeticShift(inputString):
    res =""
    for el in inputString:
        res+=chr((ord(el)+1-97)%26+97)
    return res
