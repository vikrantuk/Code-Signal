'''
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.
'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    s1=""
    s2=""
   
    while(a!=None):
        if(len(str(a.value))<4):
            s1+="0"*(4-len(str(a.value)))
        s1+=str(a.value)
        a=a.next
    while(b!=None):
        if(len(str(b.value))<4):
            s2+="0"*(4-len(str(b.value)))
        s2+=str(b.value)
        b=b.next
    s1=str(int(s1)+int(s2))
    rs1=s1[::-1]
    li=[]   #slice rs1 in 4 from last and store in li then reverse li and add each element in n
    for el in range(0,len(s1),4):
        v=rs1[el:el+4]
        li.append(v[::-1])
    li.reverse()
    n = ListNode(int(li[0]))
    a=n
    for el in range(1,len(li)):
        n.next=ListNode(int(li[el]))
        n=n.next
    return a
