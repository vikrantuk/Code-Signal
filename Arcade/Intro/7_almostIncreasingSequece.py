'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
'''

def almostIncreasingSequence(sequence):
    found = 0
    if(len(sequence)==2):
        return(True)
    for i in range(1,len(sequence)):
        if(sequence[i]<=sequence[i-1]):
            if(found!=0):
                return(False)
            if(i==1 or sequence[i-2]< sequence[i]):
                found += 1
            if(i==len(sequence)-1 or sequence[i-1]<sequence[i+1]):
                found += 1
            if(found == 0):
                return(False)
        print(found)
    return True
