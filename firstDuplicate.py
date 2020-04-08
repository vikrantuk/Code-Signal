def firstDuplicate(a):
    for i in range(len(a)):
        m = abs(a[i])
        if(a[m-1]<0):
            return m
        else:
            a[m-1]=-a[m-1]
    return(-1)
