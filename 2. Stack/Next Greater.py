"""
Q. Next Greater -

Given an array A, find the next greater element G[i] for every element A[i] in the array.
The next greater element for an element A[i] is the first greater element on the right side of A[i] in the array, A.

More formally:

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
	
Elements for which no greater element exists, consider the next greater element as -1.

"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        n = len(A)
        stack =[]
        ans = [0]*n
        for i in range(n):
            while( len(stack) > 0 and A[i] > A[stack[-1]] ):
                ans[stack[-1]] = A[i]
                stack.pop()
            stack.append(i)
        
        for idx in stack:
            ans[idx] = -1
        
        return ans