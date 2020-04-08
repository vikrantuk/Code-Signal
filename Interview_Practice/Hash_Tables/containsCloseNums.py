'''
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
containsCloseNums(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.
'''

def containsCloseNums(nums, k):
    dic = dict()
    for i in range(len(nums)):
        if(nums[i] not in dic):
            dic[nums[i]]=list()
        dic[nums[i]].append(i)
    for elm in list(dic.keys()):
        if(len(dic[elm])<2):
            del dic[elm]
    
    for el in dic:
        res=chk(dic[el],k)
        if(res==True):
            return(res)
    return(False)

def chk(li,k):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(abs(li[i]-li[j])<=k):
                return(True)
    return(False)
