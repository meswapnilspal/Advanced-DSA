"""
Q. Balanced Paranthesis -

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.
Refer to the examples for more clarity.

"""

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
        s = list()
        n = len(A)
        for i in range(n):
            if len(s) == 0:
                s.append(A[i])
                continue
            
            cond1 = s[-1] == '(' and A[i] == ')'
            cond2 = s[-1] == '[' and A[i] == ']'
            cond3 = s[-1] == '{' and A[i] == '}' 

            if cond1 or cond2 or cond3:
                s.pop()
            else:
                s.append(A[i])
            
        if len(s) == 0:
            return 1
        return 0
