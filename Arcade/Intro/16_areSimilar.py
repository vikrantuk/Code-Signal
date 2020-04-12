'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
'''

def areSimilar(a, b):
    count=0
    w,x,y,z=0,0,0,0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            count+=1
            if(count==1):
                w,x=a[i],b[i]
            if(count==2):
                y,z=a[i],b[i]
    if(count==2 or count==0):
        if(w==z and x==y):
            return True
        else:
            return False
    else:
        return False
