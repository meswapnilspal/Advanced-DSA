"""
Q. Reverse Linked List -

You are given a singly linked list having head node A. You have to reverse the linked list and return the head node of that reversed list.
NOTE: You have to do it in-place and in one-pass.

"""


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):
        prev = None
        curr = A

        while(curr is not None):
            currP1 = curr.next
            curr.next = prev
            prev = curr
            curr = currP1

        return prev