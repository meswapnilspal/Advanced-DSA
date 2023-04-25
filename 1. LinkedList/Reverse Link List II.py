"""
Q. Reverse Link List II -

Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.

"""



# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):
        if B == C:
            return A

        org_head = A
        head = A

        def get_start_and_end(head,curr,start,end):
            counter = 1
            prev = None
            before = None
            while (counter != end):

                prev = curr
                curr = curr.next
                counter += 1
                if counter == start:
                    before = prev
                if counter == end:
                    endp = curr
            
            if before is None:
                startp = head
            else:
                startp = before.next            
            
            after = endp.next

            return before, startp, endp, after
        
        def reverse_list(startp,endp):
            prev = None
            p1 = startp            
            while(prev != endp):
                t = p1.next
                p1.next = prev
                
                prev = p1
                p1 = t
        

        before, startp, endp, after = get_start_and_end(head,head,B,C)
        reverse_list(startp,endp)

        #connecting rest of the LL
        if before is None:
            head = endp
        else:
            before.next = endp
            head = org_head        
        
        startp.next = after
        
        return head