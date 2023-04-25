
"""
Q. Sort stack using another stack -

Given a stack of integers A, sort it using another stack.
Return the array of integers after sorting the stack using another stack.

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        tmp_stack = []
        while(A):
            t = A.pop()
            while (len(tmp_stack) > 0  and t < tmp_stack[-1] ):
                A.append(tmp_stack.pop())
            tmp_stack.append(t)
        
        return tmp_stack