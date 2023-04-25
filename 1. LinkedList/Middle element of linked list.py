"""
Q. Middle element of linked list -

Given a linked list of integers, find and return the middle element of the linked list.
NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.

"""


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        slowP = A
        fastP = A
        while(fastP is not None and fastP.next is not None ):
            slowP = slowP.next
            fastP = fastP.next.next
        
        return slowP.val