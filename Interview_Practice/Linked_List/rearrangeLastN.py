'''
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if(l==None or n==0):
        return l
    li=[]
    while(l!=None):
        li.append(l)
        l= l.next
    l=li[-n]
    m=l
    for i in range(len(li)-n+1,len(li)):
        l.next=li[i]
        l=l.next
    for i in range(len(li)-n):
        l.next=li[i]
        l=l.next
    l.next=None
    return m
