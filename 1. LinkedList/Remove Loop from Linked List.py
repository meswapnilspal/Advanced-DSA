"""
Q. Remove Loop from Linked List -

You are given a linked list that contains a loop.
You need to find the node, which creates a loop and break it by making the node point to NULL.

"""


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slowP = A.next
        fastP = A.next.next

        while(slowP != fastP):
            slowP = slowP.next
            fastP = fastP.next.next
        
        fastP = A

        while(slowP.next != fastP.next):
            slowP = slowP.next
            fastP = fastP.next
        
        slowP.next = None

        return A