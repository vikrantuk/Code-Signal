'''
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
'''

def rotateImage(a):
    for i in range(len(a)-1):
        a[0][i],a[0+i][len(a)-1],a[len(a)-1][len(a)-1-i],a[len(a)-1-i][0] = a[len(a)-1-i][0],a[0][i],a[0+i][len(a)-1],a[len(a)-1][len(a)-1-i]
        for j in range(len(a)-2*i-3):
            a[1+i][1+i+j],a[1+i+j][len(a)-2-i],a[len(a)-2-i][len(a)-2-i-j],a[len(a)-2-i-j][1+i] = a[len(a)-2-i-j][1+i],a[1+i][1+i+j],a[1+i+j][len(a)-2-i],a[len(a)-2-i][len(a)-2-i-j]
    return(a)
