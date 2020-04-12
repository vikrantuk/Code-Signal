'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''

def addBorder(picture):
    temp=len(picture[0])
    picture.insert(0,'*'*(temp+2))
    picture.append('*'*(temp+2))
    for i in range(1,len(picture)-1):
        picture[i]='*'+picture[i]+'*'
    return(picture)
