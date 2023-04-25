"""
Q. Remove Nth Node from List End -

Given a linked list A, remove the B-th node from the end of the list and return its head. For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5. NOTE: If B is greater than the size of the list, remove the first node of the list. NOTE: Try doing it using constant additional space.

"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        counter = 0
        curr = A
        while(curr is not None):
            curr = curr.next
            counter += 1
        
        if counter == 1 and B == 1:
            return None

        tar_pos = counter - B

        if tar_pos <= 0:
            A = A.next
            return A

        counter = 1
        curr = A
        while counter <= tar_pos and curr is not None:
            curr = curr.next
            counter += 1
            if counter == tar_pos:
                curr.next = curr.next.next
        
        return A