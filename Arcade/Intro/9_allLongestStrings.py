'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''

def allLongestStrings(inputArray):
    li=[inputArray[0]]
    for i in range(1,len(inputArray)):
        if(len(inputArray[i])==len(li[0])):
            li.append(inputArray[i])
        elif(len(inputArray[i])>len(li[0])):
            li=[]
            li.append(inputArray[i])
    return(li)
