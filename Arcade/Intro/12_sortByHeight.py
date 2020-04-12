'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''

def sortByHeight(a):
    li=[]
    for i in range(len(a)):
        if(a[i]==(-1)):
            li.append(i)
    a.sort()
    for i in range(len(li)):
        a.insert(li[i]+len(li)-1-i,a.pop(0))
    return(a)
